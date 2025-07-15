import tweepy
import datetime
import requests
from bs4 import BeautifulSoup

# Twitter API credentials from GitHub secrets
import os
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

def get_punch_news():
    url = "https://punchng.com/"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    links = soup.select("h2.entry-title a")[:3]
    return [f"📰 Punch: {link.text.strip()}" for link in links]

def get_vanguard_news():
    url = "https://www.vanguardngr.com/"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    items = soup.select("h3.post-title a")[:3]
    return [f"📰 Vanguard: {item.text.strip()}" for item in items]

def get_channels_news():
    url = "https://www.channelstv.com/"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    headlines = soup.select("h2.post-title a")[:3]
    return [f"📺 Channels: {headline.text.strip()}" for headline in headlines]

def get_combined_news():
    today = datetime.date.today().strftime("%B %d, %Y")
    all_news = get_punch_news() + get_vanguard_news() + get_channels_news()
    tweet = f"🇳🇬 Top Nigerian News for {today}:\n\n"
    
    for line in all_news:
        if len(tweet) + len(line) + 2 > 280:
            break
        tweet += f"{line}\n"

    return tweet.strip()

def post_news():
    tweet = get_combined_news()
    api.update_status(tweet)
    print("✅ Tweeted:\n", tweet)

if _name_ == "_main_":
    post_news()
