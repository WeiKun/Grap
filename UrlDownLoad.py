#!/usr/bin/env python
# Author: weikun
# Created Time: Thu 07 Mar 2019 06:12:38 PM CST
import os
import Mgr
import requests
import time

class UrlDownLoad(object):
	def __init__(self):
		pass

	def downFile(self, url, path):
		t1 = time.time()
		if os.path.exists(path):
			return True
		
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
		try:
			response = requests.get(url,  timeout=Mgr.HTTP_TIMEOUT, headers=headers)
		except:
			#ERROR
			return False
		
		if response.status_code != 200 or not response.content:
			return False
		
		with open (path,'wb') as f:
			f.write(response.content)
			
		t2 = time.time()
		return True
	
	def downStr(self, url):
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
		try:
			response = requests.get(url,  timeout=Mgr.HTTP_TIMEOUT, headers=headers)
		except:
			#ERROR
			return False
		
		if response.status_code != 200 or not response.content:
			return None
		
		strings = response.content
		#strings = strings.decode('gbk')
		#strings = strings.encode("utf-8")
		return strings

Mgr.UrlDownLoad = UrlDownLoad()
