#!/usr/bin/env python

class FDLoginData(object):

    _home_page_url = 'https://builder-addons-next.allizom.org/'

    def __init__(self):
        self.userCredentials ={'username':'amo.test.acc@gmail.com','password':'mozilla'}
        #self.userTuple = (self.userCredentials)

    def getLoginInfo(self):
        return self.userCredentials

    def get_home_page(self):
        return self._home_page_url
