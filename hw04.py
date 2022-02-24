# https://api.github.com/users/<ID>/repos

import requests
import json


def getRepoNames(id):

    url = f"https://api.github.com/users/{id}/repos"

    # get json data for list of all user repos and their data
    jsonRepoList = requests.get(url)

    # get list of all user repos and their data
    repoList = jsonRepoList.json()

    repoNameList = []

    for repo in repoList:
        repoNameList.append(repo["name"])

    return repoNameList


def getRepoCommits(id, repoNameList):

    repoCommitDict = {}

    for repoName in repoNameList:
        jsonRepoCommits = requests.get(
            f"https://api.github.com/repos/{id}/{repoName}/commits")
        repoCommits = jsonRepoCommits.json()
        print(repoCommits)
        commitNum = len(repoCommits)
        repoCommitDict[repoName] = commitNum

    return repoCommitDict


def repoCommits(id):
    repoNameList = getRepoNames(id)
    repoDict = getRepoCommits(id, repoNameList)
    for repoName in repoDict:
        print(f"Repo: {repoName} Number of commits: {repoDict[repoName]}")
    return repoDict


repoCommits("josedlc5")
