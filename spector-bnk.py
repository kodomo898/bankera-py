# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen

import requests
import json
import datetime
import twitter

auth = twitter.OAuth(consumer_key="**",
consumer_secret="**",
token="**",
token_secret="**")

#URL
URL = {'spector_bnk':'https://spectrocoin.com/scapi/ticker/JPY/BNK'}

#JsonParse
bnk_price = requests.get(URL['spector_bnk']).json()['last']
bnkp = str(bnk_price)

todaystr = str(datetime.datetime.today())

t = twitter.Twitter(auth=auth)

status = "[" + todaystr + "]" + "\n" + "現在のBankera価格は " + bnkp + "\n" + "#bnk" + "\n" + "#BANKERA" + "\n" + "#バンクエラ"
t.statuses.update(status=status)
