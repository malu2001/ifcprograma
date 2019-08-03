from flask import Flask,render_template,request, redirect
from peewee import *
import os

arq = "comida.db"
db = SqliteDatabase(arq)

class BaseModelo(Model):
    class Meta:
        database = db

class Comida(BaseModelo):
    nome =  CharField()
    categoria = CharField()
    vencimento = CharField()

lista_global = []
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("listar_comida.html", lista_comidas  = Comida.select())

@app.route("/listar_comidas", methods = ['POST'])
def listar_comidas():
    return render_template("listar_comida.html", lista_comidas = Comida.select())


@app.route("/inserir_comida", methods = ['POST'])
def inserir_comida():
    Comida.create (nome = request.form ["nome"], categoria = request.form ["categoria"], vencimento = request.form["vencimento"])
    return render_template("exibir_comidas.html", lista_comidas = Comida.select())

@app.route("/excluir_comida")
def excluir_comida():
    Comida.delete_by_id(request.args.get("id"))
    return redirect("/")

@app.route("/form_alterar_comida")
def form_alterar_comida():
    pegar_comida = Comida.get_by_id(request.args.get("id"))
    return render_template("alterar_comida.html", comida = pegar_comida)

@app.route("/alterar_comida", methods = ["POST"])
def alterar_comida():
    comida = Comida.get_by_id(request.form["id"])
    comida.nome = request.form["nome"]
    comida.categoria = request.form["categoria"]
    comida.vencimento = request.form["vencimento"]
    comida.save()
    return render_template("listar_comida.html")
   
db.connect()
db.create_tables([Comida])

app.run(debug = True)