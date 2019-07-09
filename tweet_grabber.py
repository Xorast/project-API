from tweet_auth import get_auth
from tweepy import Stream
from tweet_utils import drop_collection, MyStreamListener


topic = "CyberSecurity"
keyword_list = ["cybersecurity", "infosec"]
limit = 15

auth = get_auth()

drop_collection(topic)

twitter_stream = Stream(auth, MyStreamListener(topic, limit))
twitter_stream.filter(track=keyword_list)
