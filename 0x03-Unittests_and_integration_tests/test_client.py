#!/usr/bin/env python3
"""Unittests and integration tests module
"""
import unittest
from unittest.mock import patch

from parameterized import parameterized
client = __import__("client")


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json):
        """test_org method
        """
        my_client = client.GithubOrgClient(org)
        my_client.org()
        my_client.org()

        mock_get_json.assert_called_once()
