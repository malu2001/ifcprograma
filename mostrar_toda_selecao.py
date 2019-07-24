from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def iniciar():
	#return "foi"
	return render_template("questao2_flask_combox.html")

@app.route("/mostra")
def mostrar_selecao():
	lista = request.args.getlist("estado")
	mensagem  = "Os estados selecionados sao: "
	for i in lista:
		mensagem += i + " "
		
	return mensagem


app.run(debug = True)