# Runes: Social Media Analytics Backend   [![CircleCI](https://circleci.com/gh/liashenko/runes-analytics-backend.svg?style=shield)](https://circleci.com/gh/liashenko/runes-analytics-backend)

Backend layer for [Runes: Social Media Analytics](https://github.com/liashenko/runes-analytics). Aggregate and visualize your data from social media in one place.

## API
* `/api/v1/tweets/<user_id>` - Get user tweets by twitter username.  
Reference: https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline

## Local development
#### Prerequisites
Python3

#### Setup Python virtual environment
1. Create the virtual environment: `python3 -m venv venv`
2. Activate this environment: `source venv/bin/activate`

#### Add .env file to the root directory
```
export TWITTER_KEY="XXX"
export TWITTER_SECRET="XXX"
export FLASK_ENV=development
```

#### Running the server
1. `pip install -r requirements.txt`
2. `FLASK_APP=runes.app.py flask run`

#### Running the tests
* `python -m unittest`

## Built With
1. [Python3](https://www.python.org/download/releases/3.0/)
2. [Flask](https://github.com/pallets/flask)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
