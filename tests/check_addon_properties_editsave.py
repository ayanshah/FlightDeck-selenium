#!/usr/bin/env python

import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, lib_editor_page, addon_editor_page, dashboard_public_page, fd_login_data

class check_addon_properties_editsave(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect('firefox')
    
    def testAddonPropertiesEditSave(self):
        #This test is to assert that the properties of an addon can be edited and changes are retained after save.
        #Create page objects
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)
        public_page_obj = dashboard_public_page.DashboardPublicPage(sel)
        addonpage_obj = addon_editor_page.AddonEditorPage(sel)
        
        user_info = fd_login_data.FDLoginData().getLoginInfo()
        username = user_info['username']
        password = user_info['password']
        
        name = 'test'
        description = 'Description_test'
    
        homepage_obj.go_to_home_page()
        homepage_obj.click_create_addon_btn()
        loginpage_obj.login(username, password)

        
        #Edit the properties, save the addon and then check that the changes have been retained. Delete the addon at the end of the process.
        addon_name = addonpage_obj.get_addon_name()
        addonpage_obj.open_addon_properties()
        addonpage_obj.edit_fields(name, description, version)
        addonpage_obj.open_addon_properties()
        new_name = addonpage_obj.get_property_addon_name()
        #print new_name
        desc = addonpage_obj.get_addon_description()
        #print desc
        self.assertNotEquals(addon_name,new_name)
        self.assertEquals(description, desc.text)
        
        homepage_obj.click_myaccount()
        dashboardpage_obj.click_addon_delete()
        dashboardpage_obj.confirm_delete()

    def tearDown(self):
        self.driver.quit()


#
#
#class check_addon_info_editable(unittest.TestCase):
#    def setUp(self):
#        self.verificationErrors = []
#        self.selenium = selenium("localhost", 4444, "*firefox /Applications/Firefox4.0b7/Firefox.app/Contents/MacOS/firefox-bin", "https://builder-addons.allizom.org/")
#        self.selenium.start()
#    
#    def test_check_addon_info_editable(self):
#        sel = self.selenium
#        sel.open("/")
#        sel.set_speed(1000)
#        sel.click("signin")
#        sel.wait_for_page_to_load("30000")
#        sel.type("id_username", "amo.test.acc@gmail.com")
#        sel.type("id_password", "qwertyasdf")
#        sel.click("save")
#        sel.wait_for_page_to_load("30000")
#        
#        #After login, click on the "Edit" button on the first add-on.
#        #Then, check that, when you click on the add-on name and it displays the add-on information, you should be able to edit the fields.
#        sel.click("//section[@id='app-content']/ul[1]/li[1]/ul/li[3]/a")
#        sel.wait_for_page_to_load("30000")
#        add_on_name=sel.get_text("//section[@id='package-info']/h3[@id='ji-toggler']/a")
#        #print add_on_name
#        sel.click("link="+add_on_name)
#        sel.type("full_name", "Name change test")
#        sel.type("package_description", "This is description")
#        sel.click("//input[@value='OK']")
#        
#        #click on addon name again to check if changed values have persisted(in future,ask to change the name as soon as the user clicks OK in the previous step)
#        sel.click("link="+add_on_name)
#        new_name=sel.get_value("//form[@id='package-info_form']/fieldset/p[1]/input[@id='full_name']")
#        #print new_name
#        self.assertNotEquals(add_on_name,new_name)
#        add_on_desc=sel.get_value("//form[@id='package-info_form']/fieldset/p[2]/textarea[@id='package_description']")
#        #print add_on_desc
#
#        self.assertEquals(add_on_desc,"This is description")
#        sel.click("//input[@value='OK']")
#        #sel.click("package-save")
#        #sel.click("link=Sign Out")
#
#    
#    def tearDown(self):
#        self.selenium.stop()
#        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
