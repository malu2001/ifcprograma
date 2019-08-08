from peewee import *
import os

arq = "exames.db"
db = SqliteDatabase(arq)

class BaseModelo(Model):
    class Meta:
        database = db

class Paciente(BaseModelo):
    nome_paciente = CharField()

class Exame(BaseModelo):
    nome_exame = CharField()
    preco = CharField()
    prazo = CharField()

class Requisicao(BaseModelo):
    exame = ForeignKeyField(Exame)
    paciente = ForeignKeyField(Paciente)
    data_requisicao = CharField()
    nome_medico = CharField()

if os.path.exists(arq):
    os.remove(arq)

db.connect()
db.create_tables([Paciente, Exame, Requisicao])

jose = Paciente.create(nome_paciente = "Jose")
exame_sangue = Exame.create(nome_exame = "Exame de Sangue", preco = "35.00", prazo = "12/08/2019")
requisicao = Requisicao.create(exame = exame_sangue, paciente = jose, data_requisicao = "01/08/2019", nome_medico = "Judileine")

todos = Requisicao.select()

print("----------------------------------------------")

for req in todos:
    print("DATA REQUISICAO: " + str(req.data_requisicao) + "|" +  " NOME MEDICO: " + str(req.nome_medico) + "|" + "PACIENTE: " +str(req.paciente.nome_paciente))
    print("EXAME: " +str(req.exame.nome_exame), "|" + "PRECO: " +str(req.exame.preco) +  "|" + "PRAZO: " + str(req.exame.prazo))

print("----------------------------------------------")


