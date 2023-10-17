#This is a library that gets a random scratch project :)
#Made by dumorando, BA4X on scratch
import requests
import random

def getRandomProjects(amount):
    arr = []
    for i in range(int(amount)):
        arr.append(getRandomProject())
    return arr

def getRandomProject():
    try:
        running = True
        notfoundtext = requests.get("https://api.scratch.mit.edu/projects/7676767676767676").text
        projectcount = 908838871
        while running:
            idrandom = random.randint(0,projectcount)
            urlrandom = f"https://api.scratch.mit.edu/projects/{idrandom}"
            if requests.get(urlrandom).text != notfoundtext:
                return idrandom
    except Exception:
        return 0