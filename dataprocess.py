
import regex as re
import string

def clean_tweets(tweet):
    #remove url links
    tweet=re.sub(r"http\S+|www\S+|https\S+", "", tweet, flags=re.MULTILINE)
    #Remove user @ references and '#' from tweet
    tweet = re.sub(r"\@\w+|\#", "", tweet)
    '''Remove RT from retweet
    tweet=re.sub(r'RT[\s]+','',tweet) #remove RT
    '''
    #remove punctuation
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))
    return tweet
