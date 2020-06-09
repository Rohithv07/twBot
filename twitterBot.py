import  tweepy

#1.Authenticate
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret_key')  
# Here we provided consumer key and consumer secret key of our developer.twitter.com

#2.Access the token
auth.set_access_token('access_token', 'access_token_secret')

#3.Using tweepy.API
api = tweepy.API(auth)

public_tweets = api.home_timeline() #Getting the timeline
for tweet in public_tweets:
    print(tweet.text)

user = api.me()
print("User name:", user.name)
print("Name on screen:", user.screen_name)
print("No of followers:", user.followers_count)

def limit_handler(cursor):
    try:
       while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

#Follow back my followers
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Rohit K':
        follower.follow()
        print("Followed back")
        break

# Auto liker

search_item = 'python'
no_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_item).items(no_of_tweets):
    try:
        tweet.favorite()
        tweet.retweet()
        print("Liked and retweeted")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break