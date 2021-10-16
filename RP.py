import psutil
import os
import time
import sys
import plyer
import speedtest

TIME_DELAY = 1.5


def start():

    # This function starts the monitoring process

    print("| Memory | CPU | Disk |")
    st = speedtest.Speedtest()
    while(True):
        vMem = psutil.virtual_memory().percent
        cpuUtil = psutil.cpu_percent()
        cpuFreq = psutil.cpu_freq()
        os.sep
        diskUse = psutil.disk_usage(os.sep).percent

        print("|  {}  | {} | {} |".format(
            str(vMem), str(cpuUtil), str(diskUse)))
        print('=========================')
        network_stats = psutil.net_io_counters(pernic=True)['lo0']
        bytes_sent = network_stats.bytes_sent
        bytes_recv = network_stats.bytes_recv
        print("| Bytes_sent | Bytes Recived |")
        print("| {} | {} |".format(str(bytes_sent),str(bytes_recv)))
        # print("==============================")
        # print('| Download Speed | Upload Speed |')
        # print('| {} | {} |'.format(str(st.download()), str(st.upload())))

        if cpuUtil > 80.0:
            CPUnotif()

        if vMem > 70.0:
            memNotif()

        if diskUse > 90.0:
            diskNotif()

        time.sleep(TIME_DELAY)
        delete_last_line()
        delete_last_line()
        delete_last_line()
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