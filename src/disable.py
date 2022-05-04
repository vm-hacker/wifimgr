def disable():
    ifname = input("Enter the inteface to disable: ")
    if __name__ == "__main__":
        try:
            for i in range(1):
                os.system("ip link set " + ifname + " down")
        except:
            pass
    else:
        pass
