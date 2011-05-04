#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author = Ayan Shah
# We need to run the add-on create test before this test case is run

import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, addon_editor_page, fd_login_data

class check_buttons_on_addon_editor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.connect('firefox')

    def testShouldCheckButtonsForAddonsInEditAndViewMode(self):
        #This test is to check that we should be able to see specific buttons in the edit mode of an addon.
        #Create page objects
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        addonpage_obj = addon_editor_page.AddonEditorPage(sel)

        user_info = fd_login_data.FDLoginData().getLoginInfo()
        username = user_info['username']
        password = user_info['password']

        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()
        loginpage_obj.login(username, password)

        #When signed in , check that the Test, Download, Save, Copy, Error Console, Revision, Properties button are present on the editor page
        self.assertTrue(addonpage_obj.check_test_btn_present())
        self.assertTrue(addonpage_obj.check_download_btn_present())
        self.assertTrue(addonpage_obj.check_save_btn_present())
        self.assertTrue(addonpage_obj.check_copy_btn_present())
        self.assertTrue(addonpage_obj.check_error_console_btn_present())
        self.assertTrue(addonpage_obj.check_revision_btn_present())
        self.assertTrue(addonpage_obj.check_properties_btn_present())

        homepage_obj.click_signout()
        homepage_obj.click_addon_view_btn()
        
        #After signout, the save and the error console button shoult not be present.
        self.assertTrue(addonpage_obj.check_test_btn_present())
        self.assertTrue(addonpage_obj.check_download_btn_present())
        self.assertTrue(addonpage_obj.check_copy_btn_present())
        self.assertTrue(addonpage_obj.check_revision_btn_present())
        self.assertTrue(addonpage_obj.check_properties_btn_present())

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
