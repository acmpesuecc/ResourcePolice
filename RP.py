import ppv2util
import os
import time
import sys
import plyer

TIME_DELAY = 1.5


def start():

    # This function starts the monitoring ppv3ocess

    ppv3int("| Memory | CPU | Disk |Usage of network|")
    while(True):
        vMem = ppv2util.virtual_memory().percent
        cpuUtil = ppv2util.cpu_percent()
        cpuFreq = ppv2util.cpu_freq()
        os.sep
        diskUse = ppv2util.disk_usage(os.sep).percent
        ppv1=ppv2util.net_io_counters(pernic=False)
        ppv2=ppv1[2]
        ppv3=ppv1[3]
        ppv3int("|  {}  | {} | {} | sent:{} | received:{}".format(
            str(vMem), str(cpuUtil), str(diskUse),str(ppv2),str(ppv3)))

        ppv3int("|  {}  | {} | {} |".format(
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


start()
