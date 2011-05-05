#!/usr/bin/env python

import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page, dashboard_public_page, fd_login_data
from vars import ConnectionParameters

class check_addon_pagination(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect(ConnectionParameters.browser)
    
    def testAddonPagination(self):
        #This test is to assert that if the count of the addons on dashboard is more than 10, then the addons should be paginated on public addons page.
        #Create page objects
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        public_page_obj = dashboard_public_page.DashboardPublicPage(sel)
        
        user_info = fd_login_data.FDLoginData().getLoginInfo()
        username = user_info['username']
        password = user_info['password']
    
        homepage_obj.go_to_home_page()
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        
        #Get the total count of the number of add-ons that are displayed on the dashboard.
        #homepage_obj.click_myaccount()
        addon_count = dashboardpage_obj.calc_total_addons()
        
        if addon_count>10:
        #If there are more than 10 addons on the dashboard, go to the public addons page and check that the next button is present for pagination
            dashboardpage_obj.go_to_public_addons_page()
            self.assertTrue(public_page_obj.check_next_button_present())
        else:
            print 'Total addons are less then 10, so there will be no pagination'

    def testLibraryPagination(self):
        #This test is to assert that if the count of the libraries on dashboard is more than 10, then the libraries should be paginated on public libraries page.
        #Create page objects
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        public_page_obj = dashboard_public_page.DashboardPublicPage(sel)
        
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
        
        if lib_count>10:
        #If there are more than 10 addons on the dashboard, go to the public addons page and check that the next button is present for pagination
            dashboardpage_obj.go_to_public_libs_page()
            self.assertTrue(public_page_obj.check_next_button_present())
        else:
            print 'Total Libraries are less then 10, so there will be no pagination'


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()