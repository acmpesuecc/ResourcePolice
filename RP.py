import psutil
import os
import time
import sys
import platform
import win10toast as w10Notif

plt = platform.system()
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
        if plt == 'Windows':
            if cpuUtil > 80.0:
                Win_CPUnotif()

            if vMem > 70.0:
                Win_memNotif()

            if diskUse > 90.0:
                Win_diskNotif()

            time.sleep(TIME_DELAY)
        elif plt == 'Darwin':
            if cpuUtil > 80.0:
                Mac_CPUnotif()

            if vMem > 70.0:
                Mac_memNotif()

            if diskUse > 90.0:
                Mac_diskNotif()

            time.sleep(TIME_DELAY)
        elif plt == 'Linux':
            if cpuUtil > 80.0:
                Linux_CPUnotif()

            if vMem > 70.0:
                Linux_memNotif()

            if diskUse > 90.0:
                Linux_diskNotif()

            time.sleep(TIME_DELAY)

        delete_last_line()
        
def Win_CPUnotif():
    # This function is to send in alert notifications in case of high CPU usage on windows

    n = w10Notif.ToastNotifier()

    n.show_toast("ResourcePolice", "CPU Usage high!", duration = 10)

def Win_memNotif():
    # This function is to send in alert notifications in case of high Memory usage on windows

    m = w10Notif.ToastNotifier()

    m.show_toast("ResourcePolice", "Memory Usage high!", duration = 10)

def Win_diskNotif():
    # This function is to send in alert notifications in case of high Disk usage on windows

    o = w10Notif.ToastNotifier()

    o.show_toast("ResourcePolice", "Disk Usage high!", duration = 10)

def Mac_CPUNotif():
    # This function is to send in alert notifications in case of high CPU usage on MAC
    message = 'CPU Usage high!'
    title = 'ResourcePolice'
    command = f'''
		osascript -e 'display notification "{message}" with title "{title}"'
        '''
    os.system(command)

def Mac_memNotif():
    # This function is to send in alert notifications in case of high Memory usage on MAC
    message = 'Memory Usage high!'
    title = 'ResourcePolice'
    command = f'''
		osascript -e 'display notification "{message}" with title "{title}"'
        '''
    os.system(command)

def Mac_diskNotif():
    # This function is to send in alert notifications in case of high Disk usage on MAC
    message = 'Disk Usage high!'
    title = 'ResourcePolice'
    command = f'''
		osascript -e 'display notification "{message}" with title "{title}"'
        '''
    os.system(command)

def Linux_CPUNotif():
    message = 'CPU Usage high!'
    title = 'ResourcePolice'
    command = f'''
		notify-send "{title}" "{message}"
		'''
    os.system(command)

def Linux_memNotif():
    message = 'Memory Usage high!'
    title = 'ResourcePolice'
    command = f'''
		notify-send "{title}" "{message}"
		'''
    os.system(command)

def Linux_diskNotif():
    message = 'Disk Usage high!'
    title = 'ResourcePolice'
    command = f'''
		notify-send "{title}" "{message}"
		'''
    os.system(command)
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

