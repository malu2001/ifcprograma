from peewee import *
import os

arq = "jardim-plantas.db"
db = SqliteDatabase(arq)

class BaseModelo(Model):
    class Meta:
        database = db

class Planta(BaseModelo):
    nome_planta = CharField()
    nome_cientifico = CharField()
    tam_folha = CharField()

class Jardineiro(BaseModelo):
    nome = CharField()

class Jardim(BaseModelo):
    planta = ManyToManyField(Planta)
    jardineiro = ForeignKeyField(Jardineiro)

if os.path.exists(arq):
    os.remove(arq)

db.connect()
db.create_tables([Planta, Jardineiro, Jardim, Jardim.planta.get_through_model()])

rosa = Planta.create(nome_planta = "Rosa", nome_cientifico = "Plantae rosium", tam_folha = "medio")
joao = Jardineiro.create(nome = "Joao")
jardim = Jardim.create(jardineiro = joao)

jardim.planta.__add__(rosa)

todos = Jardim.select()


for i in jardim.planta:
    print(i.planta.nome_planta)
    print(i.planta.nome_cientifico)
    print(i.planta.tam_folha)