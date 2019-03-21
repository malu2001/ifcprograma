from flask import Flask, render_template, request 
from classe_flask import Pessoa

app = Flask(__name__)

@app.route("/")
def hello():
    lista  = [Pessoa("Ana", "rua 08", "54654185418"),
        Pessoa("Amanda", "rua 09", "54654185555"),
        Pessoa("Maria", "rua 78", "5465418999999")]
    return render_template("cadastro.html", usuarios = lista)

@app.route("/adicionar_pessoa")
def adicionar_pessoa():
    nome=request.args.get("nome")
    endereco=request.args.get("endereco")
    lista =[nome, endereco]
    return render_template ("exibir_mensagem.html", usuario = lista)
    
app.run()



