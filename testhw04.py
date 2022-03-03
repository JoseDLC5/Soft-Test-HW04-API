import unittest
from unittest import mock
from unittest.mock import MagicMock
from unittest.mock import patch
import requests
import json

from hw04 import getRepoCommits, getRepoNames, repoCommits


class FakeResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


switcher = {"https://api.github.com/users/josedlc5/repos": "json/josedlc5_repos.json",
            "https://api.github.com/repos/josedlc5/All-Pairs-Shortest-Paths-Weighted/commits": "json/all_pairs.json",
            "https://api.github.com/repos/josedlc5/AJAX-API-Show-Search/commits": "json/ajax_api.json",
            "https://api.github.com/repos/josedlc5/Anagram-Detector/commits": "json/anagram.json"}


def mocked_requests_get(*args):
    if args[0] in switcher:
        with open(switcher[args[0]]) as f:
            return FakeResponse(json.load(f))
    return FakeResponse(None)


class testRepoCommits(unittest.TestCase):
    # @mock.patch('requests.get', side_effect=mocked_requests_get)
    # def testGetRepoCommits(self, mock_get):
    #     self.assertEqual(
    #         type(getRepoCommits("josedlc5", "Anagram-Detector")), dict)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def testGetRepoNames(self, mock_get):
        self.assertEqual(getRepoNames("josedlc5"), [
                         'AJAX-API-Show-Search', 'All-Pairs-Shortest-Paths-Weighted', 'Anagram-Detector'])

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def testRepoCommits(self, mock_get):
        self.assertEqual(getRepoCommits("josedlc5", [
                         'AJAX-API-Show-Search', 'All-Pairs-Shortest-Paths-Weighted', 'Anagram-Detector']), {
                         'AJAX-API-Show-Search': 2, 'All-Pairs-Shortest-Paths-Weighted': 3, 'Anagram-Detector': 2})

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def testRepoDict(self, mock_get):
        self.assertEqual(repoCommits("josedlc5"), {
                         'AJAX-API-Show-Search': 2, 'All-Pairs-Shortest-Paths-Weighted': 3, 'Anagram-Detector': 2})


if __name__ == '__main__':
    unittest.main()
