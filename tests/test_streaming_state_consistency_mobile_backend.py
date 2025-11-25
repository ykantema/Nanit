import pytest

@pytest.mark.streaming
def test_streaming_state_consistency_mobile_backend(flow_runner):
    flow_runner.navigate_to_stream()
    flow_runner.validate_stream()