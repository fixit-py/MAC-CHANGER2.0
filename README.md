# MAC-CHANGER2.0
# USAGE
clone the repository with git clone https://github.com/fixit-py/MAC-CHANGER2.0.git

change into the directory with cd MAC-CHANGER2.0

give the file permission to run as an executable with chmod +x mac-changer.py


run python mac-changer.py -i "interface" while using python2 

run python3 mac-changer.py -i "interface" while using  python3

replace the interface with the name of your network interface
![save](https://github.com/fixit-py/MAC-CHANGER2.0/assets/142362996/ab3d618f-536c-4687-9e9a-a61f3fc77d99)
![fix](https://github.com/fixit-py/MAC-CHANGER2.0/assets/142362996/a6652728-8790-44b7-b40d-d8ba10b774f1)

# ABOUT
This python program changes the MAC address of any interface on the network for a linux machine compatible with both python 2 and python 3
specify the interface name using the -i or --interface from the  bash terminal. Prompts the user to enter if they want the MAC address to be changed automatically to any random valid MAC address or the user wants to specify thier custom MAC address. "y" to be changed automatically to any random valid MAC address and  "n" to specify thier custom MAC address. note "" must be added to all entry prompted by the program while using python 2
