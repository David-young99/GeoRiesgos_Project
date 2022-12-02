from flask import Flask, request, render_template, jsonify

datos = [{}]

application = Flask(__name__)

@application.route("/")
def template():
    return render_template("form.html")

@application.route("/form", methods = ["POST"])
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


@application.route("/json/bridge")
def json():
    
   return jsonify(datos)


#if __name__=='__main__':
#    app.run(debug=False, port=5000)
