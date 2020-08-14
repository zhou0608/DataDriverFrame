#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait

#获取单个页面元素对象
def getElement(driver,locateType,locatorExpression):
    try:
        elemnent = WebDriverWait(driver,30).until\
            (lambda x:x.find_element(by=locateType,value=locatorExpression))
        return elemnent
    except Exception as e:
        raise e

#获取多个相同页面元素对象，以list返回
def getElements(driver,locateType,locatorExpression):
    try:
        elements = WebDriverWait(driver,30).until(
            lambda x:x.find_elements(by = locateType,value=locatorExpression))
        return elements
    except Exception as e:
        raise e
if __name__ == '__main__':
    from selenium import webdriver
    driver =webdriver.Chrome()
    driver.get('http://www.baidu.com')
    serchBox = getElement(driver,'id','kw')
    print(serchBox.tag_name)
    alist = getElements(driver,'tag name','a')
    print(len(alist))
    driver.quit()