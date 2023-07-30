#!/usr/bin/env python3
"""Test for githuborgclient class methods"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
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
