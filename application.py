from flask import Flask, request, render_template, jsonify
import datetime, pytz
from datetime import date

datos = [{}]
now = datetime.datetime.now(pytz.timezone("America/Costa_Rica"))

today = date.today().strftime("%d/%m/%Y")
h = now.hour
m = now.minute
time = str(h) + ":" + str(m) + ":"


application = Flask(__name__)

@application.route("/")
def template():
    return render_template("form.html")


@application.route("/form", methods = ["POST"])
def form():
        import datetime as dt
        import pytz

        register = dt.datetime.now(pytz.timezone("America/Costa_Rica"))
        today = date.today().strftime("%d/%m/%Y")
        h = now.hour
        m = now.minute
        time = str(h) + ":" + str(m) + ":"
        
        name = request.form["name"]
        email = request.form["email"]
        alert = request.form["alert"]
        details = request.form["details"]


        global datos
        datos = [
    {
        "name": name
    },
    {
        "email": email
    },
    {
        "alert": alert
    },
    {
        "details": details
    },
    {
        "date" : today
    },
    {
        "time" : time
    }
                ]
    
        
        json()
        status()

        return render_template("form.html")
    
        
@application.route("/json/status")
def status():

    status = [{
        "date" :  today
    },
    {
        "time" : time
    }]

    return jsonify(status)

    

@application.route("/json/bridge")
def json():
    
   return jsonify(datos)

if __name__=='__main__':
    application.run(debug=False) 
