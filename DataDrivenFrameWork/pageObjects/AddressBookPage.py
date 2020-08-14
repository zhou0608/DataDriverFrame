#coding=utf-8
from Book_code.DataDrivenFrameWork.util.ObjectMap import *
from Book_code.DataDrivenFrameWork.util.PareConfigurationFile import ParseCofigFile

class AddressBookPage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parseCF=ParseCofigFile()
        self.addContactsOptions=self.parseCF.getItemsSection('126mail_addContactsPage')
        print(self.addContactsOptions)

    def creatContactPersonButton(self):
        #获取新建联系人按钮
        try:
            locateType,locatorExpression=self.addContactsOptions\
                ['addContactsPage.createContactsBtn'.lower()].split('>')
            elementobj=getElement(self.driver,locateType,locatorExpression)
            return elementobj
        except Exception as e:
            raise e

    def contatPersonName(self):
        try:
            #从定位表达式配置文件中读取联系人姓名输入框的定位方式和表达式
            locatrType,locatorExpression=self.addContactsOptions\
                ['addContactsPage.contactPersoName'.lower()].split('>')
            #获取新建联系人界面的姓名输入框页面元素，并返回给调用者
            elementobj=getElement(self.driver,locatrType,locatorExpression)
            return elementobj
        except Exception as  e:
            raise e

    def contactPersonEmail(self):
        #获取新建联系人界面中的电子邮件输入框
        try:
            #从定位表达式配置文件中读取联系人邮箱输入框的定位方式和表达式
            locatrType,locatorExpression=self.addContactsOptions\
                ['addContactsPage.conntactPersonEmail'.lower()].split('>')
            #获取新建联系人界面的邮箱输入框页面元素，并返回给调用者
            elementobj=getElement(self.driver,locatrType,locatorExpression)
            return elementobj
        except Exception as  e:
            raise e
    def starContacts(self):
        #获取新建联系人界面中的星标联系人选择框
        try:
            #从定位表达式配置文件中读取星标联系人复选框的定位方式和表达式
            locatrType,locatorExpression=self.addContactsOptions\
                ['addContactsPage.starContacts'.lower()].split('>')
            #获取新建联系人界面的星标联系人复选框页面元素，并返回给调用者
            elementobj=getElement(self.driver,locatrType,locatorExpression)
            return elementobj
        except Exception as  e:
            raise e

    def contactPersonMobile(self):
        #获取新建联系人界面中的联系人手机号输入框
        try:
            #从定位表达式配置文件中读取联系人手机号输入框的定位方式和表达式
            locatrType,locatorExpression=self.addContactsOptions\
                ['addContactsPage.contactPersonMobile'.lower()].split('>')
            #获取新建联系人界面的联系人手机号输入框页面元素，并返回给调用者
            elementobj=getElement(self.driver,locatrType,locatorExpression)
            return elementobj
        except Exception as  e:
            raise e

    def contactPersonComment(self):
        #获取新建联系人界面中的联系人备注信息输入框
        try:
            #从定位表达式配置文件中读取联系人备注信息输入框的定位方式和表达式
            locatrType,locatorExpression=self.addContactsOptions\
                ['addContactsPage.contactPersonComment'.lower()].split('>')
            #获取新建联系人界面的联系人备注信息输入框页面元素，并返回给调用者
            elementobj=getElement(self.driver,locatrType,locatorExpression)
            return elementobj
        except Exception as  e:
            raise e

    def saveContacePerson(self):
        #获取新建联系人界面中的保存联系人按钮
        try:
            #从定位表达式配置文件中读取保存联系人按钮的定位方式和表达式
            locatrType,locatorExpression=self.addContactsOptions\
                ['addContactsPage.savecontacePerson'.lower()].split('>')
            #获取新建联系人界面的保存联系人按钮页面元素，并返回给调用者
            elementobj=getElement(self.driver,locatrType,locatorExpression)
            return elementobj
        except Exception as  e:
            raise e