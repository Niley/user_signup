from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

def isfine(inputz):
    if " " in inputz:
        return False
    if len(inputz) > 20:
        return False
    if len(inputz) < 3:
        return False
    return True

def isemail(em):
    if re.match(r"[^@]+@[^@]+\.[^@]+", em):
        return True
    if em == "":
        return True
    return False

@app.route("/submit", methods=['POST'])
def submit_info():
    errorfree = True
    usrnm = request.form["username"]
    usrnm = cgi.escape(usrnm, quote = True)
    password = request.form["password"]
    password = cgi.escape(password, quote = True)
    repeat = request.form["pwrepeat"]
    repeat = cgi.escape(repeat, quote = True)
    email = request.form["email"]
    email = cgi.escape(email, quote = True)

    if not isfine(usrnm):
        errorun = "Fix your username!"
        usrnm = ""
        errorfree = False
    else:
        errorun = ""
    if not isfine(password):
        errorpw = "Password invalid!"
        errorfree = False
    else:
        errorpw = ""
    if password != repeat:
        errorpwr = "Type the SAME password here!"
        errorfree = False
    else:
        errorpwr = ""
    if not isemail(email):
        erroremail = "Wrong email format!"
        errorfree = False
        email = ""
    else:
        erroremail = ""

    if errorfree:
        return render_template("complete.html", username = usrnm)

    return render_template("edit.html", username = usrnm, email = email, error_un = errorun, error_pw = errorpw, error_pwr = errorpwr, error_email = erroremail)



@app.route("/")
def index():
    errorz = request.args.get("error")
    return render_template("edit.html")



app.run()
