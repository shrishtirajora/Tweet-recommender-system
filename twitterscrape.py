import json
import tweepy

ACCESS_TOKEN = '787303334432546816-CSGMfXAIdR16F6BfpluMMv1nz5jRFx9'
ACCESS_SECRET = 'FMO8opQsA1mY3eDAh45SmvmkkB0nbLlrdCtcicVq1vm3g'
CONSUMER_KEY = 'aVUriqyFNEQDBgusciSJ3s3WD'
CONSUMER_SECRET = 'WWjTB1MDYIPKMtJsP0X4dRBqW5I7T9iRGgKJDzAay23yAvNglc'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

#initiate the connection to the Twitter REST API

hashtags = ["#akhilesh", "#android", "#obamacare", "#brics", "#closer"]

for ht in hashtags:
	f = open(str(ht)+".txt","w+")
	for tweet in tweepy.Cursor(api.search, q=str(ht)).items(100):
			
			
			d = {	}
			d["tweet_id"] = tweet.id
			d["tweet_text"] = tweet.text
			hashtags_list = tweet.entities['hashtags']
			l = len(hashtags_list)
			temp_list = []
			for i in range(l):
				temp_list.append(hashtags_list[i]['text'])
			d["hashtags"] = temp_list
			d["retweet_count"] = tweet.retweet_count
			d["user_name"] = tweet.user.name
			d["followers"] = tweet.user.followers_count
			d["verified_user"] = tweet.user.verified
			d["description"] = tweet.user.description

			json.dump(d, f, ensure_ascii=False)
		