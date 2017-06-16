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



 

outdirname="C:/ACL/"

csvfilename="Cisco_test.csv"

 

 

dirname= "C:/ACL/Final/To_Process/"

cisco="C:/ACL/Final/types/cisco/"

cisco1="C:/ACL/Final/types/cisco1/"

juniper="C:/ACL/Final/types/juniper/"

all_f="C:r/ACL/Final/types/all/"

 

 

configfile_dir = os.listdir(dirname)

 

file_count =0

file_count_cisco1 =0

file_count_juniper =0

file_count_cisco =0

for path, dirs, files in os.walk(dirname):

 

    for filename in files:

                if fnmatch.fnmatch(filename, '*.Config'):

                    cfg_file = os.path.abspath(os.path.join(path, filename))

#                    print(cfg_file)

                    file_count =file_count+1

                    f = open(cfg_file)

                    line = f.read()

                    first_line = line.split('\n', 1)[0]

                    copy2(cfg_file,all_f)

#                    print(first_line)

                    if re.search('^## Last commit:', first_line):

                            file_count_juniper =file_count_juniper +1

                            copy2(cfg_file,juniper)

                           

                    if re.search('^!$', first_line):

                        file_count_cisco =file_count_cisco+1

                        copy2(cfg_file,cisco)

                        Full_Path_File_Nmae = cfg_file

 

#                        parse_cisco_files(Full_Path_File_Nmae,outdirname,csvfilename)

                       

                    if re.search('^!Command:', first_line):

                        file_count_cisco1 =file_count_cisco1+1   

                        copy2(cfg_file,cisco1)

 

                       

def juniper_file():

    for path, dirs, files in os.walk(dirname):

 

         for filename in files:

                if fnmatch.fnmatch(filename, '*.Config'):

                    cfg_file = os.path.abspath(os.path.join(path, filename))

                    f = open(cfg_file)

                    line = f.read()

                    first_line = line.split('\n', 1)[0]

                    if re.search('^## Last commit:', first_line):

                               return cfg_file

                           

def cisco_file(dirname):

    for path, dirs, files in os.walk(dirname):

 

         for filename in files:

                if fnmatch.fnmatch(filename, '*.Config'):

                    cfg_file = os.path.abspath(os.path.join(path, filename))

                    f = open(cfg_file)

                   line = f.read()

                    first_line = line.split('\n', 1)[0]

                    if re.search('^!$', first_line):

                               return cfg_file

 

 

def cisco1_file():

    for path, dirs, files in os.walk(dirname):

 

         for filename in files:

                if fnmatch.fnmatch(filename, '*.Config'):

                    cfg_file = os.path.abspath(os.path.join(path, filename))

                    f = open(cfg_file)

                    line = f.read()

                    first_line = line.split('\n', 1)[0]

                    if re.search('^!Command:', first_line):

                               return cfg_file                           

                            

                         

                        

 

print(file_count,file_count_juniper,file_count_cisco,file_count_cisco1)