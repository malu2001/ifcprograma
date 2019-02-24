class Planta(object):
    def __init__(self, nome, altura, comprimento, tipo, idade, tipo_de_folha = None):
        self.nome = nome
        self.altura = altura
        self.tipo_de_folha = tipo_de_folha
        self.comprimento = comprimento
        self.idade = idade 
        self.tipo = tipo
        
       
    def trocar_nome(self, novo_nome):
        if self.nome != novo_nome:
            self.nome = novo_nome
            print('Nome modificado:', self.nome)
    
    def envelhecer_planta(self, nova_idade):
        envelheceu = nova_idade - self.idade
        return ("Quanto envelheceu: ", envelheceu, "Idade atual: ", nova_idade)
        
        
    def definir_tipo_de_folha(self, folha):
        if self.tipo_de_folha == None:
            self.tipo_de_folha = folha
            return self.tipo_de_folha
        return("Tipo de folha já estipulado")
    
    def crescer_planta(self):
        if self.idade <= 21:
            crescimento = self.idade * 0.5
            self.altura = crescimento
            print(self.altura)
            
        if self.idade > 21 or self.idade <= 60: 
            altura2 = 21 * 0.5
            age = self.idade - 21
            crescimento1 = age * 0.3
            crescimento2 = crescimento1 + altura2
            self.altura = crescimento2
            print(self.altura)
        
        if self.idade > 60:
            print("Sua plantinha não cresce mais. Sua altura é: ", crescimento2)

class Mato(Planta):
    def __init__(self, nome, altura, comprimento, tipo, idade, mes, tipo_de_folha = None):
        super().__init__(nome, altura, comprimento, tipo, idade,tipo_de_folha = None)
        self.mes = mes

    def envelhecer_mato(self, nova_idade):
        envelheceu = nova_idade - self.idade
        return ("Quanto envelheceu: ", envelheceu, "Idade atual: ", nova_idade)

    def crescer_mato(self):
        if self.idade <= 21:
            crescimento = (self.idade*12) * 1
            self.altura = crescimento
            print("em centimetros: ", self.altura, "Em metros", self.altura/100)
            
        if self.idade > 21 and self.idade <= 60: 
            altura2 = (self.idade*12)*1
            crescimento1 = (60 - 21) * 0.8
            crescimento2 = altura2 + crescimento1
            self.altura = crescimento2
            print("e centimetros: ", self.altura, "Em metros: ", self.altura/100)
        
        if self.idade > 60:
            altura2 = (self.idade*12)*1
            crescimento1 = (60 - 21) * 0.8
            crescimento2 = altura2 + crescimento1
            print("Sua plantinha não cresce mais. Sua altura", crescimento2, "cm", 'em metros: ', crescimento2/100)


if __name__ == "__main__":
    planta = Planta('maria', 1, 1.5,'margarida', 5)
    mato = Mato('capim', 1, 0.5, 'mato ué', 61, 12)
    mato.crescer_mato()
    print(mato.envelhecer_mato(62))
