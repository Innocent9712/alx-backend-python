#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from typing import Mapping, Sequence, Union
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for task 5 - 8"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value="example.com")
    def test_org(self, org, get_json):
        """test that GithubOrgClient.org returns the correct value."""
        orgClient = GithubOrgClient(org)
        self.assertEqual(orgClient.org, get_json.return_value)
        get_json.assert_called_once()

    def test_public_repos_url(self):
        """Implement the test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url."""

        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)\
                as mocker:
            mocker.return_value = {
                'repos_url': 'https://api.github.com/orgs/myorg/repos'
                }
            client = GithubOrgClient('myorg')
            result = client._public_repos_url
            self.assertEqual(result, 'https://api.github.com/orgs/myorg/repos')
