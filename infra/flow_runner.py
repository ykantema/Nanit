class FlowRunner:
    def __init__(self, api_client, ui_client, mode="both"):
        self.api = api_client
        self.ui = ui_client
        self.mode = mode

        # map each step to strategies
        self._navigate_strategies = {
            "ui": lambda: self.ui.navigate_to_stream(),
            "api": lambda: self.api.prepare_stream(),
            "both": lambda: (self.ui.navigate_to_stream(), self.api.prepare_stream())
        }

        self._validate_strategies = {
            "ui": lambda: self.ui.is_stream_visible(),
            "api": lambda: self.api.get_health() == "streaming",
            "both": lambda: (
                self.ui.is_stream_visible() or
                self.api.get_health() == "streaming"
            )
        }

    def navigate_to_stream(self):
        # just delegate, no if
        self._navigate_strategies[self.mode]()

    def validate_stream(self):
        assert self._validate_strategies[self.mode]()
