# -*- coding: utf-8 -*-
"""
Created on Sat May 20 08:14:13 2017

@author: shubra
"""

import sys
import os
import io
import fnmatch
import re
from shutil import copyfile,copy2
from ciscoconfparse import CiscoConfParse
 
 
dirname= "C:/ACL/Final/To_Process/"
 
 
configfile_dir = os.listdir(dirname)
 
file_count =0
error_count=0
file_count_juniper =0
 
for path, dirs, files in os.walk(dirname):
 
    for filename in files:
                if fnmatch.fnmatch(filename, '*.txt'):
                    cfg_file = os.path.abspath(os.path.join(path, filename))
                    file_count =file_count+1
                    f = open(cfg_file)
                    line = f.read()
                    first_line = line.split('\n', 1)[0]
                   
                    print(cfg_file)
                    if re.search('^## Last commit:', first_line):
                            file_count_juniper =file_count_juniper +1
                            parse = CiscoConfParse(cfg_file, syntax='junos', comment='#!')
                            print(cfg_file)
                            
                            target = open(cfg_file+'.dat', 'w')
                           
                            for line in parse.ioscfg:
                            #    print (line)
                                target.writelines(line)
                                target.writelines("\n")
#                           
                            target.close()  
print("Total File =",file_count,"Juniper Files=",file_count_juniper)
