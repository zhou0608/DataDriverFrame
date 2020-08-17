#coding=utf-8
import time

from DataDrivenFrameWork.util.Log import *
from selenium.webdriver.chrome.options import Options
from DataDrivenFrameWork.util.ParseExcel import ParseExcel
from DataDrivenFrameWork.config.VarConfig import *
from DataDrivenFrameWork.appModules.AddContactPersonAction import AddContactPerson
from selenium import webdriver
from DataDrivenFrameWork.appModules.LoginActiom import LoginAction
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
    driver = webdriver.Firefox()
    driver.get('http://mail.163.com')
    return driver
    '''
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
    driver=webdriver.Firefox(executable_path=r'D:\Software\Python3.7\geckodriver',chrome_options=chrome_options)
    driver.get('http://mail.163.com')
    sleep(3)
    return driver
    '''
def test126MailAddContacts():
    username=None
    password=None
    logging.info(u'163邮箱添加联系人数据驱动测试开始。。。')
    try:
        #根据Excel文件中的sheet名称获取此sheet对象
        userSheet=excelObj.getSheetByName('126账号')
        #获取126账号sheet中是否执行列
        isExecuteUser=excelObj.getColumn(userSheet,account_isExecute)
        #获取126账户sheet中的数据表列
        dataBookColumn=excelObj.getColumn(userSheet,account_dataBook)
        for idx,i in enumerate(isExecuteUser[1:]):
            #循环遍历126账号表中的账号，为需要执行的账户添加联系人
            if i.value=='y':#表示要执行
                #获取第idx+2行的数据
                userRow=excelObj.getRow(userSheet,idx+2)
                #获取第idx+2行中的用户名
                username=userRow[account_username-1].value
                #获取第i行中的密码
                password = str(userRow[account_password-1].value)
                print('用户名%s,密码%s'%(username,password))

            #创建浏览器实例对象
            logging.info('启动浏览器，访问163邮箱主页')
            driver = LaunchBrowser()
            logging.info('启动浏览器，访问163邮箱主页成功')
            #登录126邮箱
            LoginAction.login(driver,username,password)

            #等待3秒，让浏览器启动完成，以便正常进行后续操作
            time.sleep(3)
            try:
                #断言登录后跳转页面的标题是否包含‘网易邮箱’
                assert '收件箱' in driver.page_source
                logging.info('用户%s登录后，断言页面关键字"收件箱"成功'%username)
            except AssertionError as e:
                logging.info('用户%s登录后，断言页面关键字"收件箱"失败'
                             u'异常信息：%s'%(username,str(traceback.format_exc())))

            #获取为第idx+2行中用户添加的联系人数据表sheet名
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
                    print('打印1：',contactPersonName,contactPersonEmail,assertKeyWord)
                    print('打印2：',contactPersonPhone,contactPersonComment,isStar)
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
                    logging.info('添加联系人%s成功'%contactPersonEmail)

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
                        logging.info('断言关键字%s成功'%assertKeyWord)
                else:
                    logging.info(u'联系人%s被忽略执行'%contactPersonEmail)
            if contactiNum==isExecuteNum:
                #如果成功添加的联系人数与需要添加的联系人数相等，
                #说明给第i个用户添加联系人测试用例执行成功，
                #在126账户工作表中写入成功信息，否则写入失败信息
                excelObj.writeCell(userSheet,'pass',rowNo=idx+2,
                                   colsNo=account_testResult,style='green')
            else:
                excelObj.writeCell(userSheet,'faild',rowNo=idx+2,
                                   colsNo=account_testResult,style='red')
            logging.info('为用户%s添加%d个联系人，%d个成功\n'%(username,isExecuteNum,contactiNum))
        else:
            #获取被忽略执行的用户名
            ignoreUserName=excelObj.getcellOfValue(userSheet,
                                                   rowNo=id+2,colsNo=account_username)
            logging.info('用户%s被忽略执行\n'%ignoreUserName)
    except Exception as e:
        logging.info('数据驱动框架主程序执行过程发生异常，异常信息：%s'%str(traceback.format_exc()))
    finally:
        driver.quit()
if __name__ == '__main__':
    test126MailAddContacts()
    print('看看是否成功')
