# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:45:12 2018

@author: aksha
"""


import time
import datetime

print ("Time in seconds since the epoch: %s" %time.time())
print ("Current date and time: " , datetime.datetime.now())
print ("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))


print ("Current year: ", datetime.date.today().strftime("%Y"))
print ("Month of year: ", datetime.date.today().strftime("%B"))