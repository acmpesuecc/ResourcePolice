import psutil
import os
import time
import sys
import win10toast as w10Notif

TIME_DELAY = 1.0
prev_upload = int(psutil.net_io_counters(pernic=False)[0])

def start():
    # This function starts the monitoring process

    print("| Memory% | CPU%  | CPU(Hz) | Disk% | Upload(kB) | Download(kB) |")
    prev_upload = int(psutil.net_io_counters(pernic=False)[0]/1024)
    prev_download = int(psutil.net_io_counters(pernic=False)[1]/1024)
    while True:
        vMem = psutil.virtual_memory().percent
        cpuUtil = psutil.cpu_percent()
        cpuFreq = psutil.cpu_freq()[1]/1000
        sep = os.sep
        new_upload = int(psutil.net_io_counters(pernic=False)[0]/1024)
        upload = (new_upload - prev_upload)/TIME_DELAY
        prev_upload = new_upload
        new_download = int(psutil.net_io_counters(pernic=False)[1]/1024)
        download = (new_download - prev_download)/TIME_DELAY
        prev_download = new_download
        diskUse = psutil.disk_usage(sep).percent

        print("| {0:>6}% | {1:^4}% | {2:>4}GHz | {3:>4}% | {4:>5}kBps | {5:>5}kBps  |".format(
            str(vMem), str(cpuUtil), str(cpuFreq), str(diskUse), str(upload), str(download)))

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

    pass

def delete_last_line():

    # This function refreshes resource variables

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)

start()


