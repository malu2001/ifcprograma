from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def iniciar():
	return render_template("inicio.html")

@app.route("/mostrar_selecao")
def mostrar_selecao():
	lista = request.args.getlist("estado")
	mensagem  = "Os estados selecionados sao: "
	for i in lista:
		mensagem += i + " "
		
	return mensagem
