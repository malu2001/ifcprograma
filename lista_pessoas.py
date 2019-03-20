from flask import Flask, render_template
from classe_flask import Pessoa


app = Flask(__name__)
@app.route("/")

def hello():

    lista  = [Pessoa("Ana", "rua 08", "54654185418"),
        Pessoa("Amanda", "rua 09", "54654185555"),
        Pessoa("Maria", "rua 78", "5465418999999")]
    return render_template("cadastro.html", usuarios = lista)

app.run()

