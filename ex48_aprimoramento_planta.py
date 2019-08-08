from peewee import *
import os

arq = "especie-plantas.db"
db = SqliteDatabase(arq)

class BaseModelo(Model):
    class Meta:
        database = db

class Especie(BaseModelo):
    periodo_poda = CharField()
    data_plantacao = CharField()

class Planta(BaseModelo):
    nome_planta = CharField()
    nome_cientifico = CharField()
    tam_folha = CharField()
    especie = ForeignKeyField(Especie)

class Jardim(BaseModelo):
    nome = CharField()
    plantas = ManyToManyField(Planta)

if os.path.exists(arq):
    os.remove(arq)

db.connect()
db.create_tables([Especie, Planta, Jardim, Jardim.plantas.get_through_model()])

espe = Especie.create(periodo_poda = "3 dias", data_plantacao = "12/08/2017")
rosa = Planta.create(nome_planta = "Rosa", nome_cientifico = "Plantae rosium", tam_folha = "medio", especie = espe)
jar = Jardim.create(nome = "Jardim la de casa")

