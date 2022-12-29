from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
    user_id = '2'
    apiUrl = f"http://localhost:5000/users/2"
    response = requests.get(apiUrl)
    return "funciona"
