import psutil
import os
import time
import sys
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify


Notify.init("Resource Police")
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

#This variable is to set the frequency of notifications
notif_frequency=10       
def CPUnotif():

    # This function is to send in alert notifications in case of high CPU usage

    n = Notify.Notification.new("Alert","<b>CPU Usage high!</b>","dialog-information")
    n.set_urgency(1)

    n.show()
    time.sleep(notif_frequency)

def memNotif():

    # This function is to send in alert notifications in case of high memory usage

    m = Notify.Notification.new("Alert","<b>Memory Usage high!</b>","dialog-information")
    m.set_urgency(1)

    m.show()
    time.sleep(notif_frequency)

def diskNotif():

    # This function is to send in alert notifications in case of high Disk usage

    o = Notify.Notification.new("Alert","<b>Disk Usage high!</b>","dialog-information")
    o.set_urgency(1)

    o.show()
    time.sleep(notif_frequency)
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

start()

