from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        form_entries = {
            "name_entry": request.form.get("nome"),
            "email_entry": request.form.get("email"),
            "assunto_entry": request.form.get("assunto"),
            "mensagem_entry": request.form.get("mensagem")
        }
        print(form_entries)        
    return render_template("home.html")