#!/usr/bin/env python

import unittest, time, re, string
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page, fd_login_data

#My Account Page
#This test should be run only after you run the create library test.First create an library. Then go to dashoard and compare that the label is 'initial'. then create a copy of that library and compare that the label is 'copy'
class check_lib_label(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect('firefox')

    def testLibCount(self):
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)

        user_info = fd_login_data.FDLoginData().getLoginInfo()
        username = user_info['username']
        password = user_info['password']
    
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        
        #Get the total count of the number of add-ons that are displayed on the dashboard.
        #homepage_obj.click_myaccount()
        lib_count = dashboardpage_obj.calc_total_libs()

        #Get the number of libraries that are displayed on the left hand side of the page.(Something like your Libraries(20))
        counter = dashboardpage_obj.get_libs_count()
        counter = string.lstrip(counter, '(')
        counter = string.rstrip(counter, ')')
    
        #Assert that the total libraries on the page matches the counter on the left hand side.
        self.assertEquals(str(lib_count), str(counter))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
