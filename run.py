# /bin/env python3
# coding=utf-8

import requests
import json

get_list_url = 'https://used-api.jd.com/auction/list?pageNo=1&pageSize=50&category1=&status=&orderDirection=1&auctionType=1&orderType=1&callback=__jp0'
r = requests.get(get_list_url)
r_data = r.text.lstrip('/**/__jp0(').rstrip(');')
json_data = json.loads(r_data)
print(json_data)
totalNumber = json_data['data']['totalNumber']
auctionInfos = json_data['data']['auctionInfos']
for auctionInfo in auctionInfos:
    print(auctionInfo)
