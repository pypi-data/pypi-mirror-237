import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "only: only run tests with this marker"
    )


def pytest_runtest_setup(item):
    marker_names = [mark.name for mark in item.iter_markers()]
    if 'only' not in marker_names:
        pytest.skip('only not present')
