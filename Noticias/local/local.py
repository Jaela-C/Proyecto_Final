
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = ""
csecret = "bC5GgQ0SIwvNSd3fhNHxQqXU2HUe79yVooaKkIgkMXvtTbrOR5"
atoken = "913124280258453504-66pWzJfevXzbdri95FCn9TTsNO1Oqij"
asecret = "yGvRBH5QMtrOvmH3g3bDQspMzvrR3GnCJ8vxqIqVrG4pk"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('noticiasecu')
except:
    db = server['noticiasecu']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[-78.619545,-0.365889,-78.441315,-0.047208])  
twitterStream.filter(track=['teleamazonasec','ecuavisa','Gamavisionecu','tctelevision','TVCEcuador'])
