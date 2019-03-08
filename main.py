#!/usr/bin/env python
# Author: weikun
# Created Time: Thu 07 Mar 2019 06:02:47 PM CST

import os
import Mgr
import Log
import UrlDownLoad
import DirDownLoad

class UrlParse(object):
	def __init__(self):
		pass

	def parse(self, url):
		#string = Mgr.UrlDownLoad.downStr(url)
		
		dirName = u'Y:/BT_UT/Test_Grap/'
		if not os.path.exists(dirName):
			os.makedirs(dirName)
			
		UUID = 1
		def urlIter():
			index = 1
			while True:
				imgUrl = 'https://%d.jpg' % (index, )
				fileName = '%03d.jpg' % (index, )
				index += 1
				yield imgUrl, fileName
		return dirName, UUID, urlIter


Mgr.UrlParse = UrlParse()

if __name__ == '__main__':
	import DBBase
	Mgr.ProjectName = 'Test'
	Mgr.DBEntity = DBBase.DBBase()
	quest = Mgr.DirDownLoad('')
	ret = 'Begin'
	
	for ret in quest.download():
		if ret == 'Complete':
			break
	

