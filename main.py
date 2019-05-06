# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Author: weikun
# Created Time: Thu 07 Mar 2019 06:02:47 PM CST

import os
import Mgr
import Log
import UrlDownLoad
import DirDownLoad
from xml.dom.minidom import parse, parseString
from bs4 import BeautifulSoup
import threadpool


class UrlParse(object):
    def __init__(self):
        pass

    def parse(self, url):
        dirName = 'DowdDir/%s' % (dirName, )
        if not os.path.exists(dirName):
            os.makedirs(dirName)

        maxIndex = 1
        UUID = 1

        def urlIter():
            index = 1
            while True and index <= maxIndex:
                imgUrl = urlTmp % (index, )
                fileName = '%03d.jpg' % (index, )
                index += 1
                yield imgUrl, fileName
        return dirName, UUID, urlIter


Mgr.UrlParse = UrlParse()

if __name__ == '__main__':
    import urllib.request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    url = ''
    req = urllib.request.Request(url, headers=headers)
    r = urllib.request.urlopen(req)
    html = r.read().decode('utf-8')
    print(html)
    soup = BeautifulSoup(html)
    title = soup.title
    print (soup.title)

    # ULRS = (
    # 		'',
    # 		'',
    # 		'',
    # 		)

    # ULRS = (url for url in ULRS if url)
    # Mgr.DBEntity = DBBase.DBBase()
    # pool = threadpool.ThreadPool(3)

    # def downloads(url):
    # 	quest = Mgr.DirDownLoad(url)
    # 	quest.DownloadQuest()

    # requests = threadpool.makeRequests(downloads, ULRS)
    # [pool.putRequest(req) for req in requests]
    # pool.poll()
