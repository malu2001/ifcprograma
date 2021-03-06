from flask import Flask, render_template, session, request, redirect, url_for, json, jsonify

app = Flask(__name__)

lista_global = []

class Pessoa():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf 

app.config["SECRET_KEY"] = "SOUTOP"

@app.route("/")
def inicio():
    return render_template("adicionar_pessoas.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", usuario = lista_global)

@app.route("/add_pessoas")
def add_pessoas():
    nome = request.args.get("nome")
    cpf = request.args.get("cpf")
    pessoa = Pessoa(nome, cpf)
    lista_global.append(pessoa)
    return render_template("listar_pessoas.html", usuario = lista_global)

@app.route("/excluir_pessoas")
def excluir_pessoas():
    nome = request.args.get("nome")
    for i in lista_global:
        if i.nome == nome:
            lista_global.remove(i)
            return render_template("listar_pessoas.html", usuario = lista_global)
        else:
            return "Não encontrado para excluir!"

@app.route("/form_alterar_pessoas")
def form_alterar_pessoas():
    nome = request.args.get("nome")
    for i in lista_global:
        if i.nome == nome:
            return render_template("alterar_pessoas.html", pessoa = i)
        else:
            return "Pessoa não encontrada" + nome


@app.route("/alterar_pessoas")
def alterar_pessoas():
    nome_original = request.args.get("nome_original")
    nome = request.args.get("nome")
    cpf = request.args.get("cpf")
    novo_dado = Pessoa(nome, cpf)
    for i in range(len(lista_global)):
        if lista_global[i].nome == nome_original:
            lista_global[i] = novo_dado
            return redirect(url_for("listar_pessoas"))

@app.route("/form_login")
def form_login():
    return render_template("exemplo1.html")

@app.route("/login", methods=['get'])
def login():
    login = request.args.get("login")
    senha = request.args.get("senha")
    
    if login == "administrador" and senha == "587":
        response = jsonify({'message': 'ok'})
    
    else:
        response = jsonify({'message': 'error'})
        #return "Houve algum erro durante o seu login!"
        
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response



@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/")

app.run(debug = True)