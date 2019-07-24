from peewee import *
import os

arq = 'doacaoProva2.db'
db = SqliteDatabase(arq)

class BaseModelo(Model):
    class Meta:
        database = db

class TipoDestinatario(BaseModelo):
    descricao = CharField()

class Doacao(BaseModelo):
    item_doado = CharField()
    data = CharField()
    observacao = CharField()
    doacao_registro = ForeignKeyField(TipoDestinatario)


if os.path.exists(arq):
    os.remove(arq)


db.connect()

db.create_tables([TipoDestinatario, Doacao])

tip = TipoDestinatario.create(descricao = "Esta doacao foi feita para ajudar as pessoas")
registro = Doacao.create(item_doado = "Bicicleta", data = "01/03/2019", observacao  = "Amigo do ciclano", doacao_registro = tip)

print(registro.item_doado)
print(registro.doacao_registro)