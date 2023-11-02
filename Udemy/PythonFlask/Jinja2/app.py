from flask import Flask, render_template


app = Flask(__name__)


class CarrosBrasileiros:
    def __init__(self, marca, modelo, ano, qtd_rodas, qtd_portas, qtd_lugares):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.qtd_rodas=qtd_rodas
        self.qtd_portas=qtd_portas
        self.qtd_lugares=qtd_lugares



@app.route("/data-structures/")
def render_data_structures():

    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A beautiful Mind"
    ]

    car = {
        "brand": "Chevrolet",
        "model": "Monza",
        "year": "1990"
    },

    carro = CarrosBrasileiros("Gurgel", "BR-800", "1990", "4", "2", "4")

    kwargs = {
        "movies": movies,
        "car": car,
        "carro": carro
    }
 

    return render_template("data_structures.html", **kwargs)


@app.route("/condicionais-basicas/")
def render_conditional():
    # company = "Apple"
    company = "Microsoft"
    return render_template("conditional_basics.html", company=company)


@app.route("/for-loop/")
def render_loops_for():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]

    return render_template("for_loop.html", planets=planets)


@app.route("/for-loop-condicionais/")
def render_for_loop_conditionais():
    user_os = {
        "Bob_Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Slvatierra": "Windows"
    }

    return render_template("loops_and_conditionals.html", user_os=user_os)