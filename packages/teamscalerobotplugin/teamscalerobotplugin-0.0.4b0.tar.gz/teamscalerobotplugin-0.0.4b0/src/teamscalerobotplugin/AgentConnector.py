from typing import List, Any
from urllib.parse import quote
import requests
import logging


class AgentConnector:
    """Provides functionality to interact with the agent that records the test coverage."""

    def __init__(self, url: str):
        self._url = self._sanitize_url(url)
        self._logger = logging.getLogger(__package__)

    def tia_start_test(self, test: str):
        """Notify the agent that a test is about to start."""
        self._request("test/start/" + quote(test, safe=""))

    def tia_end_test(self, test: str, result: str, message=""):
        """Notify the agent that a test has ended"""
        self._request("test/end/" + quote(test, safe=""),
                      {"result": result, "message": message})

    def tia_start_testrun(self, available_tests: List[str]):
        """Notify the agent that a test run is about to start. 
        The provided available tests will be used to select the impacted tests.
        Returns a cluster containing impacted tests."""
        self._logger.debug(
            "Available tests: %s", available_tests)
        impacted_tests = self._request("testrun/start", available_tests)
        self._logger.debug(
            "Received impacted tests: %s", impacted_tests)
        return impacted_tests

    def tia_end_testrun(self, partial: bool):
        """Notify the agent that the test run has ended."""
        path = "testrun/end"
        if partial:
            path += "?partial=true"
        self._request(path)

    def _request(self, path: str, json: Any = None):
        url = self._url + path
        self._logger.debug("Posting to %s", url)
        self._logger.debug("Request body %s", json)
        try:
            response = requests.post(url, json=json)
            if response.ok:
                self._logger.debug("Request successful")
                return response.content.decode()
            else:
                self._logger.error("Request failed: %s\n-----\n%s\n-----", str(response.status_code), response.text)
                return None
        except Exception as e:
            self._logger.error("Request failed: %s", str(e))
            return None

    def _sanitize_url(self, url: str):
        """Ensures that URLs end with '/'"""
        return url if url.endswith('/') else url + '/'
