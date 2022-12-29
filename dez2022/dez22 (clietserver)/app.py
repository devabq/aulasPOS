import json
from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"nome": "alice",
                    "email": "alice@outlook.com"})

@app.route("/users/<int:user_id>")
def users(user_id):
    return users_obj[user_id]

app.run()
