#coding=utf-8
from DataDrivenFrameWork.config.VarConfig import pageElementLocatorPath
import configparser

class ParseCofigFile(object):
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self,sectionName):
        #获取配置文件中指定section下的所有option键值对
        #并以字段类型返回给调用者
        """注意：
        使用self.cf.items(sectionName)此种方法获取到
        的配置文件中的options内容均被转成小写，
        比如，loginpage.frame被转换成了loginpage.frame
        """
        optionsDict=dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self,sectionName,optionName):
        #获取指定section下的执行option得值
        value = self.cf.get(sectionName,optionName)
        return value

if __name__ == '__main__':
    pc=ParseCofigFile()
    print(pc.getItemsSection('126mail_login'))
    print(pc.getOptionValue('126mail_login','loginPage.frame'))