from flask import Flask, render_template, request
#import requests
import scratchattach as scratch3
import scratchrandom
import existence

app = Flask(__name__)

def getRandomProjects():
    arr = []
    for item in scratchrandom.getRandomProjects(1):
        arr.append(scratch3.get_project(item))
    return arr

@app.route("/")
def index():
    return render_template("index.html", featured_projects=scratch3.featured_projects(), recent_projects=scratch3.newest_projects(), random_projects=getRandomProjects())

@app.route("/projects/<id>")
def project(id):
    if not existence.check(id):
        return render_template("projecterror.html")
    saproject = scratch3.get_project(id)
    return render_template("project.html", title=saproject.title, author=saproject.author, id=saproject.id, instructions=saproject.instructions, notes=saproject.notes, comments=saproject.comments(limit=999, offset=0))

@app.route("/users/<username>")
def userpage(username):
    if not existence.checkUser(username):
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