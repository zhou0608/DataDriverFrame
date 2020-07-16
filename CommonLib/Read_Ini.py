# -*- coding: utf-8 -*-
import  configparser,os
def get_ini(key,value):
    cofing = configparser.ConfigParser()
    path =os.path.dirname(__file__)+'/config.ini'
    cofing.read(path)
    value =cofing.get(key,value)
    return value

