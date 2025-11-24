from time import sleep

from assignment.infra.mobile_locators import get_screen
from assignment.infra.mobile_session import MobileSession

ids ={
  "email_input": {
    "iOS": "email_input_ios",
    "Android": "email_input_android"
  },
  "password_input": {
    "iOS": "password_input_ios",
    "Android": "password_input_android"
  },
  "login_button": {
    "iOS": "login_button_ios",
    "Android": "login_button_android"
  },
  "terms_and_conditions_check_box": {
    "iOS": "terms_and_conditions_check_box_ios",
    "Android": "terms_and_conditions_check_box_android"
  }
}

class LoginScreen:
    """Login screen interactions."""

    def __init__(self, sess: MobileSession):
        self.s = sess

    def wait_for_displayed(self, timeout) -> bool:
        for _ in range(timeout):
            try:
                self.is_displayed()
                return True
            except:
                sleep(1)
        return False

    def is_displayed(self) -> bool:
        self.s.find_element(ids["email_input"][self.s.platform_name])
        return True

    def logged_in(self) -> bool:
        el = self.s.find_element(ids["login_button"][self.s.platform_name]).click()
        return not el.is_enabled()
