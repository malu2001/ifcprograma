from peewee import *
import os

arq = "receitas.db"
db = SqliteDatabase(arq)

class BaseModelo(Model):
    class Meta:
        database = db

class Receita(BaseModelo):
    titulo = CharField()

class Ingrediente(BaseModelo):
    nome_ingrediente = CharField()

class IngredienteDaReceita(BaseModelo):
    receita = ForeignKeyField(Receita)
    ingrediente = ForeignKeyField(Ingrediente)
    qtd = FloatField()


if __name__ == "__main__":
    if os.path.exists:
        os.remove(arq)

    db.connect()
    db.create_tables([Receita, Ingrediente, IngredienteDaReceita])

    bolo = Receita.create(titulo = "bolo")
    ingre = Ingrediente.create(nome_ingrediente = "farinha, ovo")
    ingre_receita = IngredienteDaReceita.create(receita = bolo, ingrediente = ingre, qtd = 400 )

    #print(ingre_receita.receita.titulo)
    #print(ingre_receita.ingrediente.nome_ingrediente)

    #Para listar os ingredientes da receita, basta:

    for i in Receita.select():
        print(i.titulo)
        ings = IngredienteDaReceita.select().where(IngredienteDaReceita.receita == i)
        print("Ingredientes:")
        for p in ings:
            print(p.ingrediente.nome_ingrediente)