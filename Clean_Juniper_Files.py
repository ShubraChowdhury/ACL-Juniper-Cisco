# -*- coding: utf-8 -*-
"""
Created on Sat May 20 08:11:07 2017

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
                if fnmatch.fnmatch(filename, '*.Config'):
                    cfg_file = os.path.abspath(os.path.join(path, filename))
                    file_count =file_count+1
                    f = open(cfg_file)
                    line = f.read()
                    first_line = line.split('\n', 1)[0]
                    Last_line = len(line)
                   
                    if re.search('^## Last commit:', first_line):
                            file_count_juniper =file_count_juniper +1
                            target = open(cfg_file+'.txt', 'w')
#                            print(cfg_file)
                            with io.open(cfg_file,'r',encoding='utf-8',errors='ignore') as ff:
                                for num, line1 in enumerate(ff, 1):
                                   
                                    if re.search('^{master:', line1):
#                                        print( line1.replace(line1[0:len(line1)],''))
                                         print("Master: ", cfg_file)
#                                        rep_line = line[0:len(line1)]
#                                        print(rep_line)
                                    elif re.search('^{primary:', line1):
                                        print("primary: ", cfg_file)
                                       
                                    elif re.search('^{master', line1):
                                         print("Master ", cfg_file)
                                         
                                    else:
#                                        print(cfg_file+'.txt' )
                                        target.writelines(line1)
                                        target.writelines("\n")
                            target.close()           
                            ff.close()
                    f.close()
 
                                  
 
print("Total File =",file_count,"Juniper Files=",file_count_juniper,"Juniper Error =",error_count)
