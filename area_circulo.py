class Circulo(object):
    def __init__(self, circun):
        self.circun = circun

    def descobrir_raio(self):
        raio = self.circun/(2*3.14)
        return raio

    def calcular_area(self):
        descoberta = self.descobrir_raio()
        area = 3.14*(descoberta**2)
        return area


if __name__ == "__main__":
    bola = Circulo(20)
    print(bola.descobrir_raio())
    print(bola.calcular_area())
    








