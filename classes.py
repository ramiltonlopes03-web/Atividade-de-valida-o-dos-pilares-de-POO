class Arvore:
    def __init__(self, nome, folhas, tronco, calendario_climatico):
        self.nome = nome
        self.folhas = folhas
        self.tronco = tronco
        self.calendario_climatico = calendario_climatico

class ArvoreFrutiferas(Arvore):
    def __init__(self, frutas):
        self.frutas = frutas