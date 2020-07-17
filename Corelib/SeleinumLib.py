# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from CommonLib.Read_Config import *
from CommonLib.debug_Config import *

class SeleniumLib(object):
    def run_driver(self):
        self.launch_browser()
        time.sleep(10)
        self.driver.implicitly_wait(5)
        url = get_ini('data', 'url')
        self.driver.get(url)
        self.driver.maximize_window()
        logger.info('初始化')
        return self.driver

    def close_driver(self):
        self.driver.quit()
        logger.info('销毁')

    def launch_browser(self):
        brower = get_ini('data','brower')
        try:
            if  brower.lower() == 'chrome':
                self.driver = webdriver.Chrome()
                logger.info('打开谷歌浏览器')
            elif brower.lower() == 'firefox':
                self.driver = webdriver.Firefox()
                logger.info('打开火狐浏览器')
        except Exception as err:
            logger.info('启动浏览器失败原因:%s'%err)

    def new_find_element(self,obj):
        try:
            logger.info('本次操作的元素是:%s'%obj)
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
            logger.info('页面无法查找到元素点不了')
            return False

    def is_element_present(self,element):
        time.sleep(global_mid_time)
        try:
            self.new_find_element(element)
            logger.info('查找的页面元素存在:%s'%element)
            return True
        except Exception as err:
            logger.info('查找的元素不存在:',err)
            return False

    def is_text_present(self,text):
        time.sleep(global_mid_time)
        text_path = "//*[contains(text(),'"+text+"')]"
        try:
            self.driver.find_element_by_xpath(text_path)
            logger.info('查找的页面文字存在:%s'%text)
            return True
        except:
            logger.info('查找的页面文字不存在:%s'%text)
            return False


if __name__=='__main__':
    run = SeleniumLib()
    run.is_text_present('用户名或者密111码错误')