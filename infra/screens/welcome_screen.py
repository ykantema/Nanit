from typing import Any

from assignment.infra.mobile_locators import get_screen
from assignment.infra.mobile_session import MobileSession


class WelcomeScreen:
    def __init__(self, sess: MobileSession):
        self.s = sess

    def is_displayed(self) -> bool:
        el = self.s.find_element("login_button_" + self.s.platform_name)
        return el.is_displayed()

