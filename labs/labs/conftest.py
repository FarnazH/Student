"""Test Configuration."""


def pytest_collectstart(collector):
    """Skip certain output types checked by nval plugin."""
    collector.skip_compare += 'application/javascript', 'text/plain', # 'text/html', 'stderr',
