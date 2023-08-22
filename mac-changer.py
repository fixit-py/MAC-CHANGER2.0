#!/usr/bin/env python3

import subprocess
import optparse
import re
import random

print("All input entry must be string:")
print('e.g "y" , "n" ,  "00:00:5e:00:53:af" ')
def generate_mac_address():
    mac = [random.randint ( 0x00, 0xff ) for _ in range ( 6 )]
    mac[0] = (mac[0] & 0xfc) | 0x02  # Setting the second least significant bit of the first byte to 1
    mac_address = ':'.join ( ['{:02x}'.format ( byte ) for byte in mac] )
    return mac_address
question = input('Do you want a random MAC address "y"/"n":  ' )
if question == "y":
    new_mac = generate_mac_address()
elif question == "n":
    new_mac = input("enter a mac address:")
else:
    new_mac = generate_mac_address ()

print(new_mac)
def get_argument():
    parser = optparse.OptionParser()
    parser.add_option('-i', "--interface", dest="interface", help="interface to change the mac address")
    # parser.add_option('-m', "--mac", dest ="new_mac", help="new MAC address")
    (options, argument) = parser.parse_args()
    # to access the new interface we do option.interface same applies with the mac
    if not options.interface:
        parser.error("please enter an interface")
    #elif not options.new_mac:
        #parser.error("please enter a MAC address")
    return options


def change_mac(interface, new_mac):
    print("[+] changing the MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_new_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    print (ifconfig_result)
    mac_search = re.search (r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))
    if mac_search:
        return mac_search.group (0)
    else:
        print ("MAC address not present")
options = get_argument()

current = get_new_mac(options.interface)
print("new mac address ="+ str(current))
change_mac(options.interface, new_mac)
current = get_new_mac(options.interface)
if current == new_mac:
    print("[+] MAC address has successfully been changed to:" + current)
else:
    print ("[+] MAC address did not get changed ")


























# written by fixit
