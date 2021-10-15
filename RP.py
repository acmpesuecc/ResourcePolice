import psutil
import os
import time
import sys
import win10toast as w10Notif
from os import name, system
TIME_DELAY = 1.5

def start():

    # This function starts the monitoring process 

    print("| Memory | CPU | Disk |")
    while(True):
        vMem = psutil.virtual_memory().percent
        cpuUtil = psutil.cpu_percent()
        cpuFreq = psutil.cpu_freq()
        os.sep
        diskUse = psutil.disk_usage(os.sep).percent

        print("|  {}  | {} | {} |".format(str(vMem), str(cpuUtil), str(diskUse)))

        if cpuUtil > 80.0:
            CPUnotif()

        if vMem > 70.0:
            memNotif()

        if diskUse > 90.0:
            diskNotif()

        time.sleep(TIME_DELAY)
        delete_last_line()
        
def CPUnotif():

    # This function is to send in alert notifications in case of high CPU usage

    n = w10Notif.ToastNotifier()

    n.show_toast("ResourcePolice", "CPU Usage high!", duration = 10)

def memNotif():

    # This function is to send in alert notifications in case of high CPU usage

    m = w10Notif.ToastNotifier()

    m.show_toast("ResourcePolice", "Memory Usage high!", duration = 10)

def diskNotif():

    # This function is to send in alert notifications in case of high CPU usage

    o = w10Notif.ToastNotifier()

    o.show_toast("ResourcePolice", "Disk Usage high!", duration = 10)

# LOOKUP = {
#     'rp.start': start,
#     'rp.stop': stop,
#     'rp.quit': quit,
#     'rp.network': showNetworkResource
# } # lookup table for user-defined commands 

def stop():

    # complete this function to stop monitoring

    pass

def quit():

    # complete this function to quit ResourcePolice

    pass

def showNetworkResource():

    # complete this function to monitor system network resource
    #print("\n_____________________________________________________Network Monitoring_____________________________________________________________\n")
    print("| Bytes_sent \t\t | Bytes_rcvd\t\t | Pakts_sent \t\t | Pakts_rcvd\t\t ")
    while(True):
        Bytes_sent, Bytes_received, Packets_sent, Packets_received = list(psutil.net_io_counters())[:4]
        #Errin, Errout, Dropin, Dropout = list(psutil.net_io_counters())[4:]
        os.sep
        diskUse = psutil.disk_usage(os.sep).percent

        print(f"| {round(Bytes_sent/1000, 3)}KB\t\t | {round(Bytes_received/1000, 3)}KB\t\t | {Packets_sent}  \t\t | {Packets_received} ", end = '\r')

        time.sleep(TIME_DELAY)
        # delete_last_line()


def delete_last_line():

    # This function refreshes resource variables

    # Checking if the working system is a Windows machine. Changes console setting if that's the case.
    # if os.name == 'nt':
    #     from ctypes import windll
    #     k = windll.kernel32
    #     k.SetConsoleMode(k.GetStdHandle(-11), 7)
        
    # CURSOR_UP_ONE = '\x1b[1A'
    # ERASE_LINE = '\x1b[2K'
    CURSOR_UP_ONE = '\033[F'
    ERASE_LINE = '\033[K'
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)

def refresh_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux
    else:
        _ = system('clear')

# start()
showNetworkResource()

