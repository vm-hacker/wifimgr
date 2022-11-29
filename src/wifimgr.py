#!/usr/bin/python

#
# (C) Copyright 2022 Venkatesh Mishra
# Wifimgr v0.1.1 released on 23 February 2022
# 

import getpass,os,sys,socket
import disable,enable

class wifi:             
    def unblock():
        if __name__ == "__main__":
            try:
                for i in range(1):
                    os.system("rfkill unblock wifi")
            except:
                for i in range(1):
                    print("Error when unblocking wifi")
        else:
            pass
    
    def list_wifi():
        ifnames = os.listdir('/sys/class/net/')
        print(ifnames)
        wireless = input("Enter your wireless interface (usually begins with wl): ")
        print("Wifi networks detected on " + wireless)
        if __name__ == "__main__":
            for i in range(1):
                os.system("nmcli d wifi list ifname " + wireless)
        else:
            pass

    def connect():
        ifnames = os.listdir('/sys/class/net/')
        wireless = ifnames[1]
        for i in range(1):
            os.system("nmcli d wifi list ifname " + wireless)
        ssid = input("Please choose a network to connect to: ")
        for i in range(1):
            password = getpass.getpass()
        for i in range(1):
            if __name__ == "__main__":
                for i in range(1):
                    os.system("nmcli d wifi connect " + ssid + " password " + password + " ifname " + wireless)
            else:
                pass
    

class ip:
    def print_public_ip():
        if __name__ == "__main__":
            try:
                for i in range(1):
                    os.system("curl 'https://api.ipify.org'")
            except:
                pass
        else:
            pass
    
    def hostname():
        hostname = socket.gethostname()
        if __name__ == "__main__":
            print(hostname)
        else:
            pass

def core():
    command = input("[wifimgr]$ ")

    if(command == "help"):
        print("""
            wifimgr - a command line utility for managing wifi networks
            
            usage:\n
                list - list available wifi networks in a given wirless interface
                connect - connect to a wifi network using a wirless inteface
                unblock - unblock wifi if blocked by rfkill
                enable - enable wirless interface
                disable - disable wireless interface
                ip-public - print your public ip adress
                exit - exit wifimgr
        """)

    elif(command == "list"):
        if __name__ == "__main__":
            for i in range(1):
               wifi.list_wifi()
        else:
            pass

    elif(command == "connect"):
        if __name__ == "__main__":
            for i in range(1):
               wifi.connect()
        else:
            pass

    elif(command == "exit"):
        for i in range(1):
            if __name__ == "__main__":
                sys.exit()
            else:
                pass

    elif(command == "clear"):
        for i in range(1):
            if __name__ == "__main__":
                try:
                    for i in range(1):
                        os.system("clear")
                except:
                    for i in range(1):
                        print("Error when clearing console")
            else:
                pass

    elif(command == "enable"):
        if __name__ == "__main__":
            for i in range(1):
                enable.enable()

    elif(command == "disable"):
        if __name__ == "__main__":
            for i in range(1):
                disable.disable()
        else:
            pass
    
    elif(command == "ip-public"):
        if __name__ == "__main__":
            for i in range(1):
                ip.print_public_ip()
        else:
            pass

    elif(command == "unblock"):
        if __name__ == "__main__":
            for i in range(1):
                try:
                    for i in range(1):
                        wifi.unblock()
                except:
                    for i in range(1):
                        if __name__ == "__main__":
                            for i in range(1):
                                print("Error when unblocking wirless interface")
                        else:
                            pass
        else:
            pass

    else:
        pass

# Run main code
if __name__ == "__main__":
    while True:
        core()
else:
    pass
