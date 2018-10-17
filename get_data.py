import  os
import  json
import  requests


def get_news(API_NAME_2, API_KEY_2):

    response  = requests.get(API_NAME_2 + API_KEY_2)
    response  = response.json()
    
    # print(response["totalResults"])
    
    return  response["articles"]
    
def get_tweets(API_NAME_1, API_KEY_1):
    
    response            = requests.get(API_NAME_1 + API_KEY_1)
    request_content     = response.json()
    
    tweets_array = []
    
    for tweet in request_content :
        tweets_array.append({   "id"            : tweet['id'],
                                "text"          : tweet['text'], 
                                "likes"         : tweet['user']['favourites_count'],
                                "username"      : tweet['user']['name'],
                                "retweet_count" : tweet['retweet_count'],
                                "reply_count"   : tweet['reply_count'],
                                "retweeted"     : tweet['retweeted_status']['created_at'] if "retweeted_status" in tweet else "NO"
                            })

    return tweets_array