from peewee import *
import os

arq = "especie-plantas.db"
db = SqliteDatabase(arq)

class BaseModelo(Model):
    class Meta:
        database = db

class Planta(BaseModelo):
    nome_planta = CharField()
    nome_cientifico = CharField()
    tam_folha = CharField()
    periodo_poda = CharField()

class Jardim(BaseModelo):
    nome = CharField()

class PlantaDoJardim(BaseModelo):
    data_plantacao = CharField()
    planta = ForeignKeyField(Planta)
    jardim = ForeignKeyField(Jardim)

if os.path.exists(arq):
    os.remove(arq)

db.connect()
db.create_tables([Planta, Jardim, PlantaDoJardim])

rosa = Planta.create(nome_planta = "Rosa", nome_cientifico = "Plantae rosium", tam_folha = "medio", periodo_poda = "120 dias")
jar = Jardim.create(nome = "Jardim la de casa")
plant_jar = PlantaDoJardim.create(data_plantacao = "12/02/2019", planta = rosa, jardim = jar)

for i in PlantaDoJardim.select():
    print("Data plantacao: " +str(i.data_plantacao))
    print("Dados da planta: " +str(i.planta.nome_planta) + " | " +str(i.planta.nome_cientifico ) + " | " + str(i.planta.tam_folha ) + " | " +(i.planta.periodo_poda))
    print("Nome do Jardim: " + str(i.jardim.nome))
