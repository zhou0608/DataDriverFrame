# coding=utf-8

from DataDrivenFrameWork.util.ObjectMap import *
from DataDrivenFrameWork.util.PareConfigurationFile import ParseCofigFile


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF=ParseCofigFile()
        self.loginOptions=self.parseCF.getItemsSection('126mail_login')

    def switchToFrame(self):
        try:
            #从定位表达式配置文件中读取frame的定位表达式
            locatorExpression=self.loginOptions\
                ['loginPage.frame'.lower()].split(">")[1]
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(locatorExpression))
        except Exception as e:
            raise e

    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    def userNameObj(self):
        try:
            #从定位表达式配置文件中读取定位用户输入框的定位方式和表达式
            locateType,locatorExpression=self.loginOptions\
                ['loginPage.username'.lower()].split('>')
            elementObj = getElement(self.driver, locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            #从定位表达式配置文件中读取定位密码输入框的定位方式和表达式
            locateType,locatorExpression=self.loginOptions\
                ['loginPage.password'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def logingButton(self):
        try:
            # 从定位表达式配置文件中读取登录按钮的定位方式和表达式
            locateType, locatorExpression = self.loginOptions \
                ['loginPage.loginbutton'.lower()].split('>')
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e


if __name__ == '__main__':

    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('http://mail.163.com')
    import time
    time.sleep(3)
    login = LoginPage(driver)
    login.switchToFrame()
    login.userNameObj().send_keys('zjj_test@163.com')
    login.passwordObj().send_keys('9527zj.')
    time.sleep(1)
    # driver.find_element_by_id('dologin').click()
    login.logingButton().click()
    login.switchToDefaultFrame()
    driver.quit()
