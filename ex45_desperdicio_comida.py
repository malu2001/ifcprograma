from peewee import *
import os, datetime

arq = "desperdicios5.db"
db = SqliteDatabase (arq)

class  BaseModelo (Model):
    class Meta:
        daatabase = db

class Produto (BaseModelo):
    descricao = CharField ()

    def __str__ (self):
        return  self.descricao
    
class Desperdicio (BaseModelo):
    produto = ForeignKeyField (Produto)
    quantidade = CharField ()
    
    def __str__ (self):
        return  " Houve desperdício de cerca de " + str (self.quantidade) + str (self.produto)

class  Registro (BaseModelo):
    data = CharField ()
    desperdicios = ManyToManyField (Desperdicio)
    pessoas = CharField ()

    def  __str__ (self):
        s =  " Em: " + self.dados +  " havia " + self.pessoas + " pessoas: "
        for d in self.desperdicios:
            s+= str(d)
        return s            


if os.path.exists (arq):
    os.remove (arq)

db.connect ()
db.create_tables ([Produto, Desperdicio, Registro, Registro.desperdicios.get_through_model ()])

# testando como classes: criar instâncias de objetos --------------------

portG = Produto.create ( descricao  =  " Pizza portuguesa grande " )

reg1 = Registro.create ( data = "2019/6/29 ", pessoas  =  3 )
reg1.desperdicios.add(portG)

Registro.select()
