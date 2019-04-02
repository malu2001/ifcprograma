from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(listar_livros.html)

app.run()