from flask import Flask,render_template,request
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

lista_global = Comida.select()
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

@app.route("/excluir_comida", methods = ['POST'])
def excluir_comida():
    Comida(nome = request.form["nome"])
    for i in Comida.select():
        if i.nome == Comida.nome:
            Comida.delete_instance(i)
    return render_template("exibir_comidas.html", lista_comidas = Comida.select)

db.connect()
db.create_tables([Comida])

app.run(debug = True)