#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Initialize
import sys
sys.path.append("D:\Python\Twitter-API\Lib")
reload(sys)
sys.setdefaultencoding('utf-8') # デフォルトの文字コードを変更する．
import requests
from requests_oauthlib import OAuth1Session
import datetime, time
import json
import API

# デフォルトの文字コードを出力する．
print 'defaultencoding:', sys.getdefaultencoding()

#UserStream
twitter = OAuth1Session(API.CK, API.CS, API.AT, API.AS)
url = "https://userstream.twitter.com/1.1/user.json"

params = {}
RLT =  180 #Rate-Limit time (min)

while(True):
	try:
		req  = twitter.post(url, stream=True, params = params)

		#Return
		print(req.status_code)

		if req.status_code == 200:
			if req.encoding is None:
				req.encoding = "utf-8"
		
		
			for js in req.iter_lines(chunk_size=1,decode_unicode=True):
				try:
					if js :
				
						tweet = json.loads(js)
				
						if tweet.has_key("text"):
							#jsonのkeyをそれぞれ変数化
							Name = (tweet["user"]["name"])
							SC_N = (tweet["user"]["screen_name"])
							Text = (tweet["text"])
		
							#print
							print (Name+"(@"+SC_N+"):"+'\n'+Text)
							continue
				
						else:
							continue
					
				except UnicodeEncodeError:
					pass	
					
		elif req.status_code == 420:
				print('Rate Limit: Reload after', RLT, 'Sec.')
				time.sleep(RLT)
			
		else:
			print("HTTP ERRORE: %d" % req.status_code)
			break
	
	#取得が少ない場合decodeできる物が無いと怒る
	#except json.JSONDecodeError as e:
		#print("Re-try")
		#pass
	#except UnicodeEncodeError:
		#pass
	
		
	except KeyboardInterrupt:
		print("End")
		break
		
	except:
		print("except Error:", sys.exc_info())
		pass