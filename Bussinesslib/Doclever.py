from Corelib.SeleinumLib import SeleniumLib
from  ObjectStore.Docleverlb_object import  *
class Docleverlib(SeleniumLib):
    def login(self,user,pas):
        self.new_find_element(login_text).click()
        self.new_find_element(user_input).clear()
        self.new_find_element(user_input).send_keys(user)
        self.new_find_element(pas_input).clear()
        self.new_find_element(pas_input).send_keys(pas)
        self.new_find_element(login_but).click()
