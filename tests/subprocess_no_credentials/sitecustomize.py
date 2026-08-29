"""Prevent subprocess integration tests from loading developer .env files."""

import dotenv


def _disabled_load_dotenv(*args, **kwargs) -> bool:
    return False


dotenv.load_dotenv = _disabled_load_dotenv
