import os
import logging
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence, TypeVar


logger = logging.getLogger(__name__)


_DEFAULT_FALLBACK_STATUS_CODES = {400, 401, 403, 408, 409, 429, 500, 502, 503, 504}
_DEFAULT_FALLBACK_EXCEPTION_NAMES = {"APIConnectionError", "APITimeoutError", "ServiceRequestError"}


T = TypeVar("T")


@dataclass(frozen=True)
class EnvSet:
    group: str
    index: int
    values: Dict[str, str]


_preferred_env_set_index: Dict[str, int] = {}


def set_preferred_env_set(group: str, index: int) -> None:
    _preferred_env_set_index[group] = index


def get_preferred_env_set(group: str) -> Optional[int]:
    return _preferred_env_set_index.get(group)


def iter_exception_candidates(exc: Exception):
    candidates = [
        exc,
        getattr(exc, "__cause__", None),
        getattr(exc, "__context__", None),
    ]
    if getattr(exc, "args", None):
        candidates.extend(list(exc.args))

    for obj in candidates:
        if obj is None:
            continue
        if not isinstance(obj, BaseException):
            continue
        yield obj


def extract_status_code(exc: Exception) -> Optional[int]:
    for obj in iter_exception_candidates(exc):
        status_code = getattr(obj, "status_code", None)
        if status_code is None and getattr(obj, "response", None) is not None:
            status_code = getattr(obj.response, "status_code", None)
        if status_code is not None:
            try:
                return int(status_code)
            except Exception:
                return status_code

    return None


def is_fallback_eligible_error(
    exc: Exception,
    *,
    status_codes: Optional[set[int]] = None,
    exception_names: Optional[set[str]] = None,
) -> bool:
    if isinstance(exc, (ValueError, TypeError)):
        return False

    status_codes = status_codes or _DEFAULT_FALLBACK_STATUS_CODES
    exception_names = exception_names or _DEFAULT_FALLBACK_EXCEPTION_NAMES

    status_code = extract_status_code(exc)
    if status_code in status_codes:
        return True

    for obj in iter_exception_candidates(exc):
        if type(obj).__name__ in exception_names:
            return True

    return False


def run_with_env_set_fallback(
    *,
    env_sets: Sequence[EnvSet],
    group: str,
    op_name: str,
    fn: Callable[[], T],
    on_env_set_change: Optional[Callable[[EnvSet], None]] = None,
    is_eligible_error: Optional[Callable[[Exception], bool]] = None,
    log_env_sets: bool = True,
    call_on_env_set_change_for_first_attempt: bool = False,
) -> T:
    if not env_sets:
        return fn()

    if log_env_sets:
        logger.debug("%s env sets available: %s", op_name, [s.index for s in env_sets])

    last_exc: Exception | None = None
    for attempt_idx, env_set in enumerate(env_sets):
        set_preferred_env_set(group, env_set.index)
        if on_env_set_change is not None and (
            call_on_env_set_change_for_first_attempt or attempt_idx > 0
        ):
            on_env_set_change(env_set)

        try:
            return fn()
        except Exception as e:
            last_exc = e
            eligible = (
                is_eligible_error(e) if is_eligible_error is not None else is_fallback_eligible_error(e)
            )
            if eligible:
                logger.warning(
                    "%s failed (status=%s) on env set %s; trying next env set",
                    op_name,
                    extract_status_code(e),
                    env_set.index,
                )
                continue
            raise

    if last_exc is not None:
        raise last_exc
    raise RuntimeError(f"{op_name} failed without exception")


async def run_with_env_set_fallback_async(
    *,
    env_sets: Sequence[EnvSet],
    group: str,
    op_name: str,
    fn: Callable[[], Any],
    on_env_set_change: Optional[Callable[[EnvSet], None]] = None,
    is_eligible_error: Optional[Callable[[Exception], bool]] = None,
    log_env_sets: bool = True,
    call_on_env_set_change_for_first_attempt: bool = False,
) -> Any:
    if not env_sets:
        return await fn()

    if log_env_sets:
        logger.debug("%s env sets available: %s", op_name, [s.index for s in env_sets])

    last_exc: Exception | None = None
    for attempt_idx, env_set in enumerate(env_sets):
        set_preferred_env_set(group, env_set.index)
        if on_env_set_change is not None and (
            call_on_env_set_change_for_first_attempt or attempt_idx > 0
        ):
            on_env_set_change(env_set)

        try:
            return await fn()
        except Exception as e:
            last_exc = e
            eligible = (
                is_eligible_error(e) if is_eligible_error is not None else is_fallback_eligible_error(e)
            )
            if eligible:
                logger.warning(
                    "%s failed (status=%s) on env set %s; trying next env set",
                    op_name,
                    extract_status_code(e),
                    env_set.index,
                )
                continue
            raise

    if last_exc is not None:
        raise last_exc
    raise RuntimeError(f"{op_name} failed without exception")


def _env_name(base: str, index: int) -> str:
    return base if index == 0 else f"{base}_{index}"


def _get_env(base: str, index: int) -> Optional[str]:
    value = os.getenv(_env_name(base, index))
    if value is None:
        return None
    value = value.strip()
    return value or None


def any_env_var_present(bases: Sequence[str]) -> bool:
    for base in bases:
        v = os.getenv(base)
        if v is not None and v.strip():
            return True

    for name, value in os.environ.items():
        if value is None or not str(value).strip():
            continue
        for base in bases:
            prefix = f"{base}_"
            if not name.startswith(prefix):
                continue
            suffix = name[len(prefix) :]
            if suffix.isdigit():
                return True

    return False


def get_env_sets(
    group: str,
    required: Sequence[str],
    optional: Sequence[str] = (),
    defaults: Optional[Dict[str, str]] = None,
) -> List[EnvSet]:
    defaults = defaults or {}

    indices: set[int] = set()

    for base in list(required) + list(optional):
        if os.getenv(base):
            indices.add(0)

    for name in os.environ.keys():
        for base in list(required) + list(optional):
            prefix = f"{base}_"
            if not name.startswith(prefix):
                continue
            suffix = name[len(prefix) :]
            if suffix.isdigit():
                indices.add(int(suffix))

    ordered_indices = sorted(indices)

    preferred = get_preferred_env_set(group)
    if preferred is not None and preferred in ordered_indices:
        ordered_indices.remove(preferred)
        ordered_indices.insert(0, preferred)

    env_sets: List[EnvSet] = []
    for idx in ordered_indices:
        values: Dict[str, str] = {}

        ok = True
        for base in required:
            v = _get_env(base, idx)
            if v is None:
                ok = False
                break
            values[base] = v

        if not ok:
            continue

        for base in optional:
            v = _get_env(base, idx)
            if v is None:
                v = defaults.get(base)
            if v is not None:
                values[base] = v

        env_sets.append(EnvSet(group=group, index=idx, values=values))

    return env_sets


def get_active_env_set(
    group: str,
    required: Sequence[str],
    optional: Sequence[str] = (),
    defaults: Optional[Dict[str, str]] = None,
) -> Optional[EnvSet]:
    sets = get_env_sets(group=group, required=required, optional=optional, defaults=defaults)
    if not sets:
        return None

    active = sets[0]
    if get_preferred_env_set(group) is None:
        set_preferred_env_set(group, active.index)

    return active
