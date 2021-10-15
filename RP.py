import psutil
import os
import time
import sys
import plyer
from os import system, name
from time import sleep
import speedtest
TIME_DELAY = 1.5


def menu():
        choice=input("Enter which resource you want check : \nMemory(m)\nCPU(c)\nDisk(d)\nNetwork(n)\nQuit(q)\n")
        choice=choice.lower()
        clear()
        if choice=="m":
            vMem = psutil.virtual_memory().percent
            if vMem > 70.0:
                memNotif()
            print("Memory:\t{}".format(str(vMem)))
            menu()
        if choice=="c":
            cpuUtil = psutil.cpu_percent()
            if cpuUtil > 80.0:
                CPUnotif()
            print("CPU:\t{}".format(str(cpuUtil)))
            menu()
        if choice=="d":
            diskUse = psutil.disk_usage(os.sep).percent
            if diskUse > 90.0:
                diskNotif()
            print("Disk:\t{}".format(str(diskUse)))
            menu()
        if choice=="n":
            showNetworkResource()
            menu()
        if choice=="q":
            quit()
def CPUnotif():

    # This function is to send in alert notifications in case of high CPU usage for 10s

    plyer.notification.notify("ResourcePolice", "CPU Usage high!", timeout=10)


def memNotif():

    # This function is to send in alert notifications in case of high RAM usage for 10s

    plyer.notification.notify(
        "ResourcePolice", "Memory Usage high!", timeout=10)


def diskNotif():

    # This function is to send in alert notifications in case of high disk usage for 10s

    plyer.notification.notify("ResourcePolice", "Disk Usage high!", timeout=10)

# LOOKUP = {
#     'rp.start': start,
#     'rp.stop': stop,
#     'rp.quit': quit,
#     'rp.network': showNetworkResource
# } # lookup table for user-defined commands

def quit():
    sys.exit()

def showNetworkResource():
    st=speedtest.Speedtest()
    print("Download Speed : ".format(st.download()))
    print("Upload Speed : ".format(st.upload()))

def delete_last_line():

    # This function refreshes resource variables

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

if __name__=="__main__":
    menu()
