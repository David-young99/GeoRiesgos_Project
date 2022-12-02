from flask import Flask, request, render_template, jsonify

datos = [{}]

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("form.html")

@app.route("/form", methods = ["POST"])
def form():
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
    }
                ]

        return render_template("form_final.html")


@app.route("/json/bridge")
def json():
    
   return jsonify(datos)


