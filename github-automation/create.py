import os
import sys
from github import Github

with open('github-automation/credentials.txt','r') as f:
    creds = f.readlines()

username = creds[0].strip()
password = creds[1].strip()

RepoName = str(sys.argv[1])
user = Github(username, password).get_user()
repo = user.create_repo(RepoName)

print("Repository '{}' create successfully".format(RepoName))