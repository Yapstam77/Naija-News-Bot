import tweepy
import datetime
import requests
from bs4 import BeautifulSoup

# Twitter API credentials
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_secret = "YOUR_ACCESS_SECRET"

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

def get_top_news():
    url = "https://punchng.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    headlines = soup.select("h2.entry-title a")[:3]
    summary = "\n".join([f"- {item.text.strip()}" for item in headlines])
    
    today = datetime.date.today().strftime("%B %d, %Y")
    return f"🇳🇬 Top Nigerian News for {today}:\n\n{summary}\n\n#Nigeria #News"

def post_news():
    tweet = get_top_news()
    if len(tweet) > 280:
        tweet = tweet[:277] + "..."
    api.update_status(tweet)

if _name_ == "_main_":
    post_news()
