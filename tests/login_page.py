#!/usr/bin/env python

from selenium import webdriver
from page import Page

class LoginPage(Page):

    _username = 'id_username'
    _password = 'id_password'
    _login_btn = "//form[@id='login_form']/div[2]/ul/li/input"
    
    
    def __init__(self, selenium):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = selenium
    
    def login(self, username, password):
        self.sel.find_element_by_id(self._username).send_keys(username)
        self.sel.find_element_by_id(self._password).send_keys(password)
        self.sel.find_element_by_xpath(self._login_btn).click()
        self.sel.implicitly_wait(10)
        return