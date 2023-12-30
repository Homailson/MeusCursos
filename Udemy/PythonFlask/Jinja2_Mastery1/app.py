from flask import Flask, render_template

#Criando uma nova aplicação Flask
app = Flask(__name__)

todos = [
        ("Comprar pão", True), 
        ("Fazer curso da Udemy", False)
        ]

@app.route("/")
def todo():
    return render_template("home.html",todos = todos)


@app.route("/<string:todo>")
def todo_item(todo: str):
    for text, completed in todos:
        if text == todo:
            completed_text = "[x]" if completed else "[ ]"
            title = f"{completed_text} - Todos"
            return render_template("todo.html", text=text, completed=completed, title=title)
    else:
        return render_template("not-found.html", text=todo, title="Not found")