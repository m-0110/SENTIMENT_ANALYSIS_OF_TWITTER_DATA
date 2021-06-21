from textblob import TextBlob
import tweepy
from matplotlib import pyplot as plt
from oauth import *
from dataprocess import *
#finding percentage score
def percentage_score_sentiment(part,whole):
    return '%.2f'%(100*(part/whole))

#Finding sentiment
try:
    #getting credentials
    credentials=oauthorization()
    consumer_key=credentials["consumer_key"]
    consumer_secret=credentials["consumer_secret"]
    access_token=credentials["token_key"]
    access_token_secret=credentials["token_secret"]

    #establish connection with tweepy
    auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    #creating API object
    api=tweepy.API(auth)

    # getting the search_word and count
    search_word1=input("enter keyword/hashtag for which sentiment to be found : ")
    #filtering retweets
    search_word=search_word1+" -filter:retweets"
    noOfTweets=int(input("enter number of tweets to be analyzed:"))
    #getting iterator object containing tweets
    tweets = tweepy.Cursor(api.search,q = search_word,lang='en').items(noOfTweets)

    positive=0
    negative=0
    neutral=0

    #iterating through tweets
    for tweet in tweets:
        # get the text of tweets and perform data cleaning and pass it to TextBlob
        analyze=TextBlob(clean_tweets(tweet.text))
        polarity=analyze.sentiment.polarity
        # finding sentiment of each tweet whether it is positive , negative ,neutral
        if(polarity>0):
            positive+=1
        elif(polarity<0):
            negative+=1
        elif(polarity==0):
            neutral+=1
    positive=percentage_score_sentiment(positive,noOfTweets)
    negative = percentage_score_sentiment(negative,noOfTweets)
    neutral = percentage_score_sentiment(neutral,noOfTweets)
    print('The sentiment about {} on analyzing {} tweets is '.format(search_word1,noOfTweets))

    if(positive>negative):
        print('positive')
    elif(positive<negative):
        print('negative')
    elif(positive==negative):
        print('neutral')
    #plotting piechart
    plt.pie([positive,negative,neutral],
            colors=['green', 'red','orange'], startangle=90,autopct='%.2f')

    plt.legend(labels=['positive: '+str(positive)+'%','negative: '+str( negative)+'%','neutral: '+str(neutral)+'%' ],loc='lower left')
    plt.title("TWITTER SENTIMENT ANALYSIS about\n'{}' by analyzing {} tweets".format(search_word1,noOfTweets))
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


except Exception as e:
    print("error",str(e))







