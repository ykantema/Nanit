import pytest

@pytest.mark.backend
def test_stream_quality_degrades_on_poor_condition(streaming_validator):
        # Initial validation under normal conditions
        streaming_validator.validate_streaming_status("normal")

        streaming_validator.set_network_condition("poor")

        streaming_validator.validate_streaming_performance("poor")


statuses = ["normal", "poor", "offline"]
@pytest.mark.parametrize("status", statuses)
@pytest.mark.backend
def test_stream_quality_changes_on_varied_conditions(streaming_validator, status):
            streaming_validator.set_network_condition(status)
            streaming_validator.validate_streaming_status(status)