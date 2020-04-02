class Circulo():

    def __init__(self, raio):
        self.raio = raio
        self.diametro = raio * 2
        print( "\n\nCirculo construido\n")

    def getCircunferencia(self):
        return (2 * self.raio * 3.14)

    def imprimirArea(self):
        area =  3.14 * (self.raio * self.raio)
        print( "Area: ", area)
        


