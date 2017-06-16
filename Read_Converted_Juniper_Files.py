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

csvfilename="Juniper_test.csv"

dirname= "C:/ACL/Final/To_Process/"


 

def parse_cisco_files(Full_Path_File_Nmae,outdirname,csvfilename):

 

    with io.open(outdirname + "/" + csvfilename,'w',encoding='ascii',errors='replace') as out_file:  

            writer = csv.writer(out_file)

            writer.writerow(('Router_Name','Entry_Type','Entry_Type_Seq','Entry_Name','Child_Seq','Child_Name'))

            

            for path, dirs, files in os.walk(dirname):

 

                for filename in files:

                    if fnmatch.fnmatch(filename, '*.dat'):

                        cfg_file = os.path.abspath(os.path.join(path, filename))

#                        print("Parsing :", cfg_file)

                        f = open(cfg_file)

                        line = f.read()

                        first_line = line.split('\n', 1)[0]

                        if re.search('^!# Last commit:', first_line):

           

                #            parse = CiscoConfParse(Full_Path_File_Nmae)

                           

                            parse = CiscoConfParse(cfg_file)

                            

                    

                            print("Parsing :", cfg_file)

                   

                            router_name = parse.find_lines("host-name")

                           

                            # Return a list of all system         

                            system = parse.find_lines("^system")       

                            

                            for system_i,system_j in enumerate(system):

                               writer.writerow(("".join(router_name),'system',system_i,system_j,'NA','NA'))

                           

                            

                            internet = parse.find_lines("^    internet-options")       

                            

                            for internet_i,internet_j in enumerate(internet):

                                chld_internet = parse.find_all_children(internet_j)

                                if len(chld_internet) >=1 :

                                    for internet_k,internet_m in enumerate(chld_internet):

                                        writer.writerow(("".join(router_name),'internet',internet_i,internet_j,internet_k,internet_m))

                                else:

                                    writer.writerow(("".join(router_name),'internet',internet_i,internet_j,'NA','NA'))

                                   

                            ports = parse.find_lines("^    ports")       

 

                            for ports_i,ports_j in enumerate(ports):

                                chld_ports = parse.find_all_children(ports_j)

                                if len(chld_ports) >=1 :

                                    for ports_k,ports_m in enumerate(chld_ports):

                                        writer.writerow(("".join(router_name),'ports',ports_i,ports_j,ports_k,ports_m))

                                else:

                                    writer.writerow(("".join(router_name),'ports',ports_i,ports_j,'NA','NA'))

                           

                            ra = parse.find_lines("^    root-authentication")       

 

                            for ra_i,ra_j in enumerate(ra):

                                chld_ra = parse.find_all_children(ra_j)

                                if len(chld_ra) >=1 :

                                    for ra_k,ra_m in enumerate(chld_ports):

                                        writer.writerow(("".join(router_name),'root-authentication',ra_i,ra_j,ra_k,ra_m))

                                else:

                                    writer.writerow(("".join(router_name),'root-authentication',ra_i,ra_j,'NA','NA'))

                                   

                                    

                            ns = parse.find_lines("^    name-server")       

 

                            for ns_i,ns_j in enumerate(ns):

                                chld_ns = parse.find_all_children(ns_j)

                                if len(chld_ns) >=1 :

                                    for ns_k,ns_m in enumerate(chld_ns):

                                        writer.writerow(("".join(router_name),'name-server',ns_i,ns_j,ns_k,ns_m))

                                else:

                                    writer.writerow(("".join(router_name),'name-server',ns_i,ns_j,'NA','NA'))

                           

                            tac = parse.find_lines("^    tacplus")       

 

                            for tac_i,tac_j in enumerate(tac):

                                chld_tac = parse.find_all_children(tac_j)

                                if len(chld_tac) >=1 :

                                    for tac_k,tac_m in enumerate(chld_tac):

                                        writer.writerow(("".join(router_name),'tacplus',tac_i,tac_j,tac_k,tac_m))

                                else:

                                    writer.writerow(("".join(router_name),'tacplus',tac_i,tac_j,'NA','NA'))

                           

                            ro = parse.find_lines("^        retry-options ")       

 

                            for ro_i,ro_j in enumerate(ro):

                                chld_ro = parse.find_all_children(ro_j)

                                if len(chld_ro) >=1 :

                                    for ro_k,ro_m in enumerate(chld_ro):

                                        writer.writerow(("".join(router_name),'retry-options',ro_i,ro_j,ro_k,ro_m))

                                else:

                                    writer.writerow(("".join(router_name),'retry-options',ro_i,ro_j,'NA','NA'))

                                   

                            c = parse.find_lines("^        class")       

 

                            for c_i,c_j in enumerate(c):

                                chld_c = parse.find_all_children(c_j)

                                if len(chld_c) >=1 :

                                    for c_k,c_m in enumerate(chld_c):

                                        writer.writerow(("".join(router_name),'class',c_i,c_j,c_k,c_m))

                                else:

                                    writer.writerow(("".join(router_name),'class',c_i,c_j,'NA','NA'))

                                   

                            services = parse.find_lines("^    services")       

 

                            for services_i,services_j in enumerate(services):

                                chld_services = parse.find_all_children(services_j)

                                if len(chld_services) >=1 :

                                    for services_k,services_m in enumerate(chld_services):

                                        writer.writerow(("".join(router_name),'services',services_i,services_j,services_k,services_m))

                                else:

                                    writer.writerow(("".join(router_name),'services',services_i,services_j,'NA','NA'))

                                   

                            

                            host = parse.find_lines("^        host")       

 

                            for host_i,host_j in enumerate(host):

                                chld_host = parse.find_all_children(host_j)

                                if len(chld_host) >=1 :

                                    for host_k,host_m in enumerate(chld_host):

                                        writer.writerow(("".join(router_name),'host',host_i,host_j,host_k,host_m))

                                else:

                                    writer.writerow(("".join(router_name),'host',host_i,host_j,'NA','NA'))

                                   

                            sa = parse.find_lines("^        source-address")       

 

                            for sa_i,sa_j in enumerate(sa):

                                chld_sa = parse.find_all_children(sa_j)

                                if len(chld_sa) >=1 :

                                    for sa_k,sa_m in enumerate(chld_sa):

                                        writer.writerow(("".join(router_name),'source-address',sa_i,sa_j,sa_k,sa_m))

                                else:

                                    writer.writerow(("".join(router_name),'source-address',sa_i,sa_j,'NA','NA'))       

                            

                            processes = parse.find_lines("^    processes")       

 

                            for processes_i,processes_j in enumerate(processes):

                                chld_processes = parse.find_all_children(processes_j)

                                if len(chld_processes) >=1 :

                                    for processes_k,processes_m in enumerate(chld_processes):

                                        writer.writerow(("".join(router_name),'processes',processes_i,processes_j,processes_k,processes_m))

                                else:

                                    writer.writerow(("".join(router_name),'processes',processes_i,processes_j,'NA','NA'))

                                    

                            

                            ntp = parse.find_lines("^    ntp")       

 

                            for ntp_i,ntp_j in enumerate(ntp):

                                chld_ntp = parse.find_all_children(ntp_j)

                                if len(chld_ntp) >=1 :

                                    for ntp_k,ntp_m in enumerate(chld_ntp):

                                        writer.writerow(("".join(router_name),'ntp',ntp_i,ntp_j,ntp_k,ntp_m))

                                else:

                                    writer.writerow(("".join(router_name),'ntp',ntp_i,ntp_j,'NA','NA'))

                                    

                            chassis = parse.find_lines("^chassis")       

 

                            for chassis_i,chassis_j in enumerate(chassis):

                                chld_chassis = parse.find_all_children(chassis_j)

                                if len(chld_chassis) >=1 :

                                    for chassis_k,chassis_m in enumerate(chld_chassis):

                                        writer.writerow(("".join(router_name),'chassis',chassis_i,chassis_j,chassis_k,chassis_m))

                                else:

                                    writer.writerow(("".join(router_name),'chassis',chassis_i,chassis_j,'NA','NA'))

                            

                            

                            

                            

                                    

                            

                            

                            interfaces = parse.find_lines("^interfaces")       

                            

                            for interfaces_i,interfaces_j in enumerate(interfaces):

                                chld_interfaces = parse.find_all_children(interfaces_j)

                                if len(chld_interfaces) >=1 :

                                    for interfaces_k,interfaces_m in enumerate(chld_interfaces):

                                        writer.writerow(("".join(router_name),'interfaces',interfaces_i,interfaces_j,interfaces_k,interfaces_m))

                                else:

                                    writer.writerow(("".join(router_name),'interfaces',interfaces_i,interfaces_j,'NA','NA'))

                                   

                                    

                            snmp = parse.find_lines("^snmp")       

 

                            for snmp_i,snmp_j in enumerate(snmp):

                                chld_snmp = parse.find_all_children(snmp_j)

                                if len(chld_snmp) >=1 :

                                    for snmp_k,snmp_m in enumerate(chld_snmp):

                                        writer.writerow(("".join(router_name),'snmp',chassis_i,chassis_j,chassis_k,chassis_m))

                                else:

                                    writer.writerow(("".join(router_name),'snmp',chassis_i,chassis_j,'NA','NA'))

                                    

                                    

                            fo = parse.find_lines("^forwarding-options")       

 

                            for fo_i,fo_j in enumerate(fo):

                                chld_fo = parse.find_all_children(fo_j)

                                if len(chld_fo) >=1 :

                                    for fo_k,fo_m in enumerate(chld_fo):

                                        writer.writerow(("".join(router_name),'forwarding-options',fo_i,fo_j,fo_k,fo_m))

                                else:

                                    writer.writerow(("".join(router_name),'forwarding-options',fo_i,fo_j,'NA','NA'))

                                   

                                    

                            eo = parse.find_lines("^event-options")       

 

                            for eo_i,eo_j in enumerate(eo):

                                chld_eo = parse.find_all_children(eo_j)

                                if len(chld_eo) >=1 :

                                    for eo_k,eo_m in enumerate(chld_eo):

                                        writer.writerow(("".join(router_name),'event-options',eo_i,eo_j,eo_k,eo_m))

                                else:

                                    writer.writerow(("".join(router_name),'event-options',eo_i,eo_j,'NA','NA'))

                                           

                            routopt = parse.find_lines("^routing-options")       

 

                            for routopt_i,routopt_j in enumerate(routopt):

                                chld_routopt = parse.find_all_children(routopt_j)

                                if len(chld_routopt) >=1 :

                                    for routopt_k,routopt_m in enumerate(chld_routopt):

                                        writer.writerow(("".join(router_name),'routing-options',routopt_i,routopt_j,routopt_k,routopt_m))

                                else:

                                    writer.writerow(("".join(router_name),'routing-options',routopt_i,routopt_j,'NA','NA'))      

                                    

                                     

                                    

                            protocols = parse.find_lines("^protocols")       

 

                            for protocols_i,protocols_j in enumerate(protocols):

                                chld_protocols = parse.find_all_children(protocols_j)

                                if len(chld_protocols) >=1 :

                                    for protocols_k,protocols_m in enumerate(chld_protocols):

                                        writer.writerow(("".join(router_name),'protocols',protocols_i,protocols_j,protocols_k,protocols_m))

                                else:

                                    writer.writerow(("".join(router_name),'protocols',protocols_i,protocols_j,'NA','NA'))

                                   

                                    

                                    

                            igmp = parse.find_lines("^    igmp")       

 

                            for igmp_i,igmp_j in enumerate(igmp):

                                chld_igmp = parse.find_all_children(igmp_j)

                                if len(chld_igmp) >=1 :

                                    for igmp_k,igmp_m in enumerate(chld_igmp):

                                        writer.writerow(("".join(router_name),'igmp',igmp_i,igmp_j,igmp_k,igmp_m))

                                else:

                                    writer.writerow(("".join(router_name),'igmp',igmp_i,igmp_j,'NA','NA'))

                            

                            

                            ospf = parse.find_lines("^    ospf")       

 

                            for ospf_i,ospf_j in enumerate(ospf):

                                chld_ospf = parse.find_all_children(ospf_j)

                                if len(chld_ospf) >=1 :

                                    for ospf_k,ospf_m in enumerate(chld_ospf):

                                        writer.writerow(("".join(router_name),'ospf',ospf_i,ospf_j,ospf_k,ospf_m))

                                else:

                                    writer.writerow(("".join(router_name),'ospf',ospf_i,ospf_j,'NA','NA'))

                           

                            

                            

                            

                            pim = parse.find_lines("^    pim")       

 

                            for pim_i,pim_j in enumerate(pim):

                                chld_pim = parse.find_all_children(pim_j)

                                if len(chld_pim) >=1 :

                                    for pim_k,pim_m in enumerate(chld_pim):

                                        writer.writerow(("".join(router_name),'pim',pim_i,pim_j,pim_k,pim_m))

                                else:

                                    writer.writerow(("".join(router_name),'pim',pim_i,pim_j,'NA','NA'))

                                   

                            lldp = parse.find_lines("^    lldp")       

 

                            for lldp_i,lldp_j in enumerate(lldp):

                                chld_lldp = parse.find_all_children(lldp_j)

                                if len(chld_lldp) >=1 :

                                    for lldp_k,lldp_m in enumerate(chld_lldp):

                                        writer.writerow(("".join(router_name),'lldp',lldp_i,lldp_j,lldp_k,lldp_m))

                                else:

                                    writer.writerow(("".join(router_name),'lldp',lldp_i,lldp_j,'NA','NA'))

                                    

                                    

                            pol_opt = parse.find_lines("^policy-options")       

 

                            for pol_opt_i,pol_opt_j in enumerate(pol_opt):

                                chld_pol_opt = parse.find_all_children(pol_opt_j)

                                if len(chld_pol_opt) >=1 :

                                    for pol_opt_k,pol_opt_m in enumerate(chld_pol_opt):

                                        writer.writerow(("".join(router_name),'policy-options',pol_opt_i,pol_opt_j,pol_opt_k,pol_opt_m))

                                else:

                                    writer.writerow(("".join(router_name),'policy-options',pol_opt_i,pol_opt_j,'NA','NA'))

                                   

                                    

                            prefi_list = parse.find_lines("^    prefix-list")       

 

                            for prefi_list_i,prefi_list_j in enumerate(prefi_list):

                                chld_prefi_list = parse.find_all_children(prefi_list_j)

                                if len(chld_prefi_list) >=1 :

                                    for prefi_list_k,prefi_list_m in enumerate(chld_prefi_list):

                                        writer.writerow(("".join(router_name),'prefix-list',prefi_list_i,prefi_list_j,prefi_list_k,prefi_list_m))

                                else:

                                    writer.writerow(("".join(router_name),'prefix-list',prefi_list_i,prefi_list_j,'NA','NA'))

                                   

                            

                            

                            cls_of_serv = parse.find_lines("^class-of-service")       

 

                            for cls_of_serv_i,cls_of_serv_j in enumerate(cls_of_serv):

                                chld_cls_of_serv = parse.find_all_children(cls_of_serv_j)

                                if len(chld_cls_of_serv) >=1 :

                                    for cls_of_serv_k,cls_of_serv_m in enumerate(chld_cls_of_serv):

                                        writer.writerow(("".join(router_name),'class-of-service',cls_of_serv_i,cls_of_serv_j,cls_of_serv_k,cls_of_serv_m))

                                else:

                                    writer.writerow(("".join(router_name),'class-of-service',cls_of_serv_i,cls_of_serv_j,'NA','NA'))

                                   

                                    

                                    

                            classifiers = parse.find_lines("^    classifiers")       

 

                            for classifiers_i,classifiers_j in enumerate(classifiers):

                                chld_classifiers = parse.find_all_children(classifiers_j)

                                if len(chld_classifiers) >=1 :

                                    for classifiers_k,classifiers_m in enumerate(chld_classifiers):

                                        writer.writerow(("".join(router_name),'classifiers',classifiers_i,classifiers_j,classifiers_k,classifiers_m))

                                else:

                                    writer.writerow(("".join(router_name),'classifiers',classifiers_i,classifiers_j,'NA','NA'))

                                   

                                    

                            forwarding = parse.find_lines("^    forwarding")       

 

                            for forwarding_i,forwarding_j in enumerate(forwarding):

                                chld_forwarding = parse.find_all_children(forwarding_j)

                                if len(chld_forwarding) >=1 :

                                    for forwarding_k,forwarding_m in enumerate(chld_forwarding):

                                        writer.writerow(("".join(router_name),'forwarding',forwarding_i,forwarding_j,forwarding_k,forwarding_m))

                                else:

                                    writer.writerow(("".join(router_name),'forwarding',forwarding_i,forwarding_j,'NA','NA'))

                                    

                            intf = parse.find_lines("^    interfaces")       

 

                            for intf_i,intf_j in enumerate(intf):

                                chld_intf = parse.find_all_children(intf_j)

                                if len(chld_intf) >=1 :

                                    for intf_k,intf_m in enumerate(chld_intf):

                                        writer.writerow(("".join(router_name),'interfaces Class service',intf_i,intf_j,intf_k,intf_m))

                                else:

                                    writer.writerow(("".join(router_name),'interfaces Class service',intf_i,intf_j,'NA','NA'))

                                   

                                    

                            rewrite = parse.find_lines("^    rewrite")       

 

                            for rewrite_i,rewrite_j in enumerate(rewrite):

                                chld_rewrite = parse.find_all_children(rewrite_j)

                                if len(chld_rewrite) >=1 :

                                    for rewrite_k,rewrite_m in enumerate(chld_rewrite):

                                        writer.writerow(("".join(router_name),'rewrite',rewrite_i,rewrite_j,rewrite_k,rewrite_m))

                               else:

                                    writer.writerow(("".join(router_name),'rewrite',rewrite_i,rewrite_j,'NA','NA'))

                                   

                            scheduler = parse.find_lines("^    scheduler")       

 

                            for scheduler_i,scheduler_j in enumerate(scheduler):

                                chld_scheduler = parse.find_all_children(scheduler_j)

                                if len(chld_scheduler) >=1 :

                                    for scheduler_k,scheduler_m in enumerate(chld_scheduler):

                                        writer.writerow(("".join(router_name),'scheduler',scheduler_i,scheduler_j,scheduler_k,scheduler_m))

                                else:

                                    writer.writerow(("".join(router_name),'scheduler',scheduler_i,scheduler_j,'NA','NA'))

                                   

                           
                                   

                                    

                            firewall = parse.find_lines("^firewall")       

 

                            for firewall_i,firewall_j in enumerate(firewall):

                               chld_firewall = parse.find_all_children(firewall_j)

                                if len(chld_firewall) >=1 :

                                    for firewall_k,firewall_m in enumerate(chld_firewall):

                                        writer.writerow(("".join(router_name),'firewall',firewall_i,firewall_j,firewall_k,firewall_m))

                                else:

                                    writer.writerow(("".join(router_name),'firewall',firewall_i,firewall_j,'NA','NA'))   

                                    

                                    

                            family = parse.find_lines("^    family")       

 

                            for family_i,family_j in enumerate(family):

                                chld_family = parse.find_all_children(family_j)

                                if len(chld_family) >=1 :

                                    for family_k,family_m in enumerate(chld_family):

                                        writer.writerow(("".join(router_name),'family',family_i,family_j,family_k,family_m))

                                else:

                                    writer.writerow(("".join(router_name),'family',family_i,family_j,'NA','NA'))

                           

                            filters = parse.find_lines("        filter")       

 

                            for filters_i,filters_j in enumerate(filters):

                                chld_filters = parse.find_all_children(filters_j)

                                if len(chld_filters) >=1 :

                                    for filters_k,filters_m in enumerate(chld_filters):

                                        writer.writerow(("".join(router_name),'filter',filters_i,filters_j,filters_k,filters_m))

                                else:

                                    writer.writerow(("".join(router_name),'filter',filters_i,filters_j,'NA','NA'))

                                   

                                    

                                    

                                    

                            term = parse.find_lines("^            term")       

 

                            for term_i,term_j in enumerate(term):

                                chld_term = parse.find_all_children(term_j)

                                if len(chld_term) >=1 :

                                    for term_k,term_m in enumerate(chld_term):

                                        writer.writerow(("".join(router_name),'term',term_i,term_j,term_k,term_m))

                                else:

                                    writer.writerow(("".join(router_name),'term',term_i,term_j,'NA','NA'))

                                   

                            switch = parse.find_lines("^switch")       

 

                            for switch_i,switch_j in enumerate(switch):

                                chld_switch = parse.find_all_children(switch_j)

                                if len(chld_switch) >=1 :

                                    for switch_k,switch_m in enumerate(chld_switch):

                                        writer.writerow(("".join(router_name),'switch-options',switch_i,switch_j,switch_k,switch_m))

                                else:

                                    writer.writerow(("".join(router_name),'switch-options',switch_i,switch_j,'NA','NA'))

                                   

                            virtual = parse.find_lines("^virtual")       

 

                            for virtual_i,virtual_j in enumerate(virtual):

                                chld_virtual = parse.find_all_children(virtual_j)

                                if len(chld_virtual) >=1 :

                                    for virtual_k,virtual_m in enumerate(chld_virtual):

                                        writer.writerow(("".join(router_name),'virtual-chassis',virtual_i,virtual_j,virtual_k,virtual_m))

                                else:

                                    writer.writerow(("".join(router_name),'virtual-chassis',virtual_i,virtual_j,'NA','NA'))

                                   

                            member = parse.find_lines("^    member")       

 

                            for member_i,member_j in enumerate(member):

                                chld_member = parse.find_all_children(member_j)

                                if len(chld_member) >=1 :

                                    for member_k,member_m in enumerate(chld_member):

                                        writer.writerow(("".join(router_name),'virtual-chassis member',member_i,member_j,member_k,member_m))

                                else:

                                    writer.writerow(("".join(router_name),'virtual-chassis member',member_i,member_j,'NA','NA'))       

                                    

                            vlans = parse.find_lines("^vlans")       

 

                            for vlans_i,vlans_j in enumerate(vlans):

                                chld_vlans = parse.find_all_children(vlans_j)

                                if len(chld_vlans) >=1 :

                                    for vlans_k,vlans_m in enumerate(chld_vlans):

                                        writer.writerow(("".join(router_name),'vlans',vlans_i,vlans_j,vlans_k,vlans_m))

                                else:

                                    writer.writerow(("".join(router_name),'vlans',vlans_i,vlans_j,'NA','NA'))

                                   

                            DATA = parse.find_lines("^    DATA")       

 

                            for DATA_i,DATA_j in enumerate(DATA):

                                chld_DATA = parse.find_all_children(DATA_j)

                                if len(chld_DATA) >=1 :

                                    for DATA_k,DATA_m in enumerate(chld_DATA):

                                        writer.writerow(("".join(router_name),'vlans DATA',DATA_i,DATA_j,DATA_k,DATA_m))

                                else:

                                    writer.writerow(("".join(router_name),'vlans DATA',DATA_i,DATA_j,'NA','NA'))

                                    

                                    

                            DEADZONE = parse.find_lines("^    DEADZONE")       

                            for DEADZONE_i,DEADZONE_j in enumerate(DEADZONE):

                                chld_DEADZONE = parse.find_all_children(DEADZONE_j)

                                if len(chld_DEADZONE) >=1 :

                                    for DEADZONE_k,DEADZONE_m in enumerate(chld_DEADZONE):

                                        writer.writerow(("".join(router_name),'vlans DEADZONE',DEADZONE_i,DEADZONE_j,DEADZONE_k,DEADZONE_m))

                                else:

                                    writer.writerow(("".join(router_name),'vlans DEADZONE',DEADZONE_i,DEADZONE_j,'NA','NA'))

                                    

                            DOA = parse.find_lines("^    DOA")       

                            for DOA_i,DOA_j in enumerate(DOA):

                                chld_DOA = parse.find_all_children(DOA_j)

                                if len(chld_DOA) >=1 :

                                    for DOA_k,DOA_m in enumerate(chld_DOA):

                                        writer.writerow(("".join(router_name),'vlans DOA-PIV ',DOA_i,DOA_j,DOA_k,DOA_m))

                                else:

                                    writer.writerow(("".join(router_name),'vlans DOA-PIV ',DOA_i,DOA_j,'NA','NA'))

                            

                            INTERNET = parse.find_lines("^    INTERNET")       

                            for INTERNET_i,INTERNET_j in enumerate(INTERNET):

                                chld_INTERNET = parse.find_all_children(INTERNET_j)

                                if len(chld_INTERNET) >=1 :

                                    for INTERNET_k,INTERNET_m in enumerate(chld_INTERNET):

                                        writer.writerow(("".join(router_name),'vlans INTERNET-ONLY',INTERNET_i,INTERNET_j,INTERNET_k,INTERNET_m))

                                else:

                                    writer.writerow(("".join(router_name),'vlans INTERNET-ONLY',INTERNET_i,INTERNET_j,'NA','NA')) 

                                    

                            VOIP1 = parse.find_lines("^    VOIP")       

                            for VOIP1_i,VOIP1_j in enumerate(VOIP1):

                                chld_VOIP1 = parse.find_all_children(VOIP1_j)

                                if len(chld_VOIP1) >=1 :

                                    for VOIP1_k,VOIP1_m in enumerate(chld_VOIP1):

                                        writer.writerow(("".join(router_name),'vlans VOIP',VOIP1_i,VOIP1_j,VOIP1_k,VOIP1_m))

                                else:

                                    writer.writerow(("".join(router_name),'vlans VOIP',VOIP1_i,VOIP1_j,'NA','NA'))

                                    

                            poe = parse.find_lines("^poe")       

                            for poe_i,poe_j in enumerate(poe):

                                chld_poe = parse.find_all_children(poe_j)

                                if len(chld_poe) >=1 :

                                    for poe_k,poe_m in enumerate(chld_poe):

                                        writer.writerow(("".join(router_name),'poe',poe_i,poe_j,poe_k,poe_m))

                                else:

                                    writer.writerow(("".join(router_name),'vlans DEADZONE',poe_i,poe_j,'NA','NA'))

                                    

                            """  

                            ############################  OLD  ##########################

                            """        

                                    

#                            writer.writerow(("".join(router_name),'service','Test','Test','NA','NA'))

                   

                            #Return a list of all Header   

                            service = parse.find_lines("^service")     

                            boot = parse.find_lines("^boot") 

                            security = parse.find_lines("^security")

                            logging = parse.find_lines("^logging")

                            no = parse.find_lines("^no")

                            

                            print("\n")

                            for service_i,service_j in enumerate(service):

#                                print("".join(router_name),"\t",'service',"\t" ,service_i,"\t",service_j)

                                writer.writerow(("".join(router_name),'service',service_i,service_j,'NA','NA'))

                            

                            

                            for boot_i,boot_j in enumerate(boot):

#                                print("".join(router_name),"\t", 'boot',"\t",boot_i,"\t",boot_j)

                                writer.writerow(("".join(router_name),'boot',boot_i,boot_j,'NA','NA'))

                             

                            for security_i,security_j in enumerate(security):

#                                print("".join(router_name),"\t", 'security',"\t",security_i,"\t",security_j)

                                writer.writerow(("".join(router_name),'security',security_i,security_j,'NA','NA'))

                                

                            for logging_i,logging_j in enumerate(logging):

#                                print("".join(router_name),"\t", 'logging',"\t",logging_i,"\t",logging_j)   

                                writer.writerow(("".join(router_name),'logging',logging_i,logging_j,'NA','NA'))

                            

                            for no_i,no_j in enumerate(no):

#                                print("".join(router_name),"\t", 'no',"\t",no_i,"\t",no_j)

                                writer.writerow(("".join(router_name),'no',no_i,no_j,'NA','NA'))

                            

                            cfs  = parse.find_lines("^cfs") 

                            for cfs_i,cfs_j in enumerate(cfs):

#                                print("".join(router_name),"\t", 'cfs',"\t",cfs_i,"\t",cfs_j)

                                writer.writerow(("".join(router_name),'cfs',cfs_i,cfs_j,'NA','NA'))

                           

                            

                            

                            # Return a list of all vdc         

                            vdc = parse.find_lines("^vdc")       

                            

                            for vdc_i,vdc_j in enumerate(vdc):

                                chld_vdc = parse.find_all_children(vdc_j)

                                if len(chld_vdc) >=1 :

                                    for vdc_k,vdc_m in enumerate(chld_vdc):

                                        writer.writerow(("".join(router_name),'vdc',vdc_i,vdc_j,vdc_k,vdc_m))

                                else:

                                    writer.writerow(("".join(router_name),'vdc',vdc_i,vdc_j,'NA','NA'))

                                   

                            

                            # Return a list of all feature    

                            feature = parse.find_lines("^feature")       

                            

                            for feature_i,feature_j in enumerate(feature):

                                chld_feature = parse.find_all_children(feature_j)

                                if len(chld_feature) >=1 :

                                    for feature_k,feature_m in enumerate(chld_feature):

                                        writer.writerow(("".join(router_name),'feature',feature_i,feature_j,feature_k,feature_m))

                                else:

                                    writer.writerow(("".join(router_name),'feature',feature_i,feature_j,'NA','NA'))

#                                   

#                           

                            # Return a list of all diagnostic         

                            diagnostic = parse.find_lines("^diagnostic")       

                            

                            for diagnostic_i,diagnostic_j in enumerate(diagnostic):

                            #    print("\n", i,"\t",j)

                                chld_diagnostic = parse.find_all_children(diagnostic_j)

                            #    print(len(chld))

                                if len(chld_diagnostic) >=1 :

                                    for diagnostic_k,diagnostic_m in enumerate(chld_diagnostic):

                                        writer.writerow(("".join(router_name),'diagnostic',diagnostic_i,diagnostic_j,diagnostic_k,diagnostic_m))

                                else:

                                    writer.writerow(("".join(router_name),'diagnostic',diagnostic_i,diagnostic_j,'NA','NA'))

#                           

                            # Return a list of all copp       

                            copp = parse.find_lines("^copp")       

                            

                            for copp_i,copp_j in enumerate(copp):

                            #    print("\n", i,"\t",j)

                                chld_copp = parse.find_all_children(copp_j)

                            #    print(len(chld))

                                if len(chld_copp) >=1 :

                                    for copp_k,copp_m in enumerate(chld_copp):

                                        writer.writerow(("".join(router_name),'copp',copp_i,copp_j,copp_k,copp_m))

                                else:

                                    writer.writerow(("".join(router_name),'copp',copp_i,copp_j,'NA','NA'))

#                           

                            # Return a list of all  vrf       

                            vrf = parse.find_lines("^vrf")       

                            

                            for vrf_i,vrf_j in enumerate(vrf):

                                chld_vrf = parse.find_all_children(vrf_j)

                                if len(chld_vrf) >=1 :

                                    for vrf_k,vrf_m in enumerate(chld_vrf):

                                        writer.writerow(("".join(router_name),'vrf',vrf_i,vrf_j,vrf_k,vrf_m))

                                else:

                                    writer.writerow(("".join(router_name),'vrf',vrf_i,vrf_j,'NA','NA'))

#                           

#                            

                            # Return a list of all policy accounting and subinterfaces         

                            aaa = parse.find_lines("^aaa")       

                            

                            for aaa_i,aaa_j in enumerate(aaa):

                            #    print("\n", i,"\t",j)

                                chld_aaa = parse.find_all_children(aaa_j)

                            #    print(len(chld))

                                if len(chld_aaa) >=1 :

                                    for aaa_k,aaa_m in enumerate(chld_aaa):

#                                        print( "".join(router_name),"\t", 'aaa',"\t",aaa_i,"\t",aaa_j,"\t",aaa_k,"\t",aaa_m)

                                        writer.writerow(("".join(router_name),'no',aaa_i,aaa_j,aaa_k,aaa_m))

                                else:

#                                    print( "".join(router_name),"\t", 'aaa',"\t",aaa_i,"\t",aaa_j)

                                    writer.writerow(("".join(router_name),'aaa',aaa_i,aaa_j,'NA','NA'))

#                           

#                           

                            # Return a list of all clock         

                            clock = parse.find_lines("^clock")       

                            

                            for clock_i,clock_j in enumerate(clock):

                            #    print("\n", i,"\t",j)

                                chld_clock = parse.find_all_children(clock_j)

                            #    print(len(chld))

                                if len(chld_clock) >=1 :

                                    for clock_k,clock_m in enumerate(chld_clock):

#                                        print( "".join(router_name),"\t", 'clock',"\t",clock_i,"\t",clock_j,"\t",clock_k,"\t",clock_m)

                                        writer.writerow(("".join(router_name),'clock',clock_i,clock_j,clock_k,clock_m))

                                else:

#                                    print( "".join(router_name),"\t", 'clock',"\t",clock_i,"\t",clock_j)

                                    

                                    writer.writerow(("".join(router_name),'clock',clock_i,clock_j,'NA','NA'))

                           

                            

                            # Return a list of all dot         

                            dot = parse.find_lines("^dot")       

                            

                            for dot_i,dot_j in enumerate(dot):

                            #    print("\n", i,"\t",j)

                                chld_dot = parse.find_all_children(dot_j)

                            #    print(len(chld))

                                if len(chld_dot) >=1 :

                                    for dot_k,dot_m in enumerate(chld_dot):

#                                        print( "".join(router_name),"\t", 'dot',"\t",dot_i,"\t",dot_j,"\t",dot_k,"\t",dot_m)

                                        writer.writerow(("".join(router_name),'dot',dot_i,dot_j,dot_k,dot_m))

                                else:

#                                    print( "".join(router_name),"\t", 'dot',"\t",dot_i,"\t",dot_j)

                                    writer.writerow(("".join(router_name),'dot',dot_i,dot_j,'NA','NA'))

#                           

                            

                            # Return a list of all ip         

                            ip1 = parse.find_lines("^ip ")  

                            

                            for ip1_a,ip1_b in enumerate(ip1):

                            #     print(a,b)       

                                 chld_ip = parse.find_all_children(ip1_b)

                                 if len(chld_ip) >=1 :

                                     for ip1_k,ip1_m in enumerate(chld_ip):

#                                         print( "".join(router_name),"\t", 'ip',"\t",ip1_a,"\t",ip1_b,"\t",ip1_k,"\t",ip1_m)

                                         writer.writerow(("".join(router_name),'ip',ip1_a,ip1_b,ip1_k,ip1_m))

                                 else:

#                                    print("".join(router_name),"\t", 'ip',"\t",ip1_a,"\t",ip1_b)

                                    writer.writerow(("".join(router_name),'ip',ip1_a,ip1_b,'NA','NA'))

#                           

#                           

#                           

                            # Return a list of all multilink         

                            multilink = parse.find_lines("^multilink")  

                            

                            for multilink_a,multilink_b in enumerate(multilink):

                            #     print(a,b)       

                                 chld_multilink = parse.find_all_children(multilink_b)

                                 if len(chld_multilink) >=1 :

                                     for multilink_k,multilink_m in enumerate(chld_ip):

#                                         print( "".join(router_name),"\t", 'multilink',"\t",multilink_a,"\t",multilink_b,"\t",multilink_k,"\t",multilink_m)

                                         writer.writerow(("".join(router_name),'multilink',multilink_a,multilink_b,multilink_k,multilink_m))

                                 else:

#                                    print("".join(router_name),"\t", 'multilink',"\t",multilink_a,"\t",multilink_b)

                                    writer.writerow(("".join(router_name),'multilink',multilink_a,multilink_b,'NA','NA'))

                           

#                                    

                            voice_card = parse.find_lines("^voice-card")  

                            

                            for voice_card_a,voice_card_b in enumerate(voice_card):

                            #     print(a,b)        

                                 chld_voice_card = parse.find_all_children(voice_card_b)

                                 if len(chld_voice_card) >=1 :

                                     for voice_card_k,voice_card_m in enumerate(chld_voice_card):

#                                         print( "".join(router_name),"\t", 'voice_card',"\t",voice_card_a,"\t",voice_card_b,"\t",voice_card_k,"\t",voice_card_m)

                                         writer.writerow(("".join(router_name),'voice_card',voice_card_a,voice_card_b,voice_card_k,voice_card_m))

                                 else:

#                                    print("".join(router_name),"\t", 'voice_card',"\t",voice_card_a,"\t",voice_card_b)

                                    writer.writerow(("".join(router_name),'voice_card',voice_card_a,voice_card_b,'NA','NA'))

#                                   

                            vtp = parse.find_lines("^vtp")  

                            

                            for vtp_a,vtp_b in enumerate(vtp):

                            #     print(a,b)       

                                 chld_vtp = parse.find_all_children(vtp_b)

                                 if len(chld_vtp) >=1 :

                                     for vtp_k,vtp_m in enumerate(chld_vtp):

#                                         print( "".join(router_name),"\t", 'vtp',"\t",vtp_a,"\t",vtp_b,"\t",vtp_k,"\t",vtp_m)

                                         writer.writerow(("".join(router_name),'vtp',vtp_a,vtp_b,vtp_k,vtp_m))

                                 else:

#                                    print("".join(router_name),"\t", 'vtp',"\t",vtp_a,"\t",vtp_b)

                                    writer.writerow(("".join(router_name),'vtp',vtp_a,vtp_b,'NA','NA'))

#                                   

                            username = parse.find_lines("^username")  

                            

                            for username_a,username_b in enumerate(username):

                            #     print(a,b)       

                                 chld_username = parse.find_all_children(username_b)

                                 if len(chld_username) >=1 :

                                     for username_k,username_m in enumerate(chld_username):

#                                         print( "".join(router_name),"\t", 'username',"\t",username_a,"\t",username_b,"\t",username_k,"\t",username_m)

                                         writer.writerow(("".join(router_name),'username',username_a,username_b,username_k,username_m))

                                 else:

#                                    print("".join(router_name),"\t", 'username',"\t",username_a,"\t",username_b)

                                    writer.writerow(("".join(router_name),'username',username_a,username_b,'NA','NA'))

#                                   

                            archive = parse.find_lines("^archive")  

                            

                            for archive_a,archive_b in enumerate(archive):

                            #     print(a,b)       

                                 chld_archive = parse.find_all_children(archive_b)

                                 if len(chld_archive) >=1 :

                                     for archive_k,archive_m in enumerate(chld_archive):

#                                         print( "".join(router_name),"\t", 'archive',"\t",archive_a,"\t",archive_b,"\t",archive_k,"\t",archive_m)

                                         writer.writerow(("".join(router_name),'archive',archive_a,archive_b,archive_k,archive_m))

                                 else:

#                                    print("".join(router_name),"\t", 'archive',"\t",archive_a,"\t",archive_b)

                                    writer.writerow(("".join(router_name),'archive',archive_a,archive_b,'NA','NA'))

#                                   

#                                   

#                                   

                            class1 = parse.find_lines("^class")  

                            

                            for class_a,class_b in enumerate(class1):

                            #     print(a,b)       

                                 chld_class = parse.find_all_children(class_b)

                                 if len(chld_class) >=1 :

                                     for class_k,class_m in enumerate(chld_class):

                                         #print( "".join(router_name),"\t", 'class',"\t",class_a,"\t",class_b,"\t",class_k,"\t",class_m)

                                         writer.writerow(("".join(router_name),'class',class_a,class_b,class_k,class_m))

                                 else:

                                    #print("".join(router_name),"\t", 'class',"\t",class_a,"\t",class_b)

                                    writer.writerow(("".join(router_name),'class',class_a,class_b,'NA','NA'))

#                                   

#                                   

                                    

                            policy = parse.find_lines("^policy")  

                            

                            for policy_a,policy_b in enumerate(policy):

                            #     print(a,b)       

                                 chld_policy = parse.find_all_children(policy_b)

                                 if len(chld_policy) >=1 :

                                     for policy_k,policy_m in enumerate(chld_policy):

                                        #print( "".join(router_name),"\t", 'policy',"\t",policy_a,"\t",policy_b,"\t",policy_k,"\t",policy_m)

                                         writer.writerow(("".join(router_name),'policy',policy_a,policy_b,policy_k,policy_m))

                                 else:

                                    #print("".join(router_name),"\t", 'policy',"\t",policy_a,"\t",policy_b)

                                    writer.writerow(("".join(router_name),'policy',policy_a,policy_b,'NA','NA'))

                                    

#                                   

                            interface = parse.find_lines("^interface")  

                            

                            for interface_a,interface_b in enumerate(interface):

                            #     print(a,b)       

                                 chld_interface = parse.find_all_children(interface_b)

                                 if len(chld_interface) >=1 :

                                     for interface_k,interface_m in enumerate(chld_interface):

                                        # print( "".join(router_name),"\t", 'interface',"\t",interface_a,"\t",interface_b,"\t",interface_k,"\t",interface_m)

                                         writer.writerow(("".join(router_name),'interface',interface_a,interface_b,interface_k,interface_m))

                                 else:

                                   # print("".join(router_name),"\t", 'interface',"\t",interface_a,"\t",interface_b)

                                    writer.writerow(("".join(router_name),'interface',interface_a,interface_b,'NA','NA'))

#                                   

#                                   

                            router1 = parse.find_lines("^router")  

                            

                            for router_a,router_b in enumerate(router1):

                            #     print(a,b)       

                                 chld_router = parse.find_all_children(router_b)

                                 if len(chld_router) >=1 :

                                     for router_k,router_m in enumerate(chld_router):

                                         #print( "".join(router_name),"\t", 'router',"\t",router_a,"\t",router_b,"\t",router_k,"\t",router_m)

                                         writer.writerow(("".join(router_name),'router',router_a,router_b,router_k,router_m))

                                 else:

                                    #print("".join(router_name),"\t", 'router',"\t",router_a,"\t",router_b)

                                    writer.writerow(("".join(router_name),'router',router_a,router_b,'NA','NA'))

#                            

                                

                            address = parse.find_lines("^address")  

                            

                            for address_a,address_b in enumerate(address):

                            #     print(a,b)       

                                 chld_address = parse.find_all_children(address_b)

                                 if len(chld_address) >=1 :

                                     for address_k,address_m in enumerate(chld_address):

                                         #print( "".join(router_name),"\t", 'address',"\t",address_a,"\t",address_b,"\t",address_k,"\t",address_m)

                                         writer.writerow(("".join(router_name),'address',address_a,address_b,address_k,address_m))

                                 else:

                                   # print("".join(router_name),"\t", 'address',"\t",address_a,"\t",address_b)

                                    writer.writerow(("".join(router_name),'address',address_a,address_b,'NA','NA'))

                                   

#                                    

                            # Return a list of all Permit access-list 23 permit

                            #==============================================================================

                            all_access_list = parse.find_lines("^access-list*") 

                            for a_all_access_list,b_all_access_list in enumerate(all_access_list):

                            #     print("".join(router_name),"\t","all_access_list","\t",a_all_access_list,"\t",b_all_access_list)

                                 try:

                                     chld_all_access_list = parse.find_all_children(b_all_access_list)

                                     if len(chld_all_access_list) >=1 :

                                         for access_k,access_m in enumerate(chld_all_access_list):

                                             #print( "".join(router_name),"\t", 'all_access_list',"\t",a_all_access_list,"\t",b_all_access_list,"\t",access_k,"\t",access_m)

                                             writer.writerow(("".join(router_name),'all_access_list',a_all_access_list,b_all_access_list,access_k,access_m))

                                 except:

                                    #print("".join(router_name),"\t","all_access_list","\t",a_all_access_list,"\t",b_all_access_list)

                                    writer.writerow(("".join(router_name),'all_access_list',a_all_access_list,b_all_access_list,'NA','NA'))

                                         

                                     

                            

                                   

                            route = parse.find_lines("^route")  

                            

                            for route_a,route_b in enumerate(route):

                            #     print(a,b)       

                                 chld_route = parse.find_all_children(route_b)

                                 if len(chld_route) >=1 :

                                     for route_k,route_m in enumerate(chld_route):

                                         #print( "".join(router_name),"\t", 'route',"\t",route_a,"\t",route_b,"\t",route_k,"\t",route_m)

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

                                         #print( "".join(router_name),"\t", 'snmp',"\t",snmp_a,"\t",snmp_b,"\t",snmp_k,"\t",snmp_m)

                                         writer.writerow(("".join(router_name),'snmp',snmp_a,snmp_b,snmp_k,snmp_m))

                                 else:

                                    #print("".join(router_name),"\t", 'snmp',"\t",snmp_a,"\t",snmp_b)

                                    writer.writerow(("".join(router_name),'snmp',snmp_a,snmp_b,'NA','NA'))

                                    

                            tacacs = parse.find_lines("^tacacs")  

                            

                            for tacacs_a,tacacs_b in enumerate(tacacs):

                            #     print(a,b)       

                                 chld_tacacs = parse.find_all_children(tacacs_b)

                                 if len(chld_tacacs) >=1 :

                                     for tacacs_k,tacacs_m in enumerate(chld_tacacs):

                                        # print( "".join(router_name),"\t", 'tacacs',"\t",tacacs_a,"\t",tacacs_b,"\t",tacacs_k,"\t",tacacs_m)

                                         writer.writerow(("".join(router_name),'tacacs',tacacs_a,tacacs_b,tacacs_k,tacacs_m))

                                 else:

                                    #print("".join(router_name),"\t", 'tacacs',"\t",tacacs_a,"\t",tacacs_b)

                                    writer.writerow(("".join(router_name),'tacacs',tacacs_a,tacacs_b,'NA','NA'))

                                  

                            control = parse.find_lines("^control")  

                            

                            for control_a,control_b in enumerate(control):

                            #     print(a,b)       

                                 chld_control = parse.find_all_children(control_b)

                                 if len(chld_control) >=1 :

                                     for control_k,control_m in enumerate(chld_control):

                                        # print( "".join(router_name),"\t", 'control',"\t",control_a,"\t",control_b,"\t",control_k,"\t",control_m)

                                         writer.writerow(("".join(router_name),'control',control_a,control_b,control_k,control_m))

                                 else:

                                    #print("".join(router_name),"\t", 'control',"\t",control_a,"\t",control_b)

                                    writer.writerow(("".join(router_name),'control',control_a,control_b,'NA','NA'))

                                   

                            banner = parse.find_lines("^banner")  

                            

                            for banner_a,banner_b in enumerate(banner):

                            #     print(a,b)       

                                 chld_banner = parse.find_all_children(banner_b)

                                 if len(chld_banner) >=1 :

                                     for banner_k,banner_m in enumerate(chld_banner):

                                         #print( "".join(router_name),"\t", 'banner',"\t",banner_a,"\t",banner_b,"\t",banner_k,"\t",banner_m)

                                         writer.writerow(("".join(router_name),'banner',banner_a,banner_b,banner_k,banner_m))

                                 else:

                                    #print("".join(router_name),"\t", 'banner',"\t",banner_a,"\t",banner_b)

                                    writer.writerow(("".join(router_name),'banner',banner_a,banner_b,'NA','NA'))

                                   

                            line = parse.find_lines("^line")  

                            

                            for line_a,line_b in enumerate(line):

                            #     print(a,b)       

                                 chld_line = parse.find_all_children(line_b)

                                 if len(chld_line) >=1 :

                                     for line_k,line_m in enumerate(chld_line):

                                        # print( "".join(router_name),"\t", 'line',"\t",line_a,"\t",line_b,"\t",line_k,"\t",line_m)

                                         writer.writerow(("".join(router_name),'line',line_a,line_b,line_k,line_m))

                                 else:

                                    #print("".join(router_name),"\t", 'line',"\t",line_a,"\t",line_b)

                                    writer.writerow(("".join(router_name),'line',line_a,line_b,'NA','NA'))

                                 

                            scheduler = parse.find_lines("^scheduler")  

                            

                            for scheduler_a,scheduler_b in enumerate(scheduler):

                            #     print(a,b)       

                                 chld_scheduler = parse.find_all_children(scheduler_b)

                                 if len(chld_scheduler) >=1 :

                                     for scheduler_k,scheduler_m in enumerate(chld_scheduler):

                                        # print( "".join(router_name),"\t", 'scheduler',"\t",scheduler_a,"\t",scheduler_b,"\t",scheduler_k,"\t",scheduler_m)

                                         writer.writerow(("".join(router_name),'scheduler',scheduler_a,scheduler_b,scheduler_k,scheduler_m))

                                 else:

                                   # print("".join(router_name),"\t", 'scheduler',"\t",scheduler_a,"\t",scheduler_b)

                                    writer.writerow(("".join(router_name),'scheduler',scheduler_a,scheduler_b,'NA','NA'))

                                  

                                    

                            ntp = parse.find_lines("^ntp")  

                            

                            for ntp_a,ntp_b in enumerate(ntp):

                            #     print(a,b)       

                                 chld_ntp = parse.find_all_children(ntp_b)

                                 if len(chld_ntp) >=1 :

                                     for ntp_k,ntp_m in enumerate(chld_ntp):

                                        # print( "".join(router_name),"\t", 'ntp',"\t",ntp_a,"\t",ntp_b,"\t",ntp_k,"\t",ntp_m)

                                         writer.writerow(("".join(router_name),'ntp',ntp_a,ntp_b,ntp_k,ntp_m))

                                 else:

                                   # print("".join(router_name),"\t", 'ntp',"\t",ntp_a,"\t",ntp_b)

                                    writer.writerow(("".join(router_name),'ntp',ntp_a,ntp_b,'NA','NA'))

           

            

    out_file.close()

parse_cisco_files(Full_Path_File_Nmae,outdirname,csvfilename)

