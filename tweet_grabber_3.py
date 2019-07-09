"""
CRON JOB 3
"""

from tweet_utils import get_tweets

topic = "IoT"
keyword_list = ["IoT"]
limit = 15

get_tweets(topic, keyword_list, limit)
