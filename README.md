### Runes: Social Media Analytics Backend

### API
* `/api/v1/tweets/<user_id>` - Get user tweets by twitter username.  
Reference: https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline

### Build
#### Prerequisites
Python3

#### Setup Python virtual environment
1. Create the virtual environment:
`python3 -m venv venv`
2. Activate this environment:
`source venv/bin/activate`
2. To deactivate the environment:
`deactivate`

#### Running the app
1. `pip install -r requirements.txt`
2. `FLASK_APP=runes.app.py flask run`

### Test
`python -m unittest`
