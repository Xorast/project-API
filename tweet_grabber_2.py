"""
CRON JOB 2
"""

from tweet_utils import get_tweets

topic = "Full_Stack"
keyword_list = ["frontend", "backend", "fullstack"]
limit = 15

get_tweets(topic, keyword_list, limit)
