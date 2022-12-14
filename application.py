from flask import Flask, request, render_template, jsonify
import datetime, pytz
from datetime import date


application = Flask(__name__)

@application.route("/")
def template1():
    return render_template("form.html")


@application.route("/form", methods = ["POST"])
def form():
        import datetime as dt
        import pytz

        global datos, today, time
        now = dt.datetime.now(pytz.timezone("America/Costa_Rica"))
        today = date.today().strftime("%d/%m/%Y")
        h = now.hour
        m = now.minute
        time = str(h) + ":" + str(m) + ":"
        
        name = request.form["name"]
        email = request.form["email"]
        alert = request.form["alert"]
        details = request.form["details"]


        
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
       
        return render_template("form.html")

@application.route("/json/bridge")
def json():
    
   return jsonify(datos)

    
@application.route("/json/status")
def status():

    status = [{
        "date" :  today
    },
    {
        "time" : time
    }]

    return jsonify(status) 


if __name__=='__main__':
    application.run(debug=False, port=5000) 
