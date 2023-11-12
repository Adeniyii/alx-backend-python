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
        my_client.org
        my_client.org

        mock_get_json.assert_called_once()

    @parameterized.expand([
        ("google", True),
        ("abc", False)
    ])
    def test_public_repos_url(self, org: str, expected: bool):
        """"""
        my_client = client.GithubOrgClient(org)
        with patch(my_client, "org") as mock_org:
            mock_org.return_value = {"repos_url": expected}
            self.assertEqual(my_client._public_repos_url, expected)
            mock_org.assert_called_once()
