from github import Github

# Authentication is defined via github.Auth
from github import Auth

import os

# using an access token
access_token = os.getenv("GITHUB_TOKEN")
auth = Auth.Token(access_token)

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", auth=auth)

# Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)
repo_obj = g.get_repo("kuma127/python_sandbox")
print(repo_obj.name)

# To close connections after use
g.close()