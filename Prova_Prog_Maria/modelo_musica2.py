from peewee import *

#arq = "C:/Users/pc/Documents/Programacao/loja_musica7.db"
arq = "loja_musica7.db"
db = SqliteDatabase(arq)

class BaseModelo (Model):
    class Meta:
        database = db

class Cliente (BaseModelo):
    nome = CharField ()
    cpf = CharField () # Considera hífen e ponto, por isso é CharField.
    endereco = CharField ()

class Produto(BaseModelo):
    nome = CharField ()
    marca = CharField ()
    preco = FloatField ()
    qtd = IntegerField ()

class InstrumentoMusical (BaseModelo):
    produto = ForeignKeyField (Produto)
    categoria = CharField ()

class EquipamentosEletronicos (BaseModelo):
    produto = ForeignKeyField (Produto)

class Discografia (BaseModelo): # Neste caso, abrange, os tipos de midia, cd, dvd, bluray... e seus respectivos atributos.
    produto = ForeignKeyField (Produto)
    autor = CharField ()
    genero =  CharField ()

class Funcionario (BaseModelo):
    nome = CharField ()
    cpf = CharField ()
    endereco = CharField ()

class Venda (BaseModelo):
    cliente = ForeignKeyField (Cliente)
    produto = ForeignKeyField (Produto)
    data_venda = CharField () # DateField()
    funcionario = ForeignKeyField (Funcionario)

class Pagamento (BaseModelo): #Pagamento de uma conta.
    tipo_pagamento = CharField () # A vista, a prazo.
    forma_pagamento = CharField () # Cartão de Crédito, dinheiro, cheque.
    venda = ForeignKeyField (Venda)

class Fornecedor (BaseModelo):
    nome = CharField ()
    produto = ForeignKeyField (Produto)

class Estoque (BaseModelo):
    produtos = ForeignKeyField (Produto)
    fornecedor = ForeignKeyField (Fornecedor)
    data_nota_fiscal = CharField ()
    qtd = IntegerField ()
    
db.connect()
db.create_tables([Cliente,Produto, InstrumentoMusical, EquipamentosEletronicos, Discografia, Funcionario, Venda, Pagamento, Fornecedor, Estoque])

if __name__ == "__main__":

    #Criação dos objetos.

    maria = Cliente.create (nome = "Maria Luisa Mognon", cpf = "444.789.456-22", endereco = "Rua XV de novembro - Pomerode")
    luisa = Cliente.create (nome = "Luisa Oliveira Slva", cpf = "111.777.888-22", endereco = "Rua XV de novembro - Blumenau")


    prod1 = Produto.create (nome = "Piano", marca = "Philco", preco = 20000, qtd = 1) 
    prod2 = Produto.create (nome = "Caixa de Som", marca = "Philco", preco = 5000, qtd = 1)
    prod3 = Produto.create (nome = "CD", marca = "MTV", preco = 30, qtd = 2) 

    piano = InstrumentoMusical.create (produto = prod1, categoria = "Percussao")
    cx_som = EquipamentosEletronicos.create (produto = prod2)
    maroon5 = Discografia.create (produto = prod3, autor = "Maroon 5", genero = "Pop Rock")

    funci1 = Funcionario.create (nome = "Alencar Medeiros", cpf = "123.456.789-63", endereco = "Rua 8 de outubro")
    funci2 = Funcionario.create (nome = "Joelma da Silva ", cpf = "555.894.123-12", endereco = "Rua 15 de agosto")
    funci3 = Funcionario.create (nome = "Celma Rosa Santos", cpf = "021.632.466-78", endereco = "Rua 5 de marco")



    venda1 = Venda.create (cliente = maria, produto = prod1, data_venda = "14/02/2019", funcionario = funci1)
    venda2 = Venda.create (cliente = luisa, produto = prod3, data_venda = "14/02/2020", funcionario = funci2)
    venda3 = Venda.create (cliente = luisa, produto = prod2, data_venda = "27/11/2020", funcionario = funci3)


    pag1 = Pagamento.create (tipo_pagamento = "A prazo", forma_pagamento = "cartao de credito", venda = venda1) # Exemplo: parcelado (prazo) em 5 vezes no cartao de credito
    pag2 = Pagamento.create (tipo_pagamento = "A prazo", forma_pagamento = "boleto", venda = venda2)
    pag3 = Pagamento.create (tipo_pagamento = "A vista", forma_pagamento = "dinheiro", venda = venda3)

    forne1 = Fornecedor.create (nome  = "Jose LTDA", produto = prod2)
    estoq1 = Estoque.create(produtos = prod3, fornecedor = forne1, data_nota_fiscal = "29/11/2019", qtd = 100)


    #Testes para ver se houve a criação dos objetos.

    print(cx_som.produto.nome, cx_som.produto.marca)
    print(piano.produto.nome, piano.produto.marca)
    print(prod1.nome)
 
    print(venda1.cliente.nome)
    print(venda1.produto.nome)
    print(pag1.venda.produto.marca)
    print(forne1.nome)
    print(funci1.nome)
    print(estoq1.produtos.nome, estoq1.fornecedor.nome +str(estoq1.qtd))
    print(pag1.venda.produto.qtd)
    print(venda2.produto.nome)