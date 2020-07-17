# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from CommonLib.Read_Config import *

class SeleniumLib(object):
    def run_driver(self):
        self.launch_browser()
        time.sleep(10)
        self.driver.implicitly_wait(5)
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
                # return self.driver
            elif brower.lower() == 'firefox':
                self.driver = webdriver.Firefox()
                return self.driver
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
            return False

    def is_element_present(self,obj):
        time.sleep(global_mid_time)
        try:
            self.new_find_element(obj)
            return True
        except Exception as err:
            return False

    def is_text_present(self,obj):
        time.sleep(global_mid_time)
        text_path = "//*[contains(text(),'"+obj+"')]"
        try:
            self.driver.find_element_by_xpath(text_path)
            return True
        except:
            return False


if __name__=='__main__':
    run = SeleniumLib()
    run.is_text_present('用户名或者密111码错误')