class BaseSession:
    session_state = {}
    def get_session_state(self):
        return self.session_state

    def set_session_state(self, session_state):
        self.session_state += session_state