import unittest, time, re
from selenium.webdriver.common.exceptions import NoSuchElementException
import home_page, login_page, dashboard_page, fd_login_data
from selenium import webdriver

class check_disable_button_present_after_signin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.connect('firefox')
    
    def testShouldCheckDisableButtonPresentAfterSignin(self):
        #This test case should be run only after create addon and create library test case
        sel = self.driver
        homepage_obj = home_page.HomePage(sel)
        loginpage_obj = login_page.LoginPage(sel)
        dashboardpage_obj = dashboard_page.DashboardPage(sel)

        user_info = fd_login_data.FDLoginData().getLoginInfo()
        username = user_info['username']
        password = user_info['password']
        
        homepage_obj.go_to_home_page()

        #Check that the disable button are not present for addon and library.
        self.assertFalse(homepage_obj.check_addon_disable_btn_present())
        self.assertFalse(homepage_obj.check_lib_disable_btn_present())
            
        homepage_obj.click_signin()
        loginpage_obj.login(username, password)
        self.assertEqual("Dashboard - Add-on Builder", dashboardpage_obj.get_page_title())
        homepage_obj.go_to_home_page()
        
        #Check that the disable button should be present now for addon and library
        self.assertTrue(homepage_obj.check_addon_disable_btn_present())
        self.assertTrue(homepage_obj.check_lib_disable_btn_present())

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
