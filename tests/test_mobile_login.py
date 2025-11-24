import pytest

from assignment.infra.screens import WelcomeScreen, LoginScreen, LiveStreamScreen


@pytest.mark.mobile
def test_login_flow_happy_path(mobile_session):
    """Happy-path: Welcome -> Login -> Live Stream (uses LOCATORS config).

    This is intentionally short and reads like a user story.
    """
    welcome = WelcomeScreen(mobile_session)
    assert welcome.is_displayed(), "Welcome should be visible"

    login = LoginScreen(mobile_session)
    assert login.is_displayed(), "Login should be visible"
    assert login.logged_in(), "Login should be logged in"

    live_stream = LiveStreamScreen(mobile_session)
    assert live_stream.is_displayed(), "Live Stream should be visible"
    assert live_stream.stream_status() == "Live", "Stream should be live"



