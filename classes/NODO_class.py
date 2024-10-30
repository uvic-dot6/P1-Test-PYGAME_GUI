


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

    def toString(self):
        return f'Nodo: {self.dato} Costo: {self.costo}'
    def pos_to_coordinate(self, x, y):
        # Convertimos x e y en una coordenada tipo "1A", "6F", etc.
        row = str(x + 1)  # Sumamos 1 para empezar desde 1
        col = chr(ord('A') + y)  # Convertimos a la letra correspondiente
        return f"{row}{col}"
    def setCosto(self,costo):
        self.costo=costo

class NodoInformado:
    def __init__(self, dato, g, movimientos, h):
        self.dato = dato  # posición del jugador
        self.g = g  # costo acumulado
        self.movimientos = movimientos  # número de movimientos
        self.h = h  # valor heurístico
        self.f = g + h  # costo total (g + h)
        self.padre = None
        self.hijos = []  # lista de nodos hijos (para el árbol)
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __repr__(self):
        return f'Nodo: {self.dato} g:{self.g} h:{self.h} f:{self.f}'