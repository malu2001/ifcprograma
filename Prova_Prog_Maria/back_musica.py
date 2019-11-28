from flask import Flask, jsonify
from playhouse.shortcuts import model_to_dict
from modelo_musica2 import *

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Esse é o backend"
    
@app.route("/listar_elementos")
def listar_elementos():
    pagamentos = list(map(model_to_dict, Pagamento.select()))
    return jsonify ({'lista' :pagamentos})


app.run (debug = True, port = 4999)