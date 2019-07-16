from peewee import *

db = SqliteDatabase("livrariatop.db")

class BaseModelo(Model):
    class Meta:
        database = db

class Comida(BaseModelo):
    nome = CharField()

class Doador(BaseModelo):
    nome = CharField
    doa = ManyToManyField(Comida)

class Receptor(BaseModelo):
    nome = CharField()
    recebe = ManyToManyField(Comida)

db.connect()
db.create_tables([Comida, Doador, Receptor, Doador.doa.get_through_model(), Receptor.recebe.get_through_model])

comida = Comida.create(nome = "Arroz")
doador1 = Doador.create(nome = "Seila da Silva")
receptor1 = Receptor.create(nome = "Ciclano")

doador1.doa.add(comida)
receptor1.recebe.add(comida)

for i in doador1.doa:
    print(i.nome)


