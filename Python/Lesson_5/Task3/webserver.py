from flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask("News Feed", template_folder = 'template')

def sendDataToIndex():
    file = open("News.txt", "a")
    file.write("<h1>" + request.args.get("title") + "</h1>")
    time = datetime.now()
    file.write("<h4>" + time.strftime('%Y-%m-%d') + "</h4>")
    file.write("<h2>" + request.args.get("text") + "</h2>")
    file.write("<hr />")
    file.close()

@app.route('/')
def index():
    dataFromFile = ""
    file = open("News.txt", "r")
    for line in file.readlines():
        dataFromFile += line
    file.close()
    return render_template("index.html", content=dataFromFile)

@app.route('/editor')
def editor():
    try:
        sendDataToIndex()
    except:
        return render_template("editor.html")
    return redirect('/')

app.run(host="0.0.0.0", port=8081)