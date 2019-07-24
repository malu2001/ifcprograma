from peewee import *


db = SqliteDatabase("saude2.db")

class BaseModelo(Model):
    class Meta():
        database = db

class Ocorrencia (BaseModelo):
    descricao = CharField ()

class Registro(BaseModelo):
    data = CharField
    sintomas = ForeignKeyField(Ocorrencia)
    intensidade = CharField()
    observacoes = CharField()

    def __str__(self):
        return ("No dia: "  +  " "  + self.data  + "a pessoas teve o sintoma(s): " + " " + self.sintomas + " " +  " " + "na qual a intensidade foi: " +  " " + self.intensidade + "Observacao: " + " " + self.observacoes) 
    

db.connect()
db.create_tables([Ocorrencia, Registro])


dor = Ocorrencia.create(descricao = "dor de cabeça")
registro = Registro.create(data = "17/08/2070", sintomas = dor, intensidade = "2", observacoes = "Pq comi amendoim")

print(registro.data)
print(registro.sintomas)
print(registro.intensidade)
print(registro.observacoes)