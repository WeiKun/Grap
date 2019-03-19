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
import bs4
import urllib
import threadpool

class UrlParse(object):
	def __init__(self):
		pass

	def parse(self, url):
		url = url.replace('/s/', '/s/')
		string = Mgr.UrlDownLoad.downStr(url)
		if not string:
			return None, None, None
		try:
			soup = BeautifulSoup(string, 'html.parser', from_encoding = 'utf-8')
		except:
			print 'Err', url
			return None, None, None
		
		node = soup.find('title')
		dirName = node.get_text()
		if '翻訳' in dirName:
			dirName = dirName[:dirName.find('翻訳')]
			dirName = dirName[:dirName.rfind('[')]
		elif '汉化' in dirName:
			dirName = dirName[:dirName.find('汉化')]
			dirName = dirName[:dirName.rfind('[')]
		dirName = dirName.strip(' ')
		dirName = dirName.replace(' ', '_')
		
		maxIndex = 0
		nodes = soup.find_all('th')
		for node in nodes:
			if (node.get_text() == '日付'):
				maxIndex = int(node.parent.find_all('td')[-1].get_text())
		
		node = soup.find('img')
		urlTmp = urllib.unquote(node['src'])
		urlTmp = urlTmp[urlTmp.find('/i/s/') + len('/i/s/'):]
		urlTmp = urlTmp.replace('1.jpg', '%d.jpg')
		urlTmp = 'https://%s' % (urlTmp, )
		urlTmp = urlTmp.replace('pic11', 'c3')
	
		dirName = u'Y:/BT_UT/NewHomic/%s' % (dirName, )
		if not os.path.exists(dirName):
			os.makedirs(dirName)
			
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
	import DBBase
	Mgr.ProjectName = 'Test'
	
	ULRS = (
			'',
			'',
			'',
			)
	
	ULRS2 = (
			'',
			'',
			'',
			'',
			'',
			'',
			'',
			'',
			'',
			'',
			'',
			'',
			) 
	
	ULRS = (url for url in ULRS if url)
	Mgr.DBEntity = DBBase.DBBase()
	pool = threadpool.ThreadPool(3)
	
	def downloads(url):
		quest = Mgr.DirDownLoad(url)
		quest.DownloadQuest()
	
	requests = threadpool.makeRequests(downloads, ULRS)
	[pool.putRequest(req) for req in requests]
	pool.poll()

