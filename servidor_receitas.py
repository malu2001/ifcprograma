from flask import Flask, render_template, request, redirect
from peewee import *
from modelo_peewee_receitas import *

lista_receitas = []
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_receita.html")

@app.route("/listar_receita")
def listar_receita():
    return render_template("listar_receita.html", lista_receitas = Receita.select())

@app.route("/listar_ingredientes_receita")
def listar_ingredientes_receita():
    receita_id = int(request.args.get("receita_id"))
    receita = Receita.get_by_id(receita_id)
    ings = IngredienteDaReceita.select().where(IngredienteDaReceita.receita == receita)
    return render_template("listar_ingre_receitas.html", receita = receita, ings = ings)

app.run(debug = True)