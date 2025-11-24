import logging

from assignment.infra.base_session import BaseSession
from screens.login_screen import LoginScreen
LOGGER = logging.getLogger(__name__)


class MobileSession(BaseSession):

    def __init__(
        self,
        platform_name
    ) -> None:
        # store provided platform_name as-is (None allowed). start_session enforces presence.
        self.platform_name = platform_name
        self.login_screen = LoginScreen(platform_name)

    # --- lifecycle ---
    def start_session(self) -> str:
        """Begin a fake session and populate some demo elements."""
        # Require an explicit platform_name (or a class-level default) before starting.
        if self.started:
            return self.session_id

    def end_session(self) -> None:
        """Terminate the mock session and clear state."""
        LOGGER.debug("Ending mock session %s", self.session_id)


    def launch_app(self) -> None:
        """Simulate launching the app."""
        LOGGER.debug("Launching app in mock session")

    def login_screen_visible(self) -> bool:
        """Simulate checking if the login screen is visible."""
        self.login_screen.is_displayed()
        LOGGER.debug("Checking if login screen is visible in mock session")
        self.set_session_state({"login_screen": "displayed"})
        return True

    def find_element(self, name):
        """Simulate finding an element by name."""
        LOGGER.debug("Finding element '%s' in mock session", name)
        return None