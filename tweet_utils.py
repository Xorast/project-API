import os
import json
from tweepy.streaming import StreamListener
from pymongo import MongoClient


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
