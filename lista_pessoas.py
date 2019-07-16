from flask import Flask, render_template, request 


lista_global= []

class Pessoa():
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone=telefone


app = Flask(__name__)

@app.route("/")
def listar_pessoas():
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

@app.route("/form_editar_pessoa")
def form_alterar():
    nome=request.args.get("nome")
    for p in lista_global:
        if p.nome==nome:
            return render_template("form_alterar_pessoa.html", pessoa=p)
    return "pessoa não encontrada" +nome 

@app.route("/alterar_pessoa")
def alterar_pessoa():
    procurar=request.args.get("nome_original")
    nome=request.args.get("nome")
    endereco=request.args.get("endereco")
    telefone=request.args.get("telefone")
    novo=Pessoa(nome,endereco,telefone)
    for i in range(len(lista_global)):
        if lista_global[i].nome==procurar:
            lista_global[i]=novo
            return redirect(url_for("listar_pessoas"))
    return "Pessoa não encontrada:" + procurar
    
app.run()



  
""" 
nome=request.args.get("nome")
    for i in lista_global:
        if i.nome==nome:
            lista_global.remove(i)
            return render_template ("exibir_mensagem.html", usuarios=lista_global)
"""
