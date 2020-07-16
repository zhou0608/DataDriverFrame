# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from CommonLib.Read_Ini import *
import re
class SeleniumLib(object):
    def run_driver(self):
        self.launch_browser()
        time.sleep(10)
        self.driver.implicitly_wait(30)
        url = get_ini('data', 'url')
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver
    def close_driver(self):
        self.driver.quit()

    def launch_browser(self):
        brower = get_ini('data','brower')
        try:
            if  brower.lower() == 'chrome':
                self.driver = webdriver.Chrome()
                print('启用了浏览器Chrome')
                return self.driver
            elif brower.lower() == 'firefox':
                self.driver = webdriver.Firefox()
                print('启用了浏览器火狐')
        except Exception as err:
            print('浏览器没有启动:',err)


    def new_find_element(self,obj):
        try:
            para = obj.index('=')
            if obj.startswith('id'):
                return self.driver.find_element_by_id(obj[para+1:])
            elif obj.startswith('xpath'):
                return self.driver.find_element_by_xpath(obj[para+1:])
            elif obj.startswith('link_text'):
                return self.driver.find_element_by_link_text(obj[para+1:])
            else:
                return 'aa'
        except Exception as err :
            print('try:',err)
            return False

    def is_element_present(self,obj):
        try:
            self.new_find_element(obj)
            return True
        except:
            return False

if __name__=='__main__':
    run = SeleniumLib()
    run.launch_browser()