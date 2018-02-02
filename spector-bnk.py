# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen

import requests
import json
import datetime
import twitter

auth = twitter.OAuth(consumer_key="YfHbXRcyQqpQSOSmDccSUrkYI",
consumer_secret="W0DBfu138fEbg21rwGB83RTPE9TP0Y7Lq5HcaER1ZzzNa4inH8",
token="956368999696154625-sn6OsA5B9V9ast1OmAOiDts5bgkTe7a",
token_secret="9hYjHVGgBZnKHtpii8JBMDJhs0kegjgCwBr3sgMxDDVwr")

#URL
URL = {'spector_bnk':'https://spectrocoin.com/scapi/ticker/JPY/BNK'}

#JsonParse
bnk_price = requests.get(URL['spector_bnk']).json()['last']
bnkp = str(bnk_price)

todaystr = str(datetime.datetime.today())

t = twitter.Twitter(auth=auth)

status = "[" + todaystr + "]" + "\n" + "現在のBankera価格は " + bnkp + "\n" + "#bnk" + "\n" + "#BANKERA" + "\n" + "#バンクエラ"
t.statuses.update(status=status)
