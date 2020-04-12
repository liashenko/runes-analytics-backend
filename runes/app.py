from flask import Flask
import json

from runes.twitter.twitter_client import TwitterClient

app = Flask(__name__)

@app.route("/api/v1/tweets/<user_id>")
def user_timeline(user_id):
    twitter_client = TwitterClient()
    return json.dumps(twitter_client.get_user_timeline(user_id))