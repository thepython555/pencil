from flask import Flask, render_template, request
#import requests
import scratchattach as scratch3
import requests


app = Flask(__name__)

#EXISTENCE & SCRATCHRANDOM CUZ VERCEL HATES IT

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
                running = False
                return scratch3.get_project(str(idrandom))
    except Exception:
        return 0




@app.route("/")
def index():
    randomproj = getRandomProject()
    return render_template("index.html", featured_projects=scratch3.featured_projects(), recent_projects=scratch3.newest_projects(), random_projects=randomproj)

@app.route("/projects/<id>")
def project(id):
    if not check(id):
        return render_template("projecterror.html")
    saproject = scratch3.get_project(id)
    return render_template("project.html", title=saproject.title, author=saproject.author, id=saproject.id, instructions=saproject.instructions, notes=saproject.notes, comments=saproject.comments(limit=999, offset=0))

@app.route("/users/<username>")
def userpage(username):
    if not checkUser(username):
        return render_template("usererror.html")
    sauser = scratch3.get_user(username)
    return render_template("user.html", user=sauser, username=username, users_projects=sauser.projects(limit=None, offset=0), fav_projects=sauser.favorites(limit=None, offset=0), following=sauser.following(limit=999, offset=0), followers=sauser.followers(limit=999, offset=0), comments=sauser.comments(page=1, limit=999))

@app.route("/search/results")
def results():
    q = request.args.get("query")
    return render_template("results.html", results=scratch3.search_projects(query=q, mode="trending", language="en", limit=40, offset=0))

@app.route("/search")
def search():
    return render_template("search.html")
