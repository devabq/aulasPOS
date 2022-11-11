from flask import Flask, render_template
import requests

apiUrl = "https://jsonplaceholder.typicode.com/users/"

userList = requests.get(apiUrl).json()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", users=userList)