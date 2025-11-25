import pytest

from assignment.infra.flow_runner import FlowRunner
from assignment.infra.mobile_session import MobileSession
from assignment.infra.streaming_validator import StreamingValidator


def pytest_addoption(parser):
    parser.addoption(
        "--platform-name",
        action="store",
        default="android",
        help="Platform name for MobileSession (default: android)"
    )
    parser.addoption(
        "--layer",
         action="store",
         default="both",
         help="both, api, ui"
    )

@pytest.fixture(scope="session")
def mobile_session(request):
    """Create and yield a MobileSession; ensure it is ended after the test."""
    platform = request.config.getoption("--platform-name")
    sess = MobileSession(platform_name=platform)
    sess.start_session()
    try:
        yield sess
    finally:
        sess.end_session()

@pytest.fixture(scope="session")
def streaming_validator():
    StreamingValidator()

@pytest.fixture
def flow_runner(request, streaming_validator, mobile_session):
    layer = request.config.getoption("--layer")
    return FlowRunner(streaming_validator, mobile_session, layer)
