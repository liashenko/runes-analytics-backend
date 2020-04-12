import requests
import json

from runes.twitter.twitter_auth import TwitterAuth

TWITTER_USER_TIMELINE_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

class TwitterClient(object):
    def __init__(self):
        self.oauth_token = TwitterAuth.get_access_token()

    def get_user_timeline(self, user_id):
        response = requests.get(TWITTER_USER_TIMELINE_URL, 
            headers={
                'Authorization': 'Bearer {}'.format(self.oauth_token)
            },
            params={
                'screen_name': user_id, 
                'include_rts': 'false', 
                'exclude_replies': 'true',
                'trim_user': 'false'
            })
        return response.json()