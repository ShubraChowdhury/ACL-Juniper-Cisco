# -*- coding: utf-8 -*-
"""
Created on Sat May 20 08:14:13 2017

@author: shubra
"""



 

from ciscoconfparse import CiscoConfParse

import csv, io,fnmatch,re,os

 

Dir_path = ""

File_name = ''

Full_Path_File_Nmae = Dir_path+File_name

outdirname="C:/ACL/"

csvfilename="Cisco_test11.csv"

dirname= "C:/ACL/Final/To_Process/"

 


 

 

 

def parse_cisco_files(Full_Path_File_Nmae,outdirname,csvfilename):

 

    with io.open(outdirname + "/" + csvfilename,'w',encoding='ascii',errors='replace') as out_file:  

            writer = csv.writer(out_file)

            writer.writerow(('Router_Name','Entry_Type','Entry_Type_Seq','Entry_Name','Child_Seq','Child_Name'))

            

            for path, dirs, files in os.walk(dirname):

 

                for filename in files:

                    if fnmatch.fnmatch(filename, '*.Config'):

                        cfg_file = os.path.abspath(os.path.join(path, filename))

                        f = open(cfg_file)

                        line = f.read()

                        first_line = line.split('\n', 1)[0]

                        if re.search('^!$', first_line):

           

                #            parse = CiscoConfParse(Full_Path_File_Nmae)

                           

                            parse = CiscoConfParse(cfg_file)

                           

                    

                            print(parse)

                   

                            router_name = parse.find_lines("^hostname")

#                            writer.writerow(("".join(router_name),'service','Test','Test','NA','NA'))

                   

                            #Return a list of all Header   

                            service = parse.find_lines("^service")     

                            boot = parse.find_lines("^boot") 

                            security = parse.find_lines("^security")

                            logging = parse.find_lines("^logging")

                            no = parse.find_lines("^no")

                            

                            print("\n")

                            for service_i,service_j in enumerate(service):

                                print("".join(router_name),"\t",'service',"\t" ,service_i,"\t",service_j)

                                writer.writerow(("".join(router_name),'service',service_i,service_j,'NA','NA'))

                            

                            

                            for boot_i,boot_j in enumerate(boot):

                                print("".join(router_name),"\t", 'boot',"\t",boot_i,"\t",boot_j)

                                writer.writerow(("".join(router_name),'boot',boot_i,boot_j,'NA','NA'))

                             

                            for security_i,security_j in enumerate(security):

                               print("".join(router_name),"\t", 'security',"\t",security_i,"\t",security_j)

                                writer.writerow(("".join(router_name),'security',security_i,security_j,'NA','NA'))

                                

                            for logging_i,logging_j in enumerate(logging):

                                print("".join(router_name),"\t", 'logging',"\t",logging_i,"\t",logging_j)   

                                writer.writerow(("".join(router_name),'logging',logging_i,logging_j,'NA','NA'))

                            

                            for no_i,no_j in enumerate(no):

                                print("".join(router_name),"\t", 'no',"\t",no_i,"\t",no_j)

                                writer.writerow(("".join(router_name),'no',no_i,no_j,'NA','NA'))

                            

                            

                            # Return a list of all policy accounting and subinterfaces         

                            aaa = parse.find_lines("^aaa")       

                            

                            for aaa_i,aaa_j in enumerate(aaa):

                            #    print("\n", i,"\t",j)

                                chld_aaa = parse.find_all_children(aaa_j)

                            #    print(len(chld))

                                if len(chld_aaa) >=1 :

                                    for aaa_k,aaa_m in enumerate(chld_aaa):

                                        print( "".join(router_name),"\t", 'aaa',"\t",aaa_i,"\t",aaa_j,"\t",aaa_k,"\t",aaa_m)

                                        writer.writerow(("".join(router_name),'no',aaa_i,aaa_j,aaa_k,aaa_m))

                                else:

                                    print( "".join(router_name),"\t", 'aaa',"\t",aaa_i,"\t",aaa_j)

                                    writer.writerow(("".join(router_name),'aaa',aaa_i,aaa_j,'NA','NA'))

                           

                            

                            # Return a list of all clock         

                            clock = parse.find_lines("^clock")       

                            

                            for clock_i,clock_j in enumerate(clock):

                            #    print("\n", i,"\t",j)

                                chld_clock = parse.find_all_children(clock_j)

                            #    print(len(chld))

                                if len(chld_clock) >=1 :

                                    for clock_k,clock_m in enumerate(chld_clock):

                                        print( "".join(router_name),"\t", 'clock',"\t",clock_i,"\t",clock_j,"\t",clock_k,"\t",clock_m)

                                        writer.writerow(("".join(router_name),'clock',clock_i,clock_j,clock_k,clock_m))

                                else:

                                    print( "".join(router_name),"\t", 'clock',"\t",clock_i,"\t",clock_j)

                    ######  TO DO                

                                    writer.writerow(("".join(router_name),'clock',clock_i,clock_j,'NA','NA'))

                           

                            

                            # Return a list of all dot         

                            dot = parse.find_lines("^dot")       

                            

                            for dot_i,dot_j in enumerate(dot):

                            #    print("\n", i,"\t",j)

                                chld_dot = parse.find_all_children(dot_j)

                            #    print(len(chld))

                                if len(chld_dot) >=1 :

                                    for dot_k,dot_m in enumerate(chld_dot):

                                        print( "".join(router_name),"\t", 'dot',"\t",dot_i,"\t",dot_j,"\t",dot_k,"\t",dot_m)

                                        writer.writerow(("".join(router_name),'dot',dot_i,dot_j,dot_k,dot_m))

                                else:

                                    print( "".join(router_name),"\t", 'dot',"\t",dot_i,"\t",dot_j)

                                    writer.writerow(("".join(router_name),'dot',dot_i,dot_j,'NA','NA'))

                           

                            

                            # Return a list of all ip         

                            ip1 = parse.find_lines("^ip ")  

                            

                            for ip1_a,ip1_b in enumerate(ip1):

                            #     print(a,b)       

                                 chld_ip = parse.find_all_children(ip1_b)

                                 if len(chld_ip) >=1 :

                                     for ip1_k,ip1_m in enumerate(chld_ip):

                                         print( "".join(router_name),"\t", 'ip',"\t",ip1_a,"\t",ip1_b,"\t",ip1_k,"\t",ip1_m)

                                         writer.writerow(("".join(router_name),'ip',ip1_a,ip1_b,ip1_k,ip1_m))

                                 else:

                                    print("".join(router_name),"\t", 'ip',"\t",ip1_a,"\t",ip1_b)

                                    writer.writerow(("".join(router_name),'ip',ip1_a,ip1_b,'NA','NA'))

                           

                            

                            

                            # Return a list of all multilink         

                            multilink = parse.find_lines("^multilink")  

                            

                            for multilink_a,multilink_b in enumerate(multilink):

                            #     print(a,b)       

                                 chld_multilink = parse.find_all_children(multilink_b)

                                 if len(chld_multilink) >=1 :

                                     for multilink_k,multilink_m in enumerate(chld_ip):

                                         print( "".join(router_name),"\t", 'multilink',"\t",multilink_a,"\t",multilink_b,"\t",multilink_k,"\t",multilink_m)

                                         writer.writerow(("".join(router_name),'multilink',multilink_a,multilink_b,multilink_k,multilink_m))

                                 else:

                                    print("".join(router_name),"\t", 'multilink',"\t",multilink_a,"\t",multilink_b)

                                    writer.writerow(("".join(router_name),'multilink',multilink_a,multilink_b,'NA','NA'))

                           

                                    

                            voice_card = parse.find_lines("^voice-card")  

                            

                            for voice_card_a,voice_card_b in enumerate(voice_card):

                            #     print(a,b)       

                                 chld_voice_card = parse.find_all_children(voice_card_b)

                                 if len(chld_voice_card) >=1 :

                                     for voice_card_k,voice_card_m in enumerate(chld_voice_card):

                                         print( "".join(router_name),"\t", 'voice_card',"\t",voice_card_a,"\t",voice_card_b,"\t",voice_card_k,"\t",voice_card_m)

                                         writer.writerow(("".join(router_name),'voice_card',voice_card_a,voice_card_b,voice_card_k,voice_card_m))

                                 else:

                                    print("".join(router_name),"\t", 'voice_card',"\t",voice_card_a,"\t",voice_card_b)

                                    writer.writerow(("".join(router_name),'voice_card',voice_card_a,voice_card_b,'NA','NA'))

                                   

                            vtp = parse.find_lines("^vtp")  

                            

                            for vtp_a,vtp_b in enumerate(vtp):

                            #     print(a,b)       

                                 chld_vtp = parse.find_all_children(vtp_b)

                                 if len(chld_vtp) >=1 :

                                     for vtp_k,vtp_m in enumerate(chld_vtp):

                                         print( "".join(router_name),"\t", 'vtp',"\t",vtp_a,"\t",vtp_b,"\t",vtp_k,"\t",vtp_m)

                                         writer.writerow(("".join(router_name),'vtp',vtp_a,vtp_b,vtp_k,vtp_m))

                                 else:

                                    print("".join(router_name),"\t", 'vtp',"\t",vtp_a,"\t",vtp_b)

                                    writer.writerow(("".join(router_name),'vtp',vtp_a,vtp_b,'NA','NA'))

                                   

                            username = parse.find_lines("^username")  

                            

                            for username_a,username_b in enumerate(username):

                            #     print(a,b)       

                                 chld_username = parse.find_all_children(username_b)

                                 if len(chld_username) >=1 :

                                     for username_k,username_m in enumerate(chld_username):

                                         print( "".join(router_name),"\t", 'username',"\t",username_a,"\t",username_b,"\t",username_k,"\t",username_m)

                                         writer.writerow(("".join(router_name),'username',username_a,username_b,username_k,username_m))

                                 else:

                                    print("".join(router_name),"\t", 'username',"\t",username_a,"\t",username_b)

                                    writer.writerow(("".join(router_name),'username',username_a,username_b,'NA','NA'))

                                   

                            archive = parse.find_lines("^archive")  

                            

                            for archive_a,archive_b in enumerate(archive):

                            #     print(a,b)       

                                 chld_archive = parse.find_all_children(archive_b)

                                 if len(chld_archive) >=1 :

                                     for archive_k,archive_m in enumerate(chld_archive):

                                         print( "".join(router_name),"\t", 'archive',"\t",archive_a,"\t",archive_b,"\t",archive_k,"\t",archive_m)

                                         writer.writerow(("".join(router_name),'archive',archive_a,archive_b,archive_k,archive_m))

                                 else:

                                    print("".join(router_name),"\t", 'archive',"\t",archive_a,"\t",archive_b)

                                    writer.writerow(("".join(router_name),'archive',archive_a,archive_b,'NA','NA'))

                                   

                                    

                                    

                            class1 = parse.find_lines("^class")  

                            

                            for class_a,class_b in enumerate(class1):

                            #     print(a,b)       

                                 chld_class = parse.find_all_children(class_b)

                                 if len(chld_class) >=1 :

                                     for class_k,class_m in enumerate(chld_class):

                                         print( "".join(router_name),"\t", 'class',"\t",class_a,"\t",class_b,"\t",class_k,"\t",class_m)

                                         writer.writerow(("".join(router_name),'class',class_a,class_b,class_k,class_m))

                                 else:

                                    print("".join(router_name),"\t", 'class',"\t",class_a,"\t",class_b)

                                    writer.writerow(("".join(router_name),'class',class_a,class_b,'NA','NA'))

                                   

                                    

                                    

                            policy = parse.find_lines("^policy")  

                            

                            for policy_a,policy_b in enumerate(policy):

                            #     print(a,b)       

                                 chld_policy = parse.find_all_children(policy_b)

                                 if len(chld_policy) >=1 :

                                     for policy_k,policy_m in enumerate(chld_policy):

                                         print( "".join(router_name),"\t", 'policy',"\t",policy_a,"\t",policy_b,"\t",policy_k,"\t",policy_m)

                                         writer.writerow(("".join(router_name),'policy',policy_a,policy_b,policy_k,policy_m))

                                 else:

                                    print("".join(router_name),"\t", 'policy',"\t",policy_a,"\t",policy_b)

                                    writer.writerow(("".join(router_name),'policy',policy_a,policy_b,'NA','NA'))

                                    

                                    

                            interface = parse.find_lines("^interface")  

                            

                            for interface_a,interface_b in enumerate(interface):

                            #     print(a,b)       

                                 chld_interface = parse.find_all_children(interface_b)

                                 if len(chld_interface) >=1 :

                                     for interface_k,interface_m in enumerate(chld_interface):

                                         print( "".join(router_name),"\t", 'interface',"\t",interface_a,"\t",interface_b,"\t",interface_k,"\t",interface_m)

                                         writer.writerow(("".join(router_name),'interface',interface_a,interface_b,interface_k,interface_m))

                                 else:

                                    print("".join(router_name),"\t", 'interface',"\t",interface_a,"\t",interface_b)

                                    writer.writerow(("".join(router_name),'interface',interface_a,interface_b,'NA','NA'))

                                   

                                    

                            router1 = parse.find_lines("^router")  

                            

                            for router_a,router_b in enumerate(router1):

                            #     print(a,b)       

                                 chld_router = parse.find_all_children(router_b)

                                 if len(chld_router) >=1 :

                                     for router_k,router_m in enumerate(chld_router):

                                         print( "".join(router_name),"\t", 'router',"\t",router_a,"\t",router_b,"\t",router_k,"\t",router_m)

                                         writer.writerow(("".join(router_name),'router',router_a,router_b,router_k,router_m))

                                 else:

                                    print("".join(router_name),"\t", 'router',"\t",router_a,"\t",router_b)

                                    writer.writerow(("".join(router_name),'router',router_a,router_b,'NA','NA'))

                            

                                

                            address = parse.find_lines("^address")  

                            

                            for address_a,address_b in enumerate(address):

                            #     print(a,b)       

                                 chld_address = parse.find_all_children(address_b)

                                 if len(chld_address) >=1 :

                                     for address_k,address_m in enumerate(chld_address):

                                         print( "".join(router_name),"\t", 'address',"\t",address_a,"\t",address_b,"\t",address_k,"\t",address_m)

                                         writer.writerow(("".join(router_name),'address',address_a,address_b,address_k,address_m))

                                 else:

                                    print("".join(router_name),"\t", 'address',"\t",address_a,"\t",address_b)

                                    writer.writerow(("".join(router_name),'address',address_a,address_b,'NA','NA'))

                                   

                                    

                            # Return a list of all Permit access-list 23 permit

                            #==============================================================================

                            all_access_list = parse.find_lines("^access-list*") 

                            for a_all_access_list,b_all_access_list in enumerate(all_access_list):

                            #     print("".join(router_name),"\t","all_access_list","\t",a_all_access_list,"\t",b_all_access_list)

                                 try:

                                     chld_all_access_list = parse.find_all_children(b_all_access_list)

                                     if len(chld_all_access_list) >=1 :

                                         for access_k,access_m in enumerate(chld_all_access_list):

                                             print( "".join(router_name),"\t", 'all_access_list',"\t",a_all_access_list,"\t",b_all_access_list,"\t",access_k,"\t",access_m)

                                             writer.writerow(("".join(router_name),'all_access_list',a_all_access_list,b_all_access_list,access_k,access_m))

                                 except:

                                    print("".join(router_name),"\t","all_access_list","\t",a_all_access_list,"\t",b_all_access_list)

                                    writer.writerow(("".join(router_name),'all_access_list',a_all_access_list,b_all_access_list,'NA','NA'))

                                        

                                     

                            

                                   

                            route = parse.find_lines("^route")  

                            

                            for route_a,route_b in enumerate(route):

                            #     print(a,b)       

                                 chld_route = parse.find_all_children(route_b)

                                 if len(chld_route) >=1 :

                                     for route_k,route_m in enumerate(chld_route):

                                         print( "".join(router_name),"\t", 'route',"\t",route_a,"\t",route_b,"\t",route_k,"\t",route_m)

                                         writer.writerow(("".join(router_name),'route',route_a,route_b,route_k,route_m))

                                 else:

                                    print("".join(router_name),"\t", 'route',"\t",route_a,"\t",route_b)

                                    writer.writerow(("".join(router_name),'route',route_a,route_b,'NA','NA'))

                                     

                            snmp = parse.find_lines("^snmp")  

                            

                            for snmp_a,snmp_b in enumerate(snmp):

                            #     print(a,b)       

                                 chld_snmp = parse.find_all_children(snmp_b)

                                 if len(chld_snmp) >=1 :

                                     for snmp_k,snmp_m in enumerate(chld_snmp):

                                         print( "".join(router_name),"\t", 'snmp',"\t",snmp_a,"\t",snmp_b,"\t",snmp_k,"\t",snmp_m)

                                         writer.writerow(("".join(router_name),'snmp',snmp_a,snmp_b,snmp_k,snmp_m))

                                 else:

                                    print("".join(router_name),"\t", 'snmp',"\t",snmp_a,"\t",snmp_b)

                                    writer.writerow(("".join(router_name),'snmp',snmp_a,snmp_b,'NA','NA'))

                                   

                            tacacs = parse.find_lines("^tacacs")  

                            

                            for tacacs_a,tacacs_b in enumerate(tacacs):

                            #     print(a,b)       

                                 chld_tacacs = parse.find_all_children(tacacs_b)

                                 if len(chld_tacacs) >=1 :

                                     for tacacs_k,tacacs_m in enumerate(chld_tacacs):

                                         print( "".join(router_name),"\t", 'tacacs',"\t",tacacs_a,"\t",tacacs_b,"\t",tacacs_k,"\t",tacacs_m)

                                         writer.writerow(("".join(router_name),'tacacs',tacacs_a,tacacs_b,tacacs_k,tacacs_m))

                                 else:

                                    print("".join(router_name),"\t", 'tacacs',"\t",tacacs_a,"\t",tacacs_b)

                                    writer.writerow(("".join(router_name),'tacacs',tacacs_a,tacacs_b,'NA','NA'))

                                 

                            control = parse.find_lines("^control")  

                            

                            for control_a,control_b in enumerate(control):

                            #     print(a,b)       

                                 chld_control = parse.find_all_children(control_b)

                                 if len(chld_control) >=1 :

                                     for control_k,control_m in enumerate(chld_control):

                                         print( "".join(router_name),"\t", 'control',"\t",control_a,"\t",control_b,"\t",control_k,"\t",control_m)

                                         writer.writerow(("".join(router_name),'control',control_a,control_b,control_k,control_m))

                                 else:

                                    print("".join(router_name),"\t", 'control',"\t",control_a,"\t",control_b)

                                    writer.writerow(("".join(router_name),'control',control_a,control_b,'NA','NA'))

                                   

                            banner = parse.find_lines("^banner")  

                            

                            for banner_a,banner_b in enumerate(banner):

                            #     print(a,b)       

                                 chld_banner = parse.find_all_children(banner_b)

                                 if len(chld_banner) >=1 :

                                     for banner_k,banner_m in enumerate(chld_banner):

                                         print( "".join(router_name),"\t", 'banner',"\t",banner_a,"\t",banner_b,"\t",banner_k,"\t",banner_m)

                                         writer.writerow(("".join(router_name),'banner',banner_a,banner_b,banner_k,banner_m))

                                 else:

                                    print("".join(router_name),"\t", 'banner',"\t",banner_a,"\t",banner_b)

                                    writer.writerow(("".join(router_name),'banner',banner_a,banner_b,'NA','NA'))

                                   

                            line = parse.find_lines("^line")  

                            

                            for line_a,line_b in enumerate(line):

                            #     print(a,b)       

                                 chld_line = parse.find_all_children(line_b)

                                 if len(chld_line) >=1 :

                                     for line_k,line_m in enumerate(chld_line):

                                         print( "".join(router_name),"\t", 'line',"\t",line_a,"\t",line_b,"\t",line_k,"\t",line_m)

                                         writer.writerow(("".join(router_name),'line',line_a,line_b,line_k,line_m))

                                 else:

                                    print("".join(router_name),"\t", 'line',"\t",line_a,"\t",line_b)

                                    writer.writerow(("".join(router_name),'line',line_a,line_b,'NA','NA'))

                                 

                            scheduler = parse.find_lines("^scheduler")  

                            

                            for scheduler_a,scheduler_b in enumerate(scheduler):

                            #     print(a,b)       

                                 chld_scheduler = parse.find_all_children(scheduler_b)

                                 if len(chld_scheduler) >=1 :

                                     for scheduler_k,scheduler_m in enumerate(chld_scheduler):

                                         print( "".join(router_name),"\t", 'scheduler',"\t",scheduler_a,"\t",scheduler_b,"\t",scheduler_k,"\t",scheduler_m)

                                         writer.writerow(("".join(router_name),'scheduler',scheduler_a,scheduler_b,scheduler_k,scheduler_m))

                                 else:

                                    print("".join(router_name),"\t", 'scheduler',"\t",scheduler_a,"\t",scheduler_b)

                                    writer.writerow(("".join(router_name),'scheduler',scheduler_a,scheduler_b,'NA','NA'))

                                  

                                    

                            ntp = parse.find_lines("^ntp")  

                            

                            for ntp_a,ntp_b in enumerate(ntp):

                            #     print(a,b)       

                                 chld_ntp = parse.find_all_children(ntp_b)

                                 if len(chld_ntp) >=1 :

                                     for ntp_k,ntp_m in enumerate(chld_ntp):

                                         print( "".join(router_name),"\t", 'ntp',"\t",ntp_a,"\t",ntp_b,"\t",ntp_k,"\t",ntp_m)

                                         writer.writerow(("".join(router_name),'ntp',ntp_a,ntp_b,ntp_k,ntp_m))

                                 else:

                                    print("".join(router_name),"\t", 'ntp',"\t",ntp_a,"\t",ntp_b)

                                    writer.writerow(("".join(router_name),'ntp',ntp_a,ntp_b,'NA','NA'))

           

            

    out_file.close()

parse_cisco_files(Full_Path_File_Nmae,outdirname,csvfilename)

 
