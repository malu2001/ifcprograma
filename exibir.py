from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def exibir():
	return render_template("cadastro_hylson.html")

app.run()
