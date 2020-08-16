#coding=utf-8
from DataDrivenFrameWork.util.ObjectMap import *
from DataDrivenFrameWork.util.PareConfigurationFile import ParseCofigFile

class HomePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF=ParseCofigFile()

    def addressLink(self):
        try:
            #从定位表达式配置文件中读取定位通讯率按钮的定位方式和表达式
            locatType,locatorExpression=self.parseCF.getOptionValue\
                ('126mail_homePage','homePage.addressbook').split('>')
            #获取登录成功页面的通讯录页面元素，并返回给调用者
            elementObj=getElement(self.driver,locatType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e
if __name__ == '__main__':
    from selenium import webdriver
    driver=webdriver.Firefox()
    HomePage(driver)