


class Nodo:
    def __init__(self, x,y, costo, movimientos):
        self.x = x
        self.y = y
        self.dato=self.pos_to_coordinate(y,x)
        print(self.dato)
        self.costo = costo
        self.movimientos = movimientos
        self.padre = None
        self.hijos = []
        self.meta=False

    def toString(self):
        return f'Nodo: {self.dato} Costo: {self.costo}'
    def pos_to_coordinate(self, x, y):
        # Convertimos x e y en una coordenada tipo "1A", "6F", etc.
        row = str(x + 1)  # Sumamos 1 para empezar desde 1
        col = chr(ord('A') + y)  # Convertimos a la letra correspondiente
        return f"{row}{col}"
    def setCosto(self,costo):
        self.costo=costo
    def setMeta(self):
        self.meta=True
class NodoInformado:
    def __init__(self, x, y,costo,distancia):
        self.x = x
        self.y = y
        self.dato=self.pos_to_coordinate(y,x)
        print(self.dato)
        self.costo = costo
        self.heuristica=costo+distancia
        self.distancia=distancia
        self.padre = None
        self.hijos = []
        self.meta=False
    def toString(self):
        return f'Nodo: {self.dato} Costo: {self.costo}'
    def pos_to_coordinate(self, x, y):
        # Convertimos x e y en una coordenada tipo "1A", "6F", etc.
        row = str(x + 1)  # Sumamos 1 para empezar desde 1
        col = chr(ord('A') + y)  # Convertimos a la letra correspondiente
        return f"{row}{col}"
    def setCosto(self,costo):
        self.costo=costo
    def setDistancia(self,distancia):
        self.distancia=distancia
    def setHeuristica(self,heuristica):
        self.heuristica=heuristica
    def getCosto(self):
        return self.costo
    def getDistancia(self):
        return self.distancia
    def getHeuristica(self):
        return self.heuristica
    def __lt__(self, other):
        return self.getDistancia() < other.getDistancia()
    def setMeta(self):
        self.meta=True