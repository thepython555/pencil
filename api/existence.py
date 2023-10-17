"""
Checks the
EXISTENCE
of a scratch project
    - BA4X
"""

import requests

def check(id):
    try:
        notfoundtext = requests.get("https://api.scratch.mit.edu/projects/7676767676767676").text
        thistext = requests.get(f"https://api.scratch.mit.edu/projects/{str(id)}").text
        if thistext == notfoundtext:
            return False
        else:
            return True
    except Exception:
        return False

def checkUser(username):
    notfoundtext = requests.get("https://api.scratch.mit.edu/users/aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/").text
    thistext = requests.get(f"https://api.scratch.mit.edu/users/{username}").text
    if thistext == notfoundtext:
        return False
    else:
        return True