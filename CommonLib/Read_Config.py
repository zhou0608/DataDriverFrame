# -*- coding: utf-8 -*-
import  configparser,os
def get_ini(key,value):
    cofing = configparser.ConfigParser()
    path =os.path.dirname(__file__)+'/config.ini'
    cofing.read(path)
    value =cofing.get(key,value)
    return value

global_min_time=1
global_mid_time=3
global_max_time=5