from flask import Flask
from flask_cors import CORS
import json

from runes.twitter.twitter_client import TwitterClient

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/tweets/<user_id>")
def user_timeline(user_id):
    twitter_client = TwitterClient()
    return json.dumps(twitter_client.get_user_timeline(user_id))