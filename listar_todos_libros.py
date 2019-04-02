from flask import Flask, render_template
app = Flask(__name__)


class Livro(object):
    def __init__(self, titulo, autor, publicacao, editora):
        self.titulo = titulo
        self.autor = autor
        self.publicacao = publicacao
        self.editora = editora


@app.route("/")
def hello():
    return render_template(listar_livros.html)


@app.route("/listar_livros")
def listar_livros():
    livros = [
        Livro("HP - Pedra Filosofal", "J.K. Rowling", 2001, "ROCCO"),
        Livro("Crimes de Grindewald", "J.K. Rowling", 2018, "ROCCO")
    ]
    return render_template("listar_livros.html", lista_livros = livros)

app.run()