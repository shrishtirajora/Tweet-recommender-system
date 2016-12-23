from __future__ import unicode_literals
from google import  search_news
# import newspaper
import urllib
from bs4 import BeautifulSoup
# data = ""
text_f = open("/home/suryansh/Desktop/debatenight", "w")
for url in search_news("debate night", stop=30):
    # print url
    # url = "http://www.hindustantimes.com/analysis/us-understands-india-s-anger-but-does-not-explicitly-back-surgical-strikes/story-VOow8dR7nRenaY6OryVjoL.html"
    
    if url[0:21] == "http://www.bbc.co.uk/":
        continue
    print "** " + url + "\n\n"
    if(url == "http://www.hamhigh.co.uk/news/hampstead_schoolgirls_hold_yoga_day_for_indian_village_1_4763832" or url == "https://www.rt.com/sport/365009-rio-worker-wages-threaten-suit/" or url == "http://www.bbc.co.uk/news/uk-england-manchester-37631537" or url == "http://www.bbc.co.uk/newsround/37675611"):
        continue
    # if( url == "https://www.bloomberg.com/view/articles/2016-11-08/india-pushes-u-k-to-figure-out-its-economic-future"):
        # continue
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,from_encoding="utf-8")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = ' '.join(chunk for chunk in chunks if chunk)
    # data += "url = "+ url + "\n\n" + text
    # text_f.write("url = "+ url + "\n\n" + text)
    print (text + "\n\n")