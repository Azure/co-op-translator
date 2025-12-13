import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence


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
