#!/usr/bin/env python3
'''
use the netifaces packages to print info (MAC and IP address) of the different interfaces on the machine
'''

import netifaces

print("\n**************Details of Interfaces with MAC and/or IP addresses *********************")
for i in netifaces.interfaces():
    has_address = False

    i_addresses = netifaces.ifaddresses(i)
    if netifaces.AF_LINK in i_addresses:
        has_address = True
        print(f"\n**************Details of Interface - '{i}' *********************")
        print(f"MAC: {i_addresses[netifaces.AF_LINK][0]['addr']}")
    
    if netifaces.AF_INET in i_addresses:
        if not has_address:
            print(f"\n**************Details of Interface - '{i}' *********************")
        print(f"IP: {netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']}")
    

