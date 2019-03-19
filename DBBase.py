#!/usr/bin/env python
# Author: weikun
# Created Time: Thu 07 Mar 2019 06:03:04 PM CST

class DBBase(object):
    def __init__(self):
        pass

    def initDB(self):
        pass

    def HasCompleteDirName(self, dirName):
        return False

    def CompleteDirName(self, dirName):
        print 'CompleteDirName %s' % (dirName, )

