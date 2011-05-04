#!/usr/bin/env python

from selenium import webdriver
from page import Page
from selenium.webdriver.common.exceptions import NoSuchElementException

class DashboardPublicPage(Page):

    _next_link = "//section[@id='app-content']/ul/ul/li[2]/a"

    def __init__(self, selenium):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = selenium

    def check_next_button_present(self):
        try:
            self.sel.find_element_by_xpath(self._next_link)
            return True
        except NoSuchElementException:
            return False
    