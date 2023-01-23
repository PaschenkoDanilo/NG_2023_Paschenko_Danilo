from flask import Flask, render_template, redirect, request
from databaseWorker import *
from task2RecordInFile import *

app = Flask("PC Information", template_folder = "template")

createFile()
prepareDb('PCInfo.db')

variants = ["CPU", "CPU Architecture", "Operating System Name", "Operating System Information", "RAM Amount", "Host Name", "System IP-Address", "Disk Amount"]
gatheringInformationFunctions = [cpuInfo(), cpuArchitectureInfo(), osName(), osInfo(), ramAmount(), hostName(), systemIpAddress(), diskAmount()]

def modes():
    choiceInformation = {}
    for variant in variants:
        choiceInformation[variant] = request.args.get(variant)
    return choiceInformation

@app.route('/')
def index():
    rows = getComponentAndInformation("PCInfo.db")
    return render_template("index.html", pcInfo = generatePCInfoHTMLTable(rows))

@app.route('/gatheringInformation')
def gatheringInformation():
    createFile()
    prepareDb('PCInfo.db')
    choiceInformation = modes()
    functionIndex = 0
    for variant in variants:
        if choiceInformation[variant] == "on":
            registerComponentAndInformation("PCInfo.db", variant, gatheringInformationFunctions[functionIndex])
            functionIndex += 1
        else:
            functionIndex += 1
    return redirect('/')

app.run(host="0.0.0.0", port=8081)