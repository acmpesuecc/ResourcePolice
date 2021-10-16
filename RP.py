import psutil
import os
import time
import sys
import plyer
from tabulate import tabulate

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

        print("|  {}  | {} | {} |".format(
            str(vMem), str(cpuUtil), str(diskUse)))

        if cpuUtil > 80.0:
            CPUnotif()

        if vMem > 70.0:
            memNotif()

        if diskUse > 90.0:
            diskNotif()

        time.sleep(TIME_DELAY)
        delete_last_line()


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


def stop():

    # complete this function to stop monitoring

    pass


def quit():

    # complete this function to quit ResourcePolice

    pass


def showNetworkResource():

    # complete this function to monitor system network resource

    pass


def delete_last_line():

    # This function refreshes resource variables

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)

def network_stats():
    Net = psutil.net_if_stats()
    #print("| Interface | ISUP | Speed | MTU |")
    table = [['Interface', 'ISUP', 'Speed', 'MTU']]
    for key,value in Net.items():
        temp_list = []
        temp_list.append(key)
        temp_list.append(value[0])
        temp_list.append(value[2])
        temp_list.append(value[3])
        table.append(temp_list)
        #print(temp_list)
        #temp_list.clear()
    #print(table)
    print(tabulate(table, headers='firstrow'))

#start()
#network_stats()

print("-----Resource Police-----")
print("1. System stats")
print("2. Network Interface stats")
ans = int(input("Enter option : "))
if(ans == 1):
    start()
if(ans == 2):
    network_stats()