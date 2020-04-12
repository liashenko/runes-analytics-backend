from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
import os

TWITTER_TOKEN_URL = 'https://api.twitter.com/oauth2/token'

TWITTER_KEY = os.environ.get("TWITTER_KEY")
TWITTER_SECRET = os.environ.get("TWITTER_SECRET")

class TwitterAuth():

    @staticmethod
    def get_access_token():
        auth = HTTPBasicAuth(TWITTER_KEY, TWITTER_SECRET)
        client = BackendApplicationClient(client_id=TWITTER_KEY)
        oauth = OAuth2Session(client=client)
        token_response = oauth.fetch_token(token_url=TWITTER_TOKEN_URL, auth=auth)
        return token_response["access_token"]