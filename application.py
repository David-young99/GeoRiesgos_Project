from flask import Flask, request, render_template, jsonify

datos = [{}]

application = Flask(__name__)
app = application

@application.route("/")
def template():
    return render_template("form.html")

@application.route("/form", methods = ["POST"])
def form():
        name = request.form["name"]
        email = request.form["email"]
        alert = request.form["alert"]
        details = request.form["details"]
        val = 0
        id = val + 1

        
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
        "id": id
    }
                ]

        return render_template("form_final.html"), val+1


@application.route("/json/bridge")
def json():
    
   return jsonify(datos)


if __name__=='__main__':
    application.run(debug=False)
