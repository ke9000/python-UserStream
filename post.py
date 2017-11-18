#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Initialize
import sys
sys.path.append("PASS")
from requests_oauthlib import OAuth1Session
import random
import API

#Random_Num
x = random.randint(1,100)
print (x)

#Tweet_Post
url = "https://api.twitter.com/1.1/statuses/update.json" #post_URL

params = {"status":"test"+str(x)}  

twitter = OAuth1Session(API.CK, API.CS, API.AT, API.AS)
req = twitter.post(url, params = params)

if req.status_code == 200:
    print ("OK")
else:
	print ("Error: %d" % req.status_code)
