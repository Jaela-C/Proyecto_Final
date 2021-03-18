import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch


# create instance of elasticsearch
es = Elasticsearch()

#API
ckey = "B8fR8M4GoiypS3dyjHGXLZt43"
csecret = "6BpiXcpFQuJeTciAU0xpeZ8ej2vZaifbF8Q5i8Mv7CkJjfBofI"
atoken = "1339679861196075008-bbb6dICJ0EqpZdolHVwNGEyvMoJDBZ"
asecret = "rG87TqnxMg5HFFj3GPwWdrtd5kdu5htcKddu573o2hRJB"

class TweetStreamListener(StreamListener):

    # on success
    def on_data(self, data):

        # decode json
        dict_data = json.loads(data)

        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])

        # output sentiment polarity
        print (tweet.sentiment.polarity)

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiment
        print (sentiment)

        # add text and sentiment info to elasticsearch
        es.index(index="arauz_sentiment",
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "geo":dict_data["user"]["location"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})
        return True

    # on failure
    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # create instance of the tweepy stream
    stream = Stream(auth, listener)

    # search twitter for "Ecuador" keyword
    stream.filter(track=['ecuarauz', 'MashiRafael', 'Elecciones2021ecuador'])
    #stream.filter(locations=[-74.300986,40.449933,-73.143301,41.069886])


    
