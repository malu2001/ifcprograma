from peewee import *

db = SqliteDatabase("marcenaria.db")

class BaseModelo(Model):
    class Meta:
        database=db


class Cliente(BaseModelo):
    nome=CharField()

    def __str__(self):
        return "Nome Cliente: " + self.nome

class Material(BaseModelo):
    nome=CharField()
    preco=CharField()
    cod_material=CharField()
    qtd = CharField()

    def __str__(self):
        return  "Material: " + self.nome + "Preco: " + self.preco + "Cod material: " + self.cod_material  + "Quantidade: " + self.qtd

class Produto(BaseModelo):
    nome=CharField()
    preco=CharField()
    pedido=ManyToManyField(Cliente)
    material=ManyToManyField(Material)

    def __str__(self):
        return "Produto: " + self.nome + "Preco: " + self.preco

class Estoque(BaseModelo):
    material=ForeignKeyField(Material)



db.connect()
db.create_tables([Cliente,Material,Produto,Estoque, Produto.pedido.get_through_model(), Produto.material.get_through_model()])

c1=Cliente.create(nome="Amanda")
m1=Material.create(nome="madeira",preco="15,00", cod_material="1", qtd = "1")
prod1=Produto.create(nome="Escrivaninha", preco="30,00")
estoque = Estoque.create(material = m1)

prod1.pedido.add(c1)
prod1.material.add(m1)

for i in prod1.pedido:
    print(i.nome)

for i in prod1.material:
    print(i.nome)
    print(i.preco)
    print(i.qtd)
    print(i.cod_material)




