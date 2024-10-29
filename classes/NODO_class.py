class Nodo:
    def __init__(self, x, y):
        self.izquierda = None
        self.derecha = None
        self.arriba = None
        self.abajo = None
        self.coordenadas = (x, y)
        self.visitado = False  # Indica si el nodo ya fue visitado
        self.casilla = (1, "A")  # Ejemplo de estado de la casilla, ajustable
        self.posibles_acciones = []  # Lista de acciones posibles desde este nodo

    def agregar_vecino(self, direccion, nodo_vecino):
        # Método para enlazar un nodo vecino en una dirección específica
        if direccion == "izquierda":
            self.izquierda = nodo_vecino
            self.posibles_acciones.append(("izquierda", nodo_vecino))
        elif direccion == "derecha":
            self.derecha = nodo_vecino
            self.posibles_acciones.append(("derecha", nodo_vecino))
        elif direccion == "arriba":
            self.arriba = nodo_vecino
            self.posibles_acciones.append(("arriba", nodo_vecino))
        elif direccion == "abajo":
            self.abajo = nodo_vecino
            self.posibles_acciones.append(("abajo", nodo_vecino))
