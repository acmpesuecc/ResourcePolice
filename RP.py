import psutil
import os
import time
import sys

def start():
    print("| Memory | CPU | Disk |")
    while(True):
        vMem = psutil.virtual_memory().percent
        cpuUtil = psutil.cpu_percent()
        cpuFreq = psutil.cpu_freq()
        os.sep
        diskUse = psutil.disk_usage(os.sep).percent
        print("|  {}  | {} | {} |".format(str(vMem), str(cpuUtil), str(diskUse)))
        if cpuUtil > 80.0:
            print("WARNING! CPU USAGE HIGH")
            delete_last_line
        time.sleep(2)
        delete_last_line()
        

def delete_last_line():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE) 

start()

