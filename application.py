from flask import Flask, request, render_template, jsonify

datos = [{}]

application = Flask(__name__)

@application.route("/")
def template():
    return render_template("form.html")



@application.route("/form", methods = ["POST"])
def form():
        import datetime as dt
        from datetime import date
        import pytz

        register = dt.datetime.now(pytz.timezone("America/Costa_Rica"))
        
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
        "id" : 0
    }
                ]
    
        
        
        return render_template("form.html")
        


@application.route("/json/bridge")
def json():
    
   return jsonify(datos)


if __name__=='__main__':
    application.run(debug=False) 
