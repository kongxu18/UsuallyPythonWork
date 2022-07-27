import time

import requests
import json
import re

header = {
    # "Accept": "*/*",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cache-Control": "max-age=0",
    # "Connection": "keep-alive",
    # "Content-Length": "119",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "language=zh; WebSession=11fdea39b6f9df2ae337",
    # "Host": "192.168.4.2",
    "If-Modified-Since": "0",
    # "Origin": "http://192.168.4.2",
    # "Referer": "http://192.168.4.2/doc/page/playback.asp",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    # "X-Requested-With": "XMLHttpRequest",
}

xml = r'<?xml version="1.0" encoding="utf-8"?><trackDailyParam><year>%d</year><monthOfYear>%d</monthOfYear></trackDailyParam>'

req = requests.post("http://192.168.4.2/ISAPI/ContentMgmt/record/tracks/1901/dailyDistribution", headers=header,data=xml)
print(req.text)

all = {}
# print(res)


with open('监控2', 'w+') as f:
    for y in range(1977, 2023):
        for m in range(1, 13):
            print(y, m)
            payload = xml % (y, m)
            req = requests.post("http://192.168.4.2/ISAPI/ContentMgmt/record/tracks/1901/dailyDistribution",
                                headers=header, data=payload)
            text = req.text
            res = re.findall('.*dayOfMonth>(\d+)<.*\n.*record>(true)<', text)


            info = {(y,m): res}
            f.write(str(info)+'\n')

# print(all)
