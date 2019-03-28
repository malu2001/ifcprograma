from flask import Flask, render_template, request 
from classe_flask import Pessoa

lista_global= []

class Pessoa():
    def __init__(self, nome, endereco, cpf):
        self.nome = nome
        self.endereco = endereco
        self. cpf = cpf


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("cadastro.html", usuarios = lista_global)

@app.route("/cadastro")
def adicionar_pessoa():
    nome=request.args.get("nome")
    endereco=request.args.get("endereco")
    cpf = request.args.get("cpf")
    pessoa = Pessoa(nome, endereco,cpf)
    lista_global.append(pessoa)
    return render_template ("exibir_mensagem.html", usuarios = lista_global)


@app.route("/excluir_pessoa")
def excluir_pessoa():
    nome=request.args.get("nome")
    ponteiro=None
    for i in lista_global:
        if i.nome==nome:
            ponteiro=i
            break 
    if ponteiro is not None: 
        lista_global.remove(ponteiro)
        return render_template("exibir_mensagem.html", usuarios = lista_global)
        
    
app.run()



  
""" 
nome=request.args.get("nome")
    for i in lista_global:
        if i.nome==nome:
            lista_global.remove(i)
            return render_template ("exibir_mensagem.html", usuarios=lista_global)
"""
