#!/usr/bin/env python3
"""Test for githuborgclient class methods"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """class inheriting unittest for githuborg class"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, test_orgname, mock_getjson):
        """tests get_json for org details"""
        url = "https://api.github.com/orgs/{}".format(test_orgname)
        example = GithubOrgClient(test_orgname)
        example.org()
        mock_getjson.assert_called_once_with(url)

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google"})
     ])
    def test_public_repos_url(self, test_org, response):
        """test with the property get mock method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as tester:
            tester.return_value = response
            example = GithubOrgClient(test_org)._public_repos_url
            self.assertEqual(example, response.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, mocked_getjson):
        """return a few dict for getjson"""
        payload = [{"name": "Thirsty"}, {"name": "Hungry"}]
        mocked_getjson.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as testit:
            testit.return_value = "https://api.github.com/orgs/google"
            example = GithubOrgClient('test').public_repos()
            self.assertEqual(example, ["Thirsty", "Hungry"])
            testit.assert_called_once()
            mocked_getjson.assert_called_once()
