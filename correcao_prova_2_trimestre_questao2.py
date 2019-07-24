from peewee import *
import os

arq = "viagens.db"
db = SqliteDatabase(arq)

class BaseModelo(Model):
    class Meta:
        database = db

class Atividade(BaseModelo):
   nome_atividade = CharField() 


class Local(BaseModelo):
    nome_local = CharField()


class Viagem(BaseModelo):
    atividade = ForeignKeyField(Atividade)
    local = ForeignKeyField(Local)
    data = CharField()


class Pessoa(BaseModelo):
    nome = CharField()
    viagem = ForeignKeyField(Viagem)


if os.path.exists (arq):
    os.remove(arq)

db.connect()
db.create_tables([Atividade, Local, Viagem, Pessoa])

ativi = Atividade.create(nome_atividade = "Templos Gregos")
locali = Local.create(nome_local = "Grécia")
viagem1 = Viagem.create(atividade = ativi, local = locali, data = "25/11/2025")
pessoa = Pessoa.create(nome = "Maria Luisa Mognon", viagem = viagem1) 

print(pessoa.viagem.data)

