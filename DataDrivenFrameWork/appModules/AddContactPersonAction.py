#cofing=utf-8
from Book_code.DataDrivenFrameWork.pageObjects.AddressBookPage import AddressBookPage
from Book_code.DataDrivenFrameWork.pageObjects.HomePage import HomePage
import traceback
import time
class AddContactPerson(object):
    def __init__(self):
        print('add cotact person')

    @staticmethod
    def add(driver,contactName,contactEmail,isStar,contactPhone,contactComment):
        try:
            #创建主业实例对象
            hp=HomePage(driver)
            hp.addressLink().click()
            time.sleep(3)
            #创建添加联系人页实例对象
            apb=AddressBookPage(driver)
            apb.creatContactPersonButton().click()
            if contactName:
                #非必填项
                apb.contatPersonName().send_keys(contactName)
                #必填项
                apb.contactPersonEmail().send_keys(contactEmail)
            if isStar =='是':
                #非必填项
                apb.starContacts().click()
            if contactPhone:
                #非必填项
                apb.contactPersonMobile().send_keys(contactPhone)
            if contactComment:
                apb.contactPersonMobile().send_keys(contactPhone)
            apb.saveContacePerson().click()
        except Exception as e:
            raise e

if __name__ == '__main__':
    from Book_code.DataDrivenFrameWork.appModules.LoginActiom import  LoginAction
    from selenium import  webdriver
    import time
    driver = webdriver.Firefox()
    driver.get('http://mail.163.com')
    time.sleep(3)
    LoginAction.login(driver,'zjj_test@163.com','Email9668')
    time.sleep(3)
    AddContactPerson.add(driver,'zjj','6433662@qq.com','是','','')
    time.sleep(3)
    assert u'zjj' in driver.page_source
    driver.quit()