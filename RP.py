import psutil

import os

import time

import sys

import plyer

import platform

import subprocess



TIME_DELAY = 3



def start():

    '''

    This function starts the monitoring process

    '''



    print("\n")

    print("="*50)

    print("System Resources:".center(50))

    print("="*85)



    disp = "| Memory usage | CPU usage | Disk usage |"

    # print(disp.center(0))



    dispList = ['Memory usage', 'CPU usage', 'Disk usage','Down Speed','Up Speed']

    eqSpam = '=' * 85



    print(eqSpam)

    print('{:<12s}{:>12s}{:>12s}'.format(dispList[0],dispList[1],dispList[2]) + "\t\t" + "{:>12s}".format(dispList[3]) + "\t\t" + '{:>12s}'.format(dispList[4]))

    print(eqSpam)



    while(True):

    	

        vMem = psutil.virtual_memory().percent

        cpuUtil = psutil.cpu_percent()

        #cpuFreq = psutil.cpu_freq()

        os.sep

        diskUse = psutil.disk_usage(os.sep).percent

	

        # outDisp = "|  {}  | {} | {} |".format(

            # str(vMem), str(cpuUtil), str(diskUse))



        # print(outDisp.center(40))

        nstat = list(netStatDisplay())[1].strip().split()

        state = netStatDisplay()[0] == True 

        if(state == True):

        	netspeed = list(netSpeedStatDisplay())

        	print('{:<12.1f}{:>12.1f}{:>12.1f}{:>12.1f}{:>12s}{:>12.1f}{:>12s}'.format(vMem,cpuUtil,diskUse,float(netspeed[1][15]),netspeed[1][16],float(netspeed[1][20]),netspeed[1][21]))

	

        

        #print(nstat)

        #nstat = netstat[1]

        #string = nstat[1][0][5:len(nstat[1][0])-] + "  IP: "+ str(nstat[1][2][1:len(nstat[1][2])-1]) + "\t" + str(nstat[1][13]) + "\t" +str(nstat[1][14]) + str(nstat[1][15]) + "\n" + "Packets Received " + str(nstat[1][21]) + " | Packets Transmitted : " + str(nstat[1][25]) + "\n" + "Packet Loss: " + str(nstat[1][26]) + " rtt: " + str(nstat[1][30])

        #string = nstat[1] + "  IP: "+ str(nstat[2][1:len(nstat[2])-1]) + "\t" + str(nstat[13]) + "\t" +str(nstat[14]) + str(nstat[15]) + "\n" + "Packets Received" + str(nstat[21]) + " | Packets Transmitted : " + str(nstat[24]) + "\n" + "Packet Loss: " + str(nstat[26]) + " rtt: " + str(nstat[30])

        	string = nstat[1] + "  IP: "+ str(nstat[2][1:len(nstat[2])-1]) + "\t" + str(nstat[13]) + "\t" +str(nstat[14]) + str(nstat[15]) + "\n" 	+ "Packets Received : " + str(nstat[21]) + " | Packets Transmitted : " + str(nstat[24]) + "\n" + "Packet Loss: " + str(nstat[26]) + " rtt: " + 	str(nstat[30])

        	print(string)

        else:

        	print("PING OFFLINE")

        	netspeed = list(netSpeedStatDisplay())

        	print('{:<12.1f}{:>12.1f}{:>12.1f}'.format(vMem,cpuUtil,diskUse))

	

        if cpuUtil > 80.0:

            CPUnotif()



        if vMem > 70.0:

            memNotif()



        if diskUse > 90.0:

            diskNotif()



        time.sleep(TIME_DELAY)

        delete_last_line(state)



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



def delete_last_line(state):

    '''

    This function refreshes resource variables

    '''

		

    CURSOR_UP_ONE = '\x1b[1A'

    ERASE_LINE = '\x1b[2K'

    if (state == True):

    	for i in range(4):

        	sys.stdout.write(CURSOR_UP_ONE)

        	sys.stdout.write(ERASE_LINE)

    else:

    	for i in range(2):

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
    os.system("cls | clear") #cls works for windows, and clear works for unix systems

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

def netSpeedStatDisplay():

    

    speed = subprocess.run(['vnstat','-tr','2'],

    			   stdout = subprocess.PIPE,

    			   stderr = subprocess.PIPE,

    			   encoding = 'utf-8')

    if speed.returncode == 0:

        return True, speed.stdout.strip().split()

    else:

        return False, speed.stderr

    return speed



introScreenLogo()

fetchSystemInfo()

#start()