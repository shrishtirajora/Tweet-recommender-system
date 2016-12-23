from sip import setapi
setapi("QDate", 2)
setapi("QDateTime", 2)
setapi("QTextStream", 2)
setapi("QTime", 2)
setapi("QVariant", 2)
setapi("QString", 2)
setapi("QUrl", 2)
import os
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


#change the directory
directory = '/home/shubhi/IR/IRdata1'
attribute_list = ["tweet_text", "user_name", "verified_user", "followers", "retweet_count", "hashtags", "tweet_id"]
count = 0
for filename in os.listdir(directory):
	filepath = directory + '/' + str(filename)
	#print(str(filepath))
	f = open(filepath, "r")
	data = f.read()
	delim = "}"
	data = data.split(delim)
	for tweet in data:
		#tweet_count = tweet_count + 1
		dict_item = str(tweet) + delim
		
		#count = count + 1
		try:
			json_item = json.loads(dict_item)
		except Exception as e1:
			#print e1
			#print dict_item
			#try_count = try_count+1
			#print("json error")
			#json_error+=1
			index = dict_item.find("description")
			dict_item = dict_item[0:index] + ',' + dict_item[index:]
			try:
				json_item = json.loads(dict_item)
			except:
				#print "another json_error"
				#print dict_item
				continue
		#write_count = write_count+1
		try:
			count+=1
			'''
			for attr in attribute_list:
				#print("for")
				attrfile = attr + ".txt"
				f = open(attrfile, "a+")
				#print(attr, " ", json_item[attr])
				
				f.write(str(json_item[attr]) + "\n")
			'''
			attrfile1 = 'hashtags' + ".txt"
			attrfile2 = 'tweet_text' + ".txt"
			f1 = open(attrfile1, "a+")
			f2 = open(attrfile2, "a+")
			tweet_text = str(json_item["tweet_text"]).strip('\n')
			tweet_text = tweet_text.replace("\n", " ")
			f2.write( tweet_text+ "\n")
			f1.write( str(json_item["hashtags"])+ "\n")
		except Exception as e:
			print(e)
			print("writeerror")
	f.close()
print(count)