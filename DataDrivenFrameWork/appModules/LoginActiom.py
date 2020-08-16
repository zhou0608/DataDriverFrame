# coding=utf-8
from DataDrivenFrameWork.pageObjects.LoginPage import LoginPage


class LoginAction:
    def __init__(self):
        print('login.....')

    @staticmethod
    def login(driver, user, pas):
        try:
            loging = LoginPage(driver)
            loging.switchToFrame()
            loging.userNameObj().send_keys(user)
            loging.passwordObj().send_keys(pas)
            loging.logingButton().click()
            loging.switchToDefaultFrame()
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Firefox()
    driver.get('https://mail.163.com')
    LoginAction.login(driver, user='zjj_test@163.com', pas='Email9668')
    time.sleep(3)
    driver.quit()
