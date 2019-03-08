#!/usr/bin/env python
# Author: weikun
# Created Time: Thu 07 Mar 2019 06:37:11 PM CST

import Mgr

class DirDownLoad(object):
	def __init__(self, url):
		self.url = url

	def download(self):
		dirName, UUID, UrlIter = Mgr.UrlParse.parse(self.url)
		if not (dirName and UUID and UrlIter):
			yield 'Complete'
		
		if Mgr.DBEntity.HasCompleteDirName(dirName):
			yield 'Complete'

		failUrlNum = 0

		while True:
			for imgUrl, fileName in UrlIter():
				tryTimes = Mgr.MAX_FAIL_URL_TIMES
				while tryTimes > 0:
					if Mgr.UrlDownLoad.downFile(imgUrl, dirName + fileName):
						break
					else:
						tryTimes -= 1
	
				if tryTimes <= 0:
					failUrlNum += 1
				else:
					Mgr.LogEntity.Log("DownLoads %s" % (dirName + fileName, ))
	
				if failUrlNum >= Mgr.MAX_FAIL_URL_NUM:
					#Mgr.DBEntity.CompleteDirName(dirName)
					yield 'Complete'
				else:
					yield 'Continue'


Mgr.DirDownLoad = DirDownLoad
