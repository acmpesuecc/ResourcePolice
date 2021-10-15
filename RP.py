import psutil
import os
import time
import sys
import win10toast as w10Notif
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

    # This function is to send in alert notifications in case of high CPU usage

    n = w10Notif.ToastNotifier()

    n.show_toast("ResourcePolice", "CPU Usage high!", duration=10)


def memNotif():

    # This function is to send in alert notifications in case of high CPU usage

    m = w10Notif.ToastNotifier()

    m.show_toast("ResourcePolice", "Memory Usage high!", duration=10)


def diskNotif():

    # This function is to send in alert notifications in case of high CPU usage

    o = w10Notif.ToastNotifier()

    o.show_toast("ResourcePolice", "Disk Usage high!", duration=10)

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
    while True:
        # Headers received from psutil.net_io_counters()
        headers = ['Bytes Sent', 'Bytes Received', 'Packets Sent',
                   'Packets Received', 'ErrIn', 'ErrOut', 'DropIn', 'DropOut']

        print(tabulate([list(psutil.net_io_counters())], headers=headers))

        time.sleep(TIME_DELAY)
        for _ in range(3):
            delete_last_line()


def delete_last_line():

    # This function refreshes resource variables

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)


if __name__ == "__main__":
    # Menu that lets the user choose b/w showing system resources and network resources

    print("""Welcome to ResourcePolice
1 --- Monitor System Resources
2 --- Monitor Network Packets""")
    choice = input()
    if choice == '1':
        start()
    elif choice == '2':
        showNetworkResource()
    else:
        print('Invalid Option! Exiting...')
