from selenium import webdriver

class SeleniumLib(object):
    def run_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.doclever.cn/controller/index/index.html")
        self.driver.maximize_window()
        return self.driver
    def close_driver(self):
        self.driver.quit()

    def new_find_element(self,obj):
        try:
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
            print('try:',err)
            return False

    def is_element_present(self,obj):
        try:
            self.new_find_element(obj)
            return True
        except:
            return False