from Corelib.SeleinumLib import SeleniumLib
from  ObjectStore.Docleverlb_object import  *
from CommonLib.Read_Ini import *
class Docleverlib(SeleniumLib):

    def login(self):
        self.new_find_element(login_text).click()
        self.new_find_element(user_input).clear()
        self.new_find_element(user_input).send_keys(get_ini('data','user'))
        self.new_find_element(pas_input).clear()
        self.new_find_element(pas_input).send_keys(get_ini('data','pas'))
        self.new_find_element(login_but).click()
