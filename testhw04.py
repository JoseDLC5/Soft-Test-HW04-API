import unittest

from hw04 import *


class testRepoCommits(unittest.TestCase):

    def testGetRepoCommits(self):
        self.assertEqual(
            type(getRepoCommits("josedlc5", "Python-Pig-Game")), dict)

    def testGetRepoNames(self):
        self.assertEqual(type(getRepoNames("josedlc5")), list)

    def testRepoDict(self):
        self.asserEqual(type(repoCommits("josedlc5")), dict)


if __name__ == '__main__':
    unittest.main()
