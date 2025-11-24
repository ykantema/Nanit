from assignment.infra.mobile_locators import get_screen
from assignment.infra.mobile_session import MobileSession

ids = {
    "live_stream_container": {
        "iOS": "live_stream_container_ios",
        "Android": "live_stream_container_android",
    },
    "stream_status_label": {
        "iOS": "stream_status_label_ios",
        "Android": "stream_status_label_android",
    }
}


class LiveStreamScreen:
    """Live stream screen verifications and actions."""

    def __init__(self, sess: MobileSession):
        self.s = sess

    def is_displayed(self) -> bool:
        el = self.s.find_element(ids["live_stream_container"][self.s.platform_name])
        return el.is_displayed()

    def stream_status(self) -> None:
        el = self.s.find_element(ids["stream_status_label"][self.s.platform_name])
        return el.text

