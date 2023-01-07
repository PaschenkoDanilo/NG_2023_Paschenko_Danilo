from task1RecordInFile import *
from rich.console import Console
import time

console = Console()

variants = {"a": "CPU",
"b": "CPU Architecture",
"c": "Operating System Name",
"d": "Operating System Information",
"e": "RAM Amount",
"f": "Host Name",
"g": "System IP-Address",
"h": "Disk Amount"
}

def menu(switching):
    for variant in variants:
        print(variant + ") " + variants[variant] + " [" + str(noToYes(switching[variant])) + "]")
    console.rule("")
    console.print("[blue]y) Proceed")


def userChoice(switching):
    menu(switching)
    variantChoice = console.input("[blue]Choose your variant: ")
    console.rule("")
    return variantChoice

def start():
    switching = modes()
    modesFunctions = modes()
    while True:
        choice = userChoice(switching)
        if choice == "y":
            recordInFile(modesFunctions)
            break
        elif choice == "a" or choice == "b" or choice == "c" or choice == "d" or choice == "e" or choice == "f" or choice == "g" or choice == "h":
            if switching[choice] == False:
                switching[choice] = True
            elif switching[choice] == True:
                switching[choice] = False
            modesForRecordInFileFunctions(switching, choice, modesFunctions)
        else:
            with console.status("[red]Your variant invalid"):
                time.sleep(1.5)
            continue

def modes():
    switching = {}
    for variant in variants:
        switching[variant] = False
    return switching

def noToYes(logical):
    if logical == True:
        return "yes"
    else:
        return "no"

def modesForRecordInFileFunctions(switching, choice, modesFunctions):
    if noToYes(switching[choice]) == "yes":
        modesFunctions[choice] = True
    elif noToYes(switching[choice]) == "no":
        modesFunctions[choice] = False
    return modesFunctions

def recordInFile(modesFunctions):
    with console.status("[gray0]Working... A few seconds", spinner = "bouncingBall"):
        time.sleep(2.5)
        createFile()
        if modesFunctions["a"] == True:
            cpuInfo()
        if modesFunctions["b"] == True:
            cpuArchitectureInfo()
        if modesFunctions["c"] == True:
            osName()
        if modesFunctions["d"] == True:
            osInfo()
        if modesFunctions["e"] == True:
            ramAmount()
        if modesFunctions["f"] == True:
            hostName()
        if modesFunctions["g"] == True:
            systemIpAddress()
        if modesFunctions["h"] == True:
            diskAmount()
        
        console.print("[bold green]Successfully completed", justify = "center")
        console.print("[bold green]Check file PCInfo.txt", justify = "center")

def main():
    with console.status("[gray0]Launching the program", spinner = "dots"):
        time.sleep(1.5)
        console.rule("[bold green]Program started")
    start()

main()