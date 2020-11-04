import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = "C:\Users\Tony Stark\AppData\Local\Google\Chrome SxS\Application\chrome.exe"
browser = webdriver.Chrome(chrome_options=chrome_options)

url = u'https://twitter.com/SatoshiLite/'
browser.get(url)
#time.sleep(5)
body = browser.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)

twitname = []
twittime = []
twittweet = []
names = browser.find_elements_by_css_selector("strong.fullname.show-popup-with-id.u-textTruncate")
times = browser.find_elements_by_css_selector("span._timestamp.js-short-timestamp")
tweets = browser.find_elements_by_css_selector(".TweetTextSize.TweetTextSize--normal.js-tweet-text.tweet-text")

#for p,g,k in zip(names, times, tweets):
    #print (p.text),(g.text),(k.text)

for p,g,k in zip(names, times, tweets):
    twitname.append(p.text)
    twittime.append(g.text)
    twittweet.append(k.text)

df = pd.DataFrame(np.column_stack([twitname, twittime, twittweet]), columns = ['Name','Time','Tweet'])
print df

browser.close()
