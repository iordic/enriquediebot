import os
import tweepy
import pickle
from generator import Generator
from constants import BIN_FILE, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def tweet_text(text):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(text)

if __name__ == '__main__':
    if os.path.isfile(BIN_FILE):
        with open(BIN_FILE, 'rb') as f:
            g = pickle.load(f)
    else:
        g = Generator()
    tweet_text(g.get_phrase())
