import getpass
import os
import socket

import disable
import enable


def help():
    print("""
wifimgr - a command line utility for managing wifi networks

Usage:
    help - display this help menu
    list - list available wifi networks in a given wireless interface
    connect - connect to a wifi network using a wireless interface
    unblock - unblock wifi if blocked by rfkill
    enable - enable wireless interface
    disable - disable wireless interface
    ip-public - print your public IP address
    clear - clear the console screen
    exit - exit wifimgr""")

class Wifi:
    @staticmethod
    def unblock():
        try:
            os.system("rfkill unblock wifi")
        except Exception:
            print("Error when unblocking wifi")

    @staticmethod
    def list_wifi():
        ifnames = os.listdir("/sys/class/net/")
        print(ifnames)
        wireless = input("Enter your wireless interface (usually begins with wl): ")
        print(f"Wifi networks detected on {wireless}")
        os.system(f"nmcli d wifi list ifname {wireless}")

    @staticmethod
    def connect():
        ifnames = os.listdir("/sys/class/net/")
        wireless = ifnames[1]
        os.system(f"nmcli d wifi list ifname {wireless}")
        ssid = input("Please choose a network to connect to: ")
        password = getpass.getpass()
        os.system(f"nmcli d wifi connect {ssid} password {password} ifname {wireless}")


class Ip:
    @staticmethod
    def print_public_ip():
        try:
            os.system("curl 'https://api.ipify.org'")
        except Exception:
            pass

    @staticmethod
    def hostname():
        hostname = socket.gethostname()
        print(hostname)


def core():
    commands = {
        "help": help,
        "list": Wifi.list_wifi,
        "connect": Wifi.connect,
        "exit": exit,
        "clear": lambda: os.system("clear"),
        "enable": enable.enable,
        "disable": disable.disable,
        "ip-public": Ip.print_public_ip,
        "unblock": Wifi.unblock,
    }

    command = input("[wifimgr]$ ")

    try:
        commands[command]()
    except KeyError:
        pass


# Run main code
if __name__ == "__main__":
    while True:
        core()
