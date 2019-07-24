lista_intens = []

class Produto(object):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Item (Produto):
    def __init__(self, quantidade, nome, preco):
        super().__init__(nome, preco)
        self.quantidade = quantidade

class Caixa(Item):
    def __init__(self, quantidade, nome, preco):
        super().__init__(self, quantidade, nome, preco)

    def calcular_preco(self, quantidade, preco):
        self.valor = self.preco*self.quantidade
        lista_intens.append(self.valor)

    def calcular_preco_total(self):
        self.total = sum(lista_intens)
        return ("Total das compras: " +str(self.total))



if __name__ == "__main__":
    produto1 = Produto("Pizza", 70)
    produto2 = Produto("Schocolade", 5)

    item = Item(5, "pizza", 70)
    caixa = Caixa(item)
    print(caixa.calcular_preco(4, 5))
