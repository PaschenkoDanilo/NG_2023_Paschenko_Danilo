from flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask("News Feed", template_folder = 'template')

def sendDataToIndex():
    file = open("News.txt", "a")
    file.write("<h1>" + request.args.get("title") + "</h1>" + "\n")
    time = datetime.now()
    file.write("<h4>" + time.strftime('%Y-%m-%d') + "</h4>" + "\n")
    file.write("<h2>" + request.args.get("text") + "</h2>" + "\n")
    file.write("<hr />" + "\n")
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

@app.route('/enter')
def enter():
    login = request.args.get('login')
    password = request.args.get('password')
    if login == "admin" and password == "admin":
        return redirect('/admin')
    else:
        return render_template("enter.html")

@app.route('/admin')
def admin():
    dataFromFile = ""
    file = open("News.txt", "r")
    for line in file.readlines():
        dataFromFile += line
    file.close()
    return render_template('admin.html', content="<textarea name=\"saveEdit\">" + dataFromFile + "</textarea>")

@app.route('/clearAllNews')
def clearAllNews():
    file = open("News.txt", "w+")
    file.close()
    return redirect('/admin')

@app.route('/saveEdits')
def saveEdit():
    edits = request.args.get("saveEdit")
    print (edits)
    file = open("News.txt", "w+")
    file.write(str(edits))
    file.close()
    return redirect('/admin')

app.run(host="0.0.0.0", port=8081)