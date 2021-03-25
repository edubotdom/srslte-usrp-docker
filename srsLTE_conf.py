
# -*- coding: utf8 -*-
import sys, os

configuration_files_path= "/root/.config/srslte"
unvalid_option_message = 'Sorry, the option you selected seems not to be present, then try again!'

def change_apn():
    '''Changes APN configuration'''

    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########                  Customize APN configuration:               ########")
    print("########                                                             ########")
    print("#############################################################################")
    
    chosen_apn = input("Introduce the APN you'd like to register: ")

    confirmation = input("APN configuration is going to be updated with " + chosen_apn + ", do you want to proceed? (0/1): " )

    if int(confirmation) == 1:
        os.system("clear")
        
        #Modify epc file
        epc_file = open("srsLTE_conf/epc.conf", "r")
        epc_file_lines = epc_file.readlines()
        epc_file_lines[29] = "apn = " + str(chosen_apn) + "\n"
        epc_file = open("srsLTE_conf/epc.conf", "w")
        epc_file.writelines(epc_file_lines)
        epc_file.close() 

        #Copy result files to configuration path
        os.system("cp ./srsLTE_conf/epc.conf " + configuration_files_path)

        print("Operation succeeded")   
        return

    elif int(confirmation) == 0:
        os.system("clear")        
        menu()
        return
    else:
        print(unvalid_option_message)


def add_new_user():
    '''Adds a new user to database'''

    new_line=''

    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########                     Register a new user:                    ########")
    print("########                                                             ########")
    print("#############################################################################")
    
    chosen_name = input("Name: ")
    chosen_auth = input("Choose an authentication algorithm between XOR (xor) and MILENAGE (mil): ")
    chosen_imsi = input("Introduce IMSI user value: ")
    chosen_key = input("Introduce the key in hexadecimal: ")
    chosen_opc_type = input("Operator's code type, either OP or OPc: ")
    chosen_opc = input("Operator Code/Cyphered Operator Code, stored in hexadecimal: ")
    chosen_amf = input("Introduce authentication management field, stored in hexadecimal: ")
    chosen_sqn = input("Introduce Sequence number for freshness of the authentication: ")
    chosen_qci = input("Introduce QoS Class Identifier: ")
    chosen_ip = input("IP allocation stratagy for the SPGW: ")

    new_line = str(chosen_name)+","+str(chosen_auth)+","+str(chosen_imsi)+","+str(chosen_key)+","+str(chosen_opc_type)+","+str(chosen_opc)+","+str(chosen_amf)+","+str(chosen_sqn)+","+str(chosen_qci)+","+str(chosen_ip)

    print(new_line)
    confirmation = input("User with this data is going to be registered, do you want to proceed? (0/1): " )

    if int(confirmation) == 1:
        os.system("clear")
        
        #Modify user database file
        db_file = open("srsLTE_conf/user_db.csv", "a+")
        db_file.write("\n")
        db_file.write(new_line)
        db_file.close()

        #Copy result files to configuration path
        os.system("cp ./srsLTE_conf/user_db.csv " + configuration_files_path)

        print("Operation succeeded")   
        return

    elif int(confirmation) == 0:
        os.system("clear")        
        menu()
        return
    else:
        print(unvalid_option_message)

def change_parameters(mcc, mnc, band):
    '''Registers custom MCC, MNC and band, and save configuration'''

    print("CONFIRMATION: Requested configuration is MCC:" + str(mcc) + " ,MNC: " + str(mnc) + " and band: " + str(band) + ". Are you sure you want to proceed?")
    confirmate_changes = input("Do you want to proceed? (0/1): ")
    
    if int(confirmate_changes) == 1:
        #Check MNC format
        if(mnc<10):
            mnc = "0"+str(mnc)

        #Find equivalent Band - EARFCN
        earfcn = 0
        if(band) == 1:
            earfcn = 300
        elif(band) == 2:
            earfcn = 900
        elif(band) == 3:
            earfcn = 1575
        elif(band) == 4:
            earfcn = 2175
        elif(band) == 5:
            earfcn = 2525
        elif(band) == 6:
            earfcn = 2700
        elif(band) == 7:
            earfcn = 3100
        elif(band) == 8:
            earfcn = 3625
        elif(band) == 9:
            earfcn = 3975
        elif(band) == 10:
            earfcn = 4450
        elif(band) == 11:
            earfcn = 4850
        elif(band) == 12:
            earfcn = 5095
        elif(band) == 13:
            earfcn = 5230
        elif(band) == 14:
            earfcn = 5330
        elif(band) == 17:
            earfcn = 5790
        elif(band) == 18:
            earfcn = 5925
        elif(band) == 19:
            earfcn = 6075
        elif(band) == 20:
            earfcn = 6300
        elif(band) == 21:
            earfcn = 6525
        elif(band) == 22:
            earfcn = 7000
        elif(band) == 23:
            earfcn = 7600
        elif(band) == 24:
            earfcn = 7870
        elif(band) == 25:
            earfcn = 8365
        elif(band) == 26:
            earfcn = 8865
        elif(band) == 27:
            earfcn = 9125
        elif(band) == 28:
            earfcn = 9435
        elif(band) == 29:
            earfcn = 9715
        elif(band) == 30:
            earfcn = 9820
        elif(band) == 30:
            earfcn = 9895
        elif(band) == 31:
            earfcn = 10140
        elif(band) == 65:
            earfcn = 65986
        elif(band) == 66:
            earfcn = 66886
        elif(band) == 67:
            earfcn = 67436
        elif(band) == 68:
            earfcn = 67686
        elif(band) == 69:
            earfcn = 68086
        elif(band) == 70:
            earfcn = 68461
        elif(band) == 33:
            earfcn = 36100
        elif(band) == 34:
            earfcn = 36275
        elif(band) == 35:
            earfcn = 36650
        elif(band) == 36:
            earfcn = 37250
        elif(band) == 37:
            earfcn = 37650
        elif(band) == 38:
            earfcn = 38000
        elif(band) == 39:
            earfcn = 38450
        elif(band) == 40:
            earfcn = 39150
        elif(band) == 41:
            earfcn = 40620
        elif(band) == 42:
            earfcn = 42590
        elif(band) == 43:
            earfcn = 44590
        elif(band) == 44:
            earfcn = 46090
        elif(band) == 45:
            earfcn = 46690
        elif(band) == 46:
            earfcn = 50665
        elif(band) == 47:
            earfcn = 54890
        elif(band) == 48:
            earfcn = 55990
    
        #Modify enb file
        enb_file = open("srsLTE_conf/enb.conf", "r")
        enb_file_lines = enb_file.readlines()
        enb_file_lines[20] = "mcc = " + str(mcc) + "\n"
        enb_file_lines[21] = "mnc = " + str(mnc) + "\n"
        enb_file_lines[62] = "dl_earfcn = " + str(earfcn) + "\n"
        enb_file = open("srsLTE_conf/enb.conf", "w")
        enb_file.writelines(enb_file_lines)
        enb_file.close() 

        #Modify epc file
        epc_file = open("srsLTE_conf/epc.conf", "r")
        epc_file_lines = epc_file.readlines()
        epc_file_lines[26] = "mcc = " + str(mcc) + "\n"
        epc_file_lines[27] = "mnc = " + str(mnc) + "\n"
        epc_file = open("srsLTE_conf/epc.conf", "w")
        epc_file.writelines(epc_file_lines)
        epc_file.close() 

        #Modify rr file
        rr_file = open("srsLTE_conf/rr.conf", "r")
        rr_file_lines = rr_file.readlines()
        rr_file_lines[60] = "  dl_earfcn = " + str(earfcn) + "\n"
        rr_file = open("srsLTE_conf/rr.conf", "w")
        rr_file.writelines(rr_file_lines)
        rr_file.close()

        #Copy result files to Docker container
        os.system("cp ./srsLTE_conf/enb.conf " + configuration_files_path)
        os.system("cp ./srsLTE_conf/epc.conf " + configuration_files_path)
        os.system("cp ./srsLTE_conf/rr.conf " + configuration_files_path)

        print("Operation succeeded")
        
        return

    if int(confirmate_changes) == 0:
        os.system("clear")        
        menu()
        return
    else:
        print(unvalid_option_message)        

def menu():
    ''' Main menu to choose an item '''
    
    chosen_element = 0
    
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########                       Choose a option:                      ########")
    print("########                                                             ########")
    print("########      1) Change MCC, MNC and band                            ########")
    print("########      2) Register new user                                   ########")
    print("########      3) Change APN                                          ########")        
    print("########      4) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 4: ")
    
    if int(chosen_element) == 1:
        os.system("clear")
        region_selector()
        return
    elif int(chosen_element) == 2:
        os.system("clear")        
        add_new_user()
        return
    elif int(chosen_element) == 3:
        os.system("clear")        
        change_apn()
        return
    elif int(chosen_element) == 4:
        os.system("clear")        
        sys.exit()
        return
    else:
        print(unvalid_option_message)

def region_selector():
    
    ''' Region selection menu '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########                    Choose a world region:                   ########")
    print("########                                                             ########")
    print("########      1) North America                                       ########")
    print("########      2) Europe                                              ########")    
    print("########      3) LATAM                                               ########")
    print("########      4) APAC                                                ########")
    print("########      5) CBRS PLTE                                           ########") 
    print("########      6) Return                                              ########")       
    print("########      7) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 7: ")

    if int(chosen_element) == 1:
        os.system("clear")
        north_american_networks()
        return
    if int(chosen_element) == 2:
        os.system("clear")
        european_networks()
        return
    if int(chosen_element) == 3:
        os.system("clear")
        latam_networks()
        return
    if int(chosen_element) == 4:
        os.system("clear")
        apac_networks()
        return
    if int(chosen_element) == 5:
        os.system("clear")
        cbrs_networks()
        return
    if int(chosen_element) == 6:
        os.system("clear")
        menu()
        return         
    elif int(chosen_element) == 7:
        os.system("clear")        
        sys.exit()
    else:
        print(unvalid_option_message)

## NORTH_AMERICA

def north_american_networks():
    
    ''' North America network selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########                Choose a north american network:             ########")
    print("########                                                             ########")
    print("########      1) USA AT&T (310 410)                                  ########")
    print("########      2) USA T-Mobile (310 260)                              ########")    
    print("########      3) USA Verizon (311 480)                               ########")
    print("########      4) Return                                              ########")    
    print("########      5) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 5: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        usa_att()
        return
    if int(chosen_element) == 2:
        os.system("clear")
        usa_tmobile()
        return
    if int(chosen_element) == 3:
        os.system("clear")
        usa_verizon()
        return
    if int(chosen_element) == 4:
        os.system("clear")
        region_selector()
        return        
    if int(chosen_element) == 5:
        os.system("clear")        
        sys.exit()
    else:
        print(unvalid_option_message)

def usa_att():
    
    ''' USA AT&T Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 2                                                   ########")
    print("########      2) 4                                                   ########")
    print("########      3) 17                                                  ########")
    print("########      4) 30                                                  ########")
    print("########      5) Return                                              ########")    
    print("########      6) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 6: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(310,410,2)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(310,410,4)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(310,410,17)
        return
    if int(chosen_element) == 4:
        os.system("clear")
        change_parameters(310,410,30)
        return
    if int(chosen_element) == 5:
        os.system("clear")
        north_american_networks() 
        return       
    if int(chosen_element) == 6:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def usa_tmobile():
    
    ''' USA T-Mobile Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 2                                                   ########")
    print("########      2) 4                                                   ########")
    print("########      3) 12                                                  ########")
    print("########      4) 66                                                  ########")
    print("########      5) 71                                                  ########")    
    print("########      6) Return                                              ########")    
    print("########      7) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 7: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(310,260,2)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(310,260,4)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(310,260,12)
        return
    if int(chosen_element) == 4:
        os.system("clear")
        change_parameters(310,260,66)
        return
    if int(chosen_element) == 5:
        os.system("clear")
        change_parameters(310,260,71)
        return    
    if int(chosen_element) == 6:
        os.system("clear")
        north_american_networks()
        return       
    if int(chosen_element) == 7:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def usa_verizon():
    
    ''' USA Verizon Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 2                                                   ########")
    print("########      2) 4                                                   ########")
    print("########      3) 13                                                  ########")
    print("########      4) Return                                              ########")    
    print("########      5) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 5: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(311,480,2)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(311,480,4)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(311,480,13)
        return 
    if int(chosen_element) == 4:
        os.system("clear")
        north_american_networks()
        return      
    if int(chosen_element) == 5:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

##EUROPE

def european_networks():
    
    ''' Europe network selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########                Choose a european network:                   ########")
    print("########                                                             ########")
    print("########      1) SP Orange (214 03)                                  ########")
    print("########      2) FR Orange (208 01)                                  ########")
    print("########      3) UK Vodafone (234 15)                                ########")
    print("########      4) GER Vodafone (262 02)                               ########")
    print("########      5) ITA Vodafone (222 10)                               ########")
    print("########      6) NL KPN (204 08)                                     ########")
    print("########      7) Return                                              ########")    
    print("########      8) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 8: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        sp_orange()
        return
    if int(chosen_element) == 2:
        os.system("clear")
        fr_orange()
        return
    if int(chosen_element) == 3:
        os.system("clear")
        uk_vodafone()
        return
    if int(chosen_element) == 4:
        os.system("clear")
        ger_vodafone()
        return
    if int(chosen_element) == 5:
        os.system("clear")
        ita_vodafone()
        return
    if int(chosen_element) == 6:
        os.system("clear")
        nl_kpn()
        return
    if int(chosen_element) == 7:
        os.system("clear")
        region_selector()
        return        
    if int(chosen_element) == 8:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def sp_orange():
    
    ''' Spain Orange Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 3                                                   ########")
    print("########      2) 7                                                   ########")
    print("########      3) Return                                              ########")    
    print("########      4) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 4: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(214,3,3)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(214,3,7)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        european_networks()
        return        
    if int(chosen_element) == 4:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def fr_orange():
    
    ''' France Orange Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 3                                                   ########")
    print("########      2) 7                                                   ########")
    print("########      3) 20                                                  ########")
    print("########      4) 28                                                  ########")    
    print("########      5) Return                                              ########")    
    print("########      6) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 6: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(208,1,3)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(208,1,7)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(208,1,20)
        return
    if int(chosen_element) == 4:
        os.system("clear")
        change_parameters(208,1,28)
        return        
    if int(chosen_element) == 5:
        os.system("clear")
        european_networks()
        return        
    if int(chosen_element) == 6:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def uk_vodafone():
    
    ''' United Kingdom Vodafone Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 1                                                   ########")    
    print("########      2) 3                                                   ########")
    print("########      3) 7                                                   ########")
    print("########      4) 20                                                  ########")    
    print("########      5) Return                                              ########")    
    print("########      6) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 6: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(234,15,1)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(234,15,3)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(234,15,7)
        return
    if int(chosen_element) == 4:
        os.system("clear")
        change_parameters(234,15,20)
        return        
    if int(chosen_element) == 5:
        os.system("clear")
        european_networks()
        return
    if int(chosen_element) == 6:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def ger_vodafone():
    
    ''' Germany Vodafone Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 7                                                   ########")
    print("########      2) 20                                                  ########")    
    print("########      3) Return                                              ########")    
    print("########      4) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 4: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(262,2,7)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(262,2,20)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        european_networks()
        return
    if int(chosen_element) == 4:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def ita_vodafone():
    
    ''' Italy Vodafone Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 3                                                   ########")
    print("########      2) 20                                                  ########")    
    print("########      3) Return                                              ########")    
    print("########      4) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 4: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(222,10,3)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(222,10,20)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        european_networks()
        return
    if int(chosen_element) == 4:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def nl_kpn():
    
    ''' Netherlands KPN Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 3                                                   ########")
    print("########      2) 7                                                  ########")    
    print("########      3) 20                                                  ########")    
    print("########      4) Return                                              ########")    
    print("########      5) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 5: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(204,8,3)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(204,8,7)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(204,8,20)
        return
    if int(chosen_element) == 4:
        os.system("clear")
        european_networks()
        return        
    if int(chosen_element) == 5:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

#LATAM

def latam_networks():
    
    ''' LATAM network selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########                   Choose a LATAM network:                   ########")
    print("########                                                             ########")
    print("########      1) MX Telcel (334 020)                                 ########")
    print("########      2) MX AT&T (334 020)                                   ########")
    print("########      3) Honduras Tigo (708 02)                              ########")
    print("########      4) Honduras Claro (708 040)                            ########")
    print("########      5) Colombia Claro (732 101)                            ########")
    print("########      6) Colombia Telefonica (732 123)                       ########")
    print("########      7) Peru Telefonica (716 06)                            ########")
    print("########      8) Peru Claro (716 10)                                 ########")
    print("########      9) Guatemala Claro (704 01)                            ########")
    print("########      10) Guatemala Tigo (704 02)                            ########")
    print("########      11) Chile Entel (730 01)                               ########")
    print("########      12) Chile Claro (730 03)                               ########")  
    print("########      13) Costa Rica Claro (712 03)                          ########")
    print("########      14) Costa Rica Telefonica (712 04)                     ########")
    print("########      15) Panama Telefonica (714 020)                        ########")
    print("########      16) Puerto Rico Claro (330 110)                        ########") 
    print("########      17) Return                                             ########")          
    print("########      18) Exit                                               ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 18: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(334,20,4)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(334,20,4)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(708,2,4)
        return
    if int(chosen_element) == 4:
        os.system("clear")
        change_parameters(708,40,4)
        return
    if int(chosen_element) == 5:
        os.system("clear")
        change_parameters(732,101,7)
        return
    if int(chosen_element) == 6:
        os.system("clear")
        change_parameters(732,123,4)
        return
    if int(chosen_element) == 7:
        os.system("clear")
        change_parameters(716,6,4)
        return
    if int(chosen_element) == 8:
        os.system("clear")
        change_parameters(716,10,2)
        return
    if int(chosen_element) == 9:
        os.system("clear")
        change_parameters(704,1,2)
        return
    if int(chosen_element) == 10:
        os.system("clear")
        change_parameters(704,2,5)
        return
    if int(chosen_element) == 11:
        os.system("clear")
        change_parameters(730,1,7)
        return
    if int(chosen_element) == 12:
        os.system("clear")
        change_parameters(730,3,7)
        return
    if int(chosen_element) == 13:
        os.system("clear")
        change_parameters(712,3,3)
        return
    if int(chosen_element) == 14:
        os.system("clear")
        change_parameters(712,4,3)
        return
    if int(chosen_element) == 15:
        os.system("clear")
        change_parameters(714,20,28)
        return
    if int(chosen_element) == 16:
        os.system("clear")
        pr_claro()
        return
    if int(chosen_element) == 17:
        os.system("clear")
        region_selector()
        return
    if int(chosen_element) == 18:
        os.system("clear")        
        sys.exit()
    else:
        print(unvalid_option_message)

def pr_claro():
    
    ''' Puerto Rico Claro Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 4                                                   ########")
    print("########      2) 13                                                  ########")    
    print("########      3) 17                                                  ########")
    print("########      4) 25                                                  ########")    
    print("########      5) Return                                              ########")    
    print("########      6) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 6: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(330,110,4)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(330,110,13)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(330,110,17)
        return
    if int(chosen_element) == 4:
        os.system("clear")
        change_parameters(330,110,25)
        return
    if int(chosen_element) == 5:
        os.system("clear")
        european_networks()
        return
    if int(chosen_element) == 6:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

##APAC

def apac_networks():
    
    ''' APAC network selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########                   Choose an APAC network:                   ########")
    print("########                                                             ########")
    print("########      1) China Mobile (460 02)                               ########")
    print("########      2) China Unicom (460 01)                               ########")
    print("########      3) Malaysia Celcom (502 19)                            ########")
    print("########      4) Malaysia Maxis (502 12)                             ########")
    print("########      5) Australia Vodafone (505 03)                         ########")
    print("########      6) Australia Telstra (505 01)                          ########")
    print("########      7) Return                                              ########")
    print("########      8) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 8: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        china_mobile()
        return
    if int(chosen_element) == 2:
        os.system("clear")
        china_unicom()
        return
    if int(chosen_element) == 3:
        os.system("clear")
        malaysia_celcom()
        return
    if int(chosen_element) == 4:
        os.system("clear")
        malaysia_maxis()
        return
    if int(chosen_element) == 5:
        os.system("clear")
        australia_vodafone()
        return
    if int(chosen_element) == 6:
        os.system("clear")
        australia_telstra()
        return
    if int(chosen_element) == 7:
        os.system("clear")
        region_selector()
        return
    if int(chosen_element) == 8:
        os.system("clear")        
        sys.exit()
    else:
        print(unvalid_option_message)

def china_mobile():
    
    ''' China Mobile Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 38                                                   ########")
    print("########      2) 39                                                  ########")    
    print("########      3) 40                                                  ########")
    print("########      4) 41                                                  ########")    
    print("########      5) Return                                              ########")    
    print("########      6) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 6: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(460,2,38)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(460,2,39)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(460,2,40)
        return
    if int(chosen_element) == 4:
        os.system("clear")
        change_parameters(460,2,41)
        return
    if int(chosen_element) == 5:
        os.system("clear")
        apac_networks()
        return     
    if int(chosen_element) == 6:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def china_unicom():
    
    ''' China Unicom Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 3                                                  ########")
    print("########      2) 41                                                  ########")    
    print("########      3) Return                                              ########")    
    print("########      4) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 4: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(460,1,3)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(460,1,41)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        apac_networks()
        return      
    if int(chosen_element) == 4:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def malaysia_celcom():
    
    ''' Malaysia Celcom Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 3                                                  ########")
    print("########      2) 7                                                  ########")    
    print("########      3) Return                                              ########")    
    print("########      4) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 4: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(502,19,3)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(502,19,7)
        return    
    if int(chosen_element) == 3:
        os.system("clear")
        apac_networks()
        return    
    if int(chosen_element) == 4:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def malaysia_maxis():
    
    ''' Malaysia Maxis Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 3                                                  ########")
    print("########      2) 7                                                  ########")    
    print("########      3) Return                                              ########")    
    print("########      4) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 4: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(502,12,3)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(502,12,7) 
        return    
    if int(chosen_element) == 3:
        os.system("clear")
        apac_networks()
        return
    if int(chosen_element) == 4:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def australia_vodafone():
    
    ''' Australia Vodafone Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 1                                                   ########")
    print("########      2) 3                                                   ########") 
    print("########      3) 5                                                   ########")       
    print("########      4) Return                                              ########")    
    print("########      5) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 5: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(505,3,1)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(505,3,3)
        return 
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(505,3,5)
        return             
    if int(chosen_element) == 4:
        os.system("clear")
        apac_networks()
        return        
    if int(chosen_element) == 5:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def australia_telstra():
    
    ''' Australia Telstra Band selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########            Choose a band for the requested network:         ########")
    print("########                                                             ########")
    print("########      1) 1                                                   ########")
    print("########      2) 3                                                   ########")
    print("########      3) 28                                                  ########")        
    print("########      4) Return                                              ########")    
    print("########      5) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 5: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(505,1,1)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(505,1,3)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        change_parameters(505,1,28)
        return 
    if int(chosen_element) == 4:
        os.system("clear")
        apac_networks()
        return        
    if int(chosen_element) == 5:
        os.system("clear")
        sys.exit()
    else:
        print(unvalid_option_message)

def cbrs_networks():
    
    ''' CBRS PLTE network selection '''
        
    chosen_element = 0 
        
    print("#############################################################################")
    print("########                                                             ########")
    print("########              srsLTE Band and MCCMNC configurator            ########")
    print("########                                                             ########")
    print("########                Choose a CBRS PLTE band network:             ########")
    print("########                                                             ########")
    print("########      1) Expeto (313 260)                                    ########")
    print("########      2) Pod (901 75)                                        ########")
    print("########      3) Return                                              ########")
    print("########      4) Exit                                                ########")
    print("########                                                             ########")
    print("#############################################################################")
    chosen_element = input("Select an option from 1 to 4: ")    

    if int(chosen_element) == 1:
        os.system("clear")
        change_parameters(313,260,48)
        return
    if int(chosen_element) == 2:
        os.system("clear")
        change_parameters(901,75,42)
        return
    if int(chosen_element) == 3:
        os.system("clear")
        region_selector()
        return
    if int(chosen_element) == 4:
        os.system("clear")        
        sys.exit()
    else:
        print(unvalid_option_message)

if __name__ == '__main__':
    menu()