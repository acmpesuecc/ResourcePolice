import psutil
import os
import time

while(True):
    vMem = psutil.virtual_memory().percent
    cpuUtil = psutil.cpu_percent()
    cpuFreq = psutil.cpu_freq()
    cpuTemp = psutil.sensors_temperture()
    os.sep
    diskUse = psutil.disk_usage(os.sep).percent
    print("Memory used: "+ str(vMem), "| CPU used: " + str(cpuUtil), "| CPU core frequency: " + str(cpuFreq),"| Disk used: " + str(diskUse))
    time.sleep(2)
    if cpuUtil > 80.0:
        print("WARNING! CPU USAGE HIGH")
