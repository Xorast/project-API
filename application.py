import os
import requests
from flask  import Flask, render_template


API_KEY =  os.environ.get("API_KEY")


app = Flask(__name__)

@app.route('/')
def get_index():
    
    r = requests.get('https://api.mlab.com/api/1/databases/github-tweets/collections/cybersecurity?apiKey=' + API_KEY)
    request_content     = r.json()
    request_content_1   = request_content[0]["text"]
    return render_template('index.html', req = request_content_1)
    
    
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

# ------------------------------------------------------------------------------