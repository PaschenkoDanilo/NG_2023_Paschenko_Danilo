import platform
import psutil
import socket

def createFile():
    file = open("PCInfo.db", "w+")
    file.close()
    return file

def cpuInfo():
    return platform.processor()

def cpuArchitectureInfo():
    return platform.machine()

def osName():
    return platform.system()

def osInfo():
    return platform.platform()

def ramAmount():
    return str(psutil.virtual_memory())

def hostName():
    return socket.gethostname()

def systemIpAddress():
    pcHostName = socket.gethostname()
    return socket.gethostbyname(pcHostName)

def diskAmount():
    return str(psutil.disk_usage('/'))