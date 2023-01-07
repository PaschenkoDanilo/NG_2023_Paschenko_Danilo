import platform
import psutil
import socket

def createFile():
    file = open("PCInfo.txt", "w+")
    file.close()
    return file

def cpuInfo():
    file = open("PCInfo.txt", "a")
    file.write ("CPU:" + "\n")
    file.write ("\t" + platform.processor() + "\n" + "\n")
    file.close()

def cpuArchitectureInfo():
    file = open("PCInfo.txt", "a")
    file.write ("CPU Architecture:" + "\n")
    file.write ("\t" + platform.machine() + "\n" + "\n")
    file.close()

def osName():
    file = open("PCInfo.txt", "a")
    file.write ("Operating System Name:" + "\n")
    file.write ("\t" + platform.system() + "\n" + "\n")
    file.close()

def osInfo():
    file = open("PCInfo.txt", "a")
    file.write ("Operating System Information:" + "\n")
    file.write ("\t" + platform.platform() + "\n" + "\n")
    file.close()

def ramAmount():
    file = open("PCInfo.txt", "a")
    file.write ("RAM Amount:" + "\n")
    file.write ("\t" + str(psutil.virtual_memory()) + "\n" + "\n")
    file.close()

def hostName():
    file = open("PCInfo.txt", "a")
    file.write ("Host Name:" + "\n")
    file.write ("\t" + socket.gethostname() + "\n" + "\n")
    file.close()

def systemIpAddress():
    file = open("PCInfo.txt", "a")
    file.write ("System IP-Address:" + "\n")
    pcHostName = socket.gethostname()
    file.write ("\t" + socket.gethostbyname(pcHostName) + "\n" + "\n")
    file.close()

def diskAmount():
    file = open("PCInfo.txt", "a")
    file.write ("Disk Amount:" + "\n")
    file.write ("\t" + str(psutil.disk_usage('/')) + "\n" + "\n")
    file.close()