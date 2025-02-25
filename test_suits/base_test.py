import pytest

@pytest.mark.usefixtures("init_logger", "init_driver")
class BaseTest:
    """Base test class that will inherit the conftest fixture."""
    pass
