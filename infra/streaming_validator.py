"""
StreamingValidator for the service running at the given base URL.

- fetch_health_metric() performs GET /health and returns parsed JSON.
- get_metric_value() extracts a numeric metric by key.
- validate_streaming_performance() verifies metric within optional bounds.
- set_network_condition() POSTs to /control/network/<condition> to change network state.

Base URL default: http://localhost:8082
"""

import logging
from typing import Any, Optional

import requests

from assignment.infra.base_session import BaseSession

LOGGER = logging.getLogger(__name__)


def get_latency_expected(status: str) -> Optional[float]:
    """Return expected latency in ms for a given network condition."""
    mapping = {
        "normal": 50.0,
        "poor": 200.0,
        "offline": None,
    }
    return mapping.get(status)


class StreamingValidator(BaseSession):

    def __init__(self, base_url: str = "http://localhost:8082", timeout: float = 5.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = float(timeout)
        self.session = requests.Session()

    def _url(self, path: str) -> str:
        """Construct a full URL for a given path (path should start with '/')."""
        if not path.startswith("/"):
            path = f"/{path}"
        return f"{self.base_url}{path}"

    def fetch_health_status(self) -> Any:
        """GET /health and return parsed JSON.

        Raises requests.HTTPError or other request exceptions on network failure.
        """
        url = self._url("/health")
        LOGGER.debug("GET %s", url)
        resp = self.session.get(url, timeout=self.timeout)
        if resp.status_code != requests.codes.ok:
            raise requests.HTTPError(f"Failed to fetch /health: {resp.status_code} {resp.reason}")
        else:
            return resp.json()


    def fetch_metric_values(self) -> Any:
        url = self._url("/control/network/current")
        LOGGER.debug("GET %s", url)
        resp = self.session.get(url, timeout=self.timeout)
        if resp.status_code != requests.codes.ok:
            raise requests.HTTPError(f"Failed to fetch /health: {resp.status_code} {resp.reason}")
        else:
            return resp.json()

    def validate_streaming_performance(self, status):
        """Validate that the 'status' metric matches the expected status."""
        metric_value = self.fetch_health_status()
        assert metric_value["current_condition"] == status
        assert metric_value["settings"]["latency_ms"] == get_latency_expected(status)

    def get_metric_value(self, key) -> any:
        """Extract a value from /health JSON by key.
        """
        data = self.fetch_metric_values()["settings"]
        if key in data:
            return data[key]
        raise KeyError(
            f"metric key '{key}' not found in /health response; response is: {data}"
        )

    def validate_streaming_status(
        self,
        network_condition: str,
    ):
        """Validate that the 'network_condition' metric matches the expected condition."""

        metric_value = self.fetch_metric_values()["current_condition"]

        assert metric_value == network_condition

    def set_network_condition(self, condition: str) -> Any:
        """PUT to /control/network/<condition> to change the mock network state.
        """
        url = self._url(f"/control/network/{condition}")
        LOGGER.debug("PUT %s", url)
        # include a JSON body; many control endpoints expect structured input
        resp = self.session.put(url, timeout=self.timeout)
        if resp.status_code in (200, 204):
            self.set_session_state({"network_condition": condition})
            return resp.json()
        raise requests.HTTPError(f"Failed to set network condition: {resp.status_code} {resp.reason}")
