# reddit-api-task
This script prints provided amount of latest posts from subreddit in JSON format

## How to set up and run the project

Clone the repository
```
git clone git@github.com:alya783/reddit-api-task.git
```
Navigate to project directory:
```
cd reddit-api-task
```
Install dependences:
```
poetry install --no-root
```
Fill in credentials in praw.ini file
```
client_id=YOUR_ID
client_secret=YOUR_SECRET
redirect_uri=YOUR_URI
user_agent=YOUR_USER_AGENT
```
Run script:
```
poetry run ./reddit-api.py
```

## Output example

```
[
    {
        "title": "New Earth Has Been Discovered Near Us: The Planet May Be Habitable",
        "author": "skorupak",
        "score": 1575
    },
    {
        "title": "Cosmos: A Spacetime Odyssey is now on Netflix! (U.S)",
        "author": "Pillippatty",
        "score": 623
    },
    {
        "title": "Seth MacFarlane just tweeted this. Peter deGrasse Tyson. That is all.",
        "author": "palakkadan",
        "score": 533
    },
    {
        "title": "Throwback Neil with killer biceps and sideburns.",
        "author": "SamuelStephenBono",
        "score": 447
    },
    {
        "title": "Every Sunday",
        "author": "tomato_sauce",
        "score": 449
    }
]
```


