"""
CRON JOB 1
"""

from tweet_utils import get_tweets

topic = "CyberSecurity"
keyword_list = ["cybersecurity", "infosec"]
limit = 15

get_tweets(topic, keyword_list, limit)