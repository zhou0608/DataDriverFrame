#coding=utf-8
import time
from selenium.webdriver.chrome.options import Options
from Book_code.DataDrivenFrameWork.util.ParseExcel import ParseExcel
from Book_code.DataDrivenFrameWork.config.VarConfig import *
from Book_code.DataDrivenFrameWork.appModules.AddContactPersonAction import AddContactPerson
from selenium import webdriver
from Book_code.DataDrivenFrameWork.appModules.LoginActiom import LoginAction
import traceback
from time import sleep

#设置此次测试的环境编码为utf-8
import  sys,importlib
importlib.reload(sys)

#创建解析Excel对象
excelObj=ParseExcel()
#将Excel数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)

def LaunchBrowser():
    #创建Chrome浏览器的一个Options实例对象
    chrome_options=Options()
    #向options实例添加禁用扩展插件的设置参数项
    chrome_options.add_argument('--disable-extensions')
    #添加屏蔽--igmore-certificate-errors 提示信息得设置参数项
    chrome_options.add_experimental_option\
        ('excludeSwitches',['ignore-certificate-errors'])
    #添加浏览器最大化的设置参数项，已启动就最大化
    chrome_options.add_argument('--start - maximized')
    #启动带有自定义设置的Chrome浏览器
    driver=webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http//mail.163.com')
    sleep(3)
    return driver

def test126MailAddContacts():
    try:
        #根据Excel文件中的sheet名称获取此sheet对象
        userSheet=excelObj.getSheetByName('126账号')
        #获取126账号sheet中是否执行列
        isExecuteUser=excelObj.getColumn(userSheet,account_isExecute)
        #获取126账户sheet中的数据表列
        dataBookColumn=excelObj.getColumn(userSheet,account_dataBook)
        print('测试为126邮箱添加联系人执行开始。。。')
        for idx,i in enumerate(isExecuteUser[1:]):
            #循环遍历126账号表中的账号，为需要执行的账户添加联系人
            if i.value=='y':#表示要执行
                #获取第i行的数据
                userRow=excelObj.getRow(userSheet,idx+2)
                #获取第i行中的用户名
                username=userRow[account_username-1].value
                #获取第i行中的密码
                password = str(userRow[account_password-1].value)
                print(username,password)

            #创建浏览器实例对象
            driver = LaunchBrowser()

            #登录126邮箱
            LoginAction.login(driver,username,password)
            #等待3秒，让浏览器启动完成，以便正常进行后续操作
            time.sleep(3)
            #获取为第i行中用户添加的联系人数据表sheet名
            dataBookName=dataBookColumn[idx+1].value
            #获取对应的数据表对象
            dataSheet=excelObj.getSheetByName(dataBookName)
            #获取联系人数据表中是否执行列对象
            isExecteData = excelObj.getColumn(dataSheet,contacts_isExecute)
            contactiNum=0#记录添加成功联系人个数
            isExecuteNum=0#记录需要执行联系人个数
            for id,data in enumerate(isExecuteUser[1:]):
                #循环遍历是否执行添加联系人列，
                #如果被设置为添加，则进行联系人添加操作
                if data.value=='y':
                    #如果第id行的联系人被设置为执行，则isExecuteNum自增1
                    isExecuteNum +=1
                    #获取联系人表第id+2行对象
                    rowContent=excelObj.getRow(dataSheet,id+2)
                    #获取联系人姓名
                    contactPersonName=\
                        rowContent[contacts_contactPersonName-1].value
                    #获取联系人邮箱
                    contactPersonEmail=\
                        rowContent[contacts_contactPersonEmai-1].value
                    #获取是否设置为星标联系人
                    isStar=rowContent[contacts_isStar-1].value
                    #获取联系人手机号
                    contactPersonPhone=\
                        rowContent[contacts_contactPersonMobile-1].value
                    #获取联系人备注信息
                    contactPersonComment=\
                        rowContent[contacts_contactPersonComment-1].value
                    #添加联系人成功后，断言的关键字
                    assertKeyWord=\
                        rowContent[contacts_assertKetWords - 1].value
                    print(contactPersonName,contactPersonEmail,assertKeyWord)
                    print(contactPersonPhone,contactPersonComment,isStar)
                    #执行新建联系人操作
                    AddContactPerson.add(
                        driver,
                        contactPersonName,
                        contactPersonEmail,
                        isStar,
                        contactPersonPhone,
                        contactPersonComment
                    )
                    sleep(1)
                    #在联系人工作表中写入添加联系人执行时间
                    excelObj.writeCellCurrentTime(dataSheet,
                        rowNo=id+2,colsNo=contacts_runTime)
                    try:
                        #断言给定的关键字是否出现在页面中
                        assert  assertKeyWord in driver.page_source
                    except AssertionError as e:
                        #断言失败，在联系人工作表中写入添加联系人测试失败信息
                        excelObj.writeCell(dataSheet,'faild',rowNo=id+2,
                                           colsNo=contacts_testResult,style='red')
                    else:
                        #断言成功，写入添加联系人成功信息
                        excelObj.writeCell(dataSheet,'pass',rowNo=id+2,
                                           colsNo=contacts_testResult,style='green')
                        contactiNum+=1
            print('contactNum=%s,isExecteNum=%s'%(contactiNum,isExecuteNum))
            if contactiNum==isExecuteNum:
                #如果成功添加的联系人数与需要添加的联系人数相等，
                #说明给第i个用户添加联系人测试用例执行成功，
                #在126账户工作表中写入成功信息，否则写入失败信息
                excelObj.writeCell(userSheet,'pass',rowNo=idx+2,
                                   colsNo=account_testResult,style='green')
                print('为用户%s添加%d个联系人，测试通过！'%(username,contactiNum))
            else:
                excelObj.writeCell(userSheet,'faild',rowNo=idx+2,
                                   colsNo=account_testResult,style='red')
        else:
            print('用户%s被设置为忽略执行！'%excelObj.getcellOfValue(\
                userSheet,rowNo=idx+2,colsNo=account_username))
        driver.quit()
    except Exception as e:
        print('数据驱动框架主程序发生异常，异常信息为：')
        print(traceback.print_exc())
if __name__ == '__main__':
    test126MailAddContacts()
    print('看看是否成功')
