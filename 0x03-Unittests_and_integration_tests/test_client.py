#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
"""
 4. Parameterize and patch as decorators
 5. Mocking a property
 6. More patching
 7. Parameterize
 8. Integration test: fixtures
"""

class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        string = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(string)


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the expected value."""
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/google/repos"}

        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/google/repos")


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=property)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that public_repos returns the expected list."""
        string = "https://api.github.com/orgs/google/repos"
        mock_public_repos_url.return_value = string
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        string = "https://api.github.com/orgs/google/repos"
        mock_get_json.assert_called_once_with(string)


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for the GithubOrgClient
    class.
    """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the correct boolean."""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


# Fixtures for parameterized class decorator
@parameterized_class([
    {"org_payload":
     {"login": "google"},
     "repos_payload":
     [{"name": "repo1"},
      {"name": "repo2"}],
     "expected_repos": ["repo1", "repo2"], "apache2_repos": []}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up mock for requests.get."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Side effect to mock .json() responses
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop mock for requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method with integration."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos, self.expected_repos)
