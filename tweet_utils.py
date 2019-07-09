import os
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from pymongo import MongoClient
from tweet_auth import get_auth


MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")


def drop_collection(topic):

    try:
        with MongoClient(MONGODB_URI) as conn:
            db = conn[MONGODB_NAME]
            coll = db[topic]
            coll.drop()
        print("Collection dropped")

    except BaseException as e:
        print("Failed dropping: %s" % str(e))


class MyStreamListener(StreamListener):

    def __init__(self, topic, limit):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.topic = topic
        self.limit = limit

    def on_data(self, data):

        if self.num_tweets < self.limit:

            self.num_tweets += 1

            try:
                with MongoClient(MONGODB_URI) as conn:
                    db = conn[MONGODB_NAME]
                    coll = db[self.topic]
                    coll.insert(json.loads(data))
                print("Tweet " + str(self.num_tweets) + "/" + str(self.limit))
                return True
            except BaseException as e:
                print("Failed on_data: %s" % str(e))

            return True

        else:

            return False

    @staticmethod
    def on_error(status):
        print(status)
        return True


def get_tweets(topic, keyword_list, limit):

    auth = get_auth()
    drop_collection(topic)
    twitter_stream = Stream(auth, MyStreamListener(topic, limit))
    twitter_stream.filter(track=keyword_list)
