#!/usr/bin/env python

from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.exceptions import NoSuchElementException
from page import Page

class AddonEditorPage(Page):

    _addon_name = 'package-info-name'
    _signin_link = 'signin'
    _home_page_url = 'https://builder-addons.allizom.org/'
    _test_btn = 'try_in_browser'
    _download_btn = 'download'
    _save_btn = 'package-save'
    _copy_btn = 'package-copy'
    _error_console_btn = 'error-console'
    _revision_btn = 'revisions_list'
    _properties_btn = 'package-properties'
    _property_addon_name = 'full_name'
    _property_addon_desc = 'package_description'
    _property_addon_version = 'version_name'
    _property_save = 'savenow'
    
    def __init__(self, selenium):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = selenium

    def get_addon_name(self):
        return self.sel.find_element_by_id(self._addon_name).text

    def get_property_addon_name(self):
        return self.sel.find_element_by_id(self._property_addon_name).text
        
    def get_addon_version(self):
        return self.sel.find_element_by_id(self._property_addon_version).text
    
    def check_fields_not_editable(self):
        try:
            self.sel.find_element_by_id(self._property_addon_name)
            return True
        except NoSuchElementException:
            return False

    def get_addon_description(self):
        return self.sel.find_element_by_id(self._property_addon_desc).text

    def click_signin(self):
        self.sel.find_element_by_id(self._signin_link).click()
        return
    
    def click_copy_btn(self):
        self.sel.find_element_by_id(self._copy_btn).click()
        self.sel.implicitly_wait(10)
        return

    def check_test_btn_present(self):
        try:
            self.sel.find_element_by_id(self._test_btn)
            return True
        except NoSuchElementException:
            return False

    def check_download_btn_present(self):
        try:
            self.sel.find_element_by_id(self._download_btn)
            return True
        except NoSuchElementException:
            return False

    def check_save_btn_present(self):
        try:
            self.sel.find_element_by_id(self._save_btn)
            return True
        except NoSuchElementException:
            return False

    def check_copy_btn_present(self):
        try:
            self.sel.find_element_by_id(self._copy_btn)
            return True
        except NoSuchElementException:
            return False

    def check_error_console_btn_present(self):
        try:
            self.sel.find_element_by_id(self._error_console_btn)
            return True
        except NoSuchElementException:
            return False
        
    def check_revision_btn_present(self):
        try:
            self.sel.find_element_by_id(self._revision_btn)
            return True
        except NoSuchElementException:
            return False
    
    def check_properties_btn_present(self):
        try:
            self.sel.find_element_by_id(self._properties_btn)
            return True
        except NoSuchElementException:
            return False
    
    def open_addon_properties(self):
        self.sel.find_element_by_id(self._properties_btn).click()
        self.sel.implicitly_wait(10)
        return
    
    def click_save_btn(self):
        self.sel.find_element_by_id(self._save_btn).click()
        flag = self.sel.execute_script("return fd.edited")
        print flag
        #alert = self.sel.switch_to_alert()
        #alert.accept()
        self.sel.implicitly_wait(10)
        return flag
    
    def edit_fields(self, name, description, version):
        self.sel.find_element_by_id(self._property_addon_name).clear()
        self.sel.find_element_by_id(self._property_addon_desc).clear()
        self.sel.find_element_by_id(self._property_addon_version).clear()
        self.sel.find_element_by_id(self._property_addon_name).send_keys(name)
        self.sel.find_element_by_id(self._property_addon_desc).send_keys(description)
        self.sel.find_element_by_id(self._property_addon_version).send_keys(version)
        self.sel.find_element_by_id(self._property_save).click()
        self.sel.implicitly_wait(10)
        return
    
    def edit_addon(self):
        self.sel.execute_script("{;fd.getItem().editor.editor.getSession().setValue('Write to editor');}")
        flag = self.sel.execute_script("return eval(fd.edited)")
        print flag
        return flag
    
    #def get_edit_flag(self):
