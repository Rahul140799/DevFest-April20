import os
import sys
from github import Github

username = "USERNAME"
password = "PASSWORD"

RepoName = str(sys.argv[1])
user = Github(username, password).get_user()
repo = user.create_repo(RepoName)

print("Repository '{}' create successfully".format(RepoName))