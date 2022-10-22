import psutil
import os
import time
import sys
import plyer
import platform
import subprocess

TIME_DELAY = 1

def start():
    '''
    This function starts the monitoring process
    '''

    print("\n")
    print("="*50)
    print("System Resources:".center(50))
    print("="*50)

    # disp = "| Memory usage | CPU usage | Disk usage |"
    # print(disp.center(0))

    dispList = ['Memory usage', 'CPU usage', 'Disk usage']
    eqSpam = '=' * 50

    print(eqSpam)
    print('{:<12s}{:>12s}{:>12s}'.format(dispList[0],dispList[1],dispList[2]))
    print(eqSpam)

    while(True):
        vMem = psutil.virtual_memory().percent
        cpuUtil = psutil.cpu_percent()
        cpuFreq = psutil.cpu_freq()
        os.sep
        diskUse = psutil.disk_usage(os.sep).percent

        # outDisp = "|  {}  | {} | {} |".format(
            # str(vMem), str(cpuUtil), str(diskUse))

        # print(outDisp.center(40))
        print('{:<12.1f}{:>12.1f}{:>12.1f}'.format(vMem,cpuUtil,diskUse))

        netstat = netStatDisplay()
        print(netstat)
        if cpuUtil > 80.0:
            CPUnotif()

        if vMem > 70.0:
            memNotif()

        if diskUse > 90.0:
            diskNotif()

        time.sleep(TIME_DELAY)
        delete_last_line()

def CPUnotif():
    '''
    This function is to send in alert notifications in case of high CPU usage for 10s
    '''

    plyer.notification.notify("ResourcePolice", "CPU Usage high!", timeout=10)


def memNotif():
    '''
    This function is to send in alert notifications in case of high RAM usage for 10s
    '''

    plyer.notification.notify("ResourcePolice", "Memory Usage high!", timeout=10)


def diskNotif():
    '''
    This function is to send in alert notifications in case of high disk usage for 10s
    '''

    plyer.notification.notify("ResourcePolice", "Disk Usage high!", timeout=10)

def delete_last_line():
    '''
    This function refreshes resource variables
    '''

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    for i in range(4):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def fetchSystemInfo():
    '''
    Fetches system information
    '''
    print("\n")
    print("="*50)
    print("System Information:".center(50))
    print("="*50)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

def introScreenLogo():
    '''
    Prints intro screen
    '''
    uname = platform.uname()
    if "darwin" in {uname.system}:
        os.system("clear") #clear works for unix systems
        f = open('rplogo.txt', 'r')
        print(''.join([line for line in f]))
    else :
        os.system("cls") #cls works for windows
        f = open('rplogo.txt', 'r')
        print(''.join([line for line in f]))


def netStatDisplay():
    reply = subprocess.run(['ping','-c','1','www.google.com'],
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE,
                           encoding = 'utf-8')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stderr
    return reply

#introScreenLogo()
fetchSystemInfo()
#start()
