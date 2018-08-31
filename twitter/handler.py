import tweepy
import os

def handle(req):
    auth = tweepy.OAuthHandler(os.environ["consumer_key"], os.environ["consumer_secret"])
    auth.set_access_token(os.environ["access_token"], os.environ["access_token_secret"])

    api = tweepy.API(auth)

    content = req
    print("Tweet content: "+content)

    api.update_status(content)

    # Log the results
    print("Tweet sent")
