from tweepy import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
import time
import urllib
ckey = 'NeuryiP3oqdbfUjWpr1owot0H'
csecret = 'PxaMWoJieE9F6nAKuQu2YBYFjHzikL6AmDes9mzVcVtQCB9aV5'
atoken = '142612556-A8ushHLC7AMFZvj1TIOM5rMruOB72um9M91O895m'
asecret = 'pBITUegwYIAKHycQHYSpntlCVlZX0ArGvyXy7rPfSMjCK'

sentdexAuth = ''



def sentimentAnalysis(text):
    encoded_text = urllib.quote(text)







class listener(StreamListener):
    def on_data(self, raw_data):
        try:
            print(raw_data)

            tweet = raw_data.split(',"text":"')[1].split('","source')[0]
            print(tweet)

            saveThis = str(time.time())+'::'+tweet
            saveFile = open('twitDB2.csv','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print('Failed on data,',str(e))
            time.sleep(5)

    def on_error(self, status_code):
        print(status_code)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

