from peewee import *

db = SqliteDatabase("livrariatop.db")

class BaseModelo(Model):
    class Meta():
        database = db

class Categoria(BaseModelo):
    denominacao = CharField()

class Ator(BaseModelo):
    nome = CharField()

class Livro(BaseModelo):
    titulo = CharField()
    ator = ForeignKeyField(Ator)
    categoria = ForeignKeyField(Categoria)

db.connect()
db.create_tables([Categoria, Ator, Livro])

cate = Categoria.create(denominacao = "seila")
at = Ator.create(nome = "jk")
livro = Livro.create(titulo = "hp", ator = at, categoria = cate)

print(livro.titulo)
print(livro.ator)
print(livro.categoria)