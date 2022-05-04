def enable():
    ifname = input("Enter the inteface to enable: ")
    if __name__ == "__main__":
        try:
            for i in range(1):
                os.system("ip link set " + ifname + " up")
        except:
            pass
    else:
        pass
