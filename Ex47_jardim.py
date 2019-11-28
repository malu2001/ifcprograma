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

class Jardim(BaseModelo):
    plantas = ManyToManyField(Planta)
    nome = CharField()

if os.path.exists(arq):
    os.remove(arq)

db.connect()
db.create_tables([Planta, Jardim, Jardim.plantas.get_through_model()])

rosa = Planta.create(nome_planta = "Rosa", nome_cientifico = "Plantae rosium", tam_folha = "medio")
jardim = Jardim.create(nome = "Jardim Ipiranga")

jardim.plantas.__add__(rosa)

