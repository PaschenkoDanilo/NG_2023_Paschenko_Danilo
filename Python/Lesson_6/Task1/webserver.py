from databaseWorker import *
from flask import Flask, render_template, redirect, request

app = Flask("Chat", template_folder = "template")
prepareDb("userLoginMessage.db")

login = ""

@app.route('/')
def index():
    rows = getLoginsAndMessages("userLoginMessage.db")
    saveLogin = "<textarea name=\"login\" id=\"textareaLoginAlign\" required>" + str(login) + "</textarea>"
    return render_template("index.html", message=generateUsersHTMLTable(rows), loginInput = saveLogin)

@app.route('/message')
def userMessage():
    global login
    login = request.args.get("login")
    message = request.args.get("message")
    registerUserMessage("userLoginMessage.db", login, message)
    return redirect('/')

@app.route('/refreshThePage')
def refreshThePage():
    return render_template("index.html")

app.run(host = "0.0.0.0", port = 8081)