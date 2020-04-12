import unittest
import json
from unittest.mock import patch, create_autospec, Mock

from runes.app import app

class TestApp(unittest.TestCase):

    @patch('runes.twitter.twitter_client.TwitterClient.get_user_timeline')
    @patch('runes.twitter.twitter_auth.TwitterAuth.get_access_token')
    def test_user_tweets(self, mock_get_access_token, mock_get_user_timeline):
        with app.test_client() as client:
            test_response_json = {"text": "OK"}
            mock_get_user_timeline.return_value = test_response_json

            response = client.get('/api/v1/tweets/test_user')

            self.assertEqual(response.data.decode("utf-8"), json.dumps(test_response_json))

if __name__ == '__main__':
    unittest.main()