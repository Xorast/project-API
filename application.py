import  os
import  json
import  requests
from    flask       import Flask, render_template


API_KEY_1   = os.environ.get("API_KEY_1")
API_NAME_1  = os.environ.get("API_NAME_1")

API_KEY_2   = os.environ.get("API_KEY_2")
API_NAME_2  = os.environ.get("API_NAME_2")

app = Flask(__name__)

@app.route('/')
def get_index():
    
    # --------------------------
    url     = (API_NAME_2 + API_KEY_2)
    
    r2       = requests.get(url)
    r2       = r2.json()
    
    articles = r2["articles"]
    print(r2["totalResults"])
    
    # --------------------------
    
    # --------------------------
    r1              = requests.get(API_NAME_1 + API_KEY_1)
    request_content = r1.json()
    
    tweets_array = []
    
    for tweet in request_content :
        tweets_array.append({   "text"          : tweet['text'], 
                                "likes"         : tweet['user']['favourites_count'],
                                "username"      : tweet['user']['name'],
                                "retweet_count" : tweet['retweet_count'],
                                "reply_count"   : tweet['reply_count'],
                                "retweeted"     : tweet['retweeted_status']['created_at'] if "retweeted_status" in tweet else "NO"
                            })
                
    # -------------------------
    
    return render_template('index.html', tweets = tweets_array, articles = articles)
    
    
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

# ------------------------------------------------------------------------------