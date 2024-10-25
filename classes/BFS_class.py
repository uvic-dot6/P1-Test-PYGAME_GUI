from .AGENT_class import *
from .TERRAIN_class import *
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

class BFS:
    def __init__(self, agent, terrain, x_ini, y_ini, x_fin, y_fin):
        self.agent = agent
        self.terrain = terrain
        self.x_ini = x_ini
        self.y_ini = y_ini
        self.x_fin = x_fin
        self.y_fin = y_fin
        self.visited = set()  # Conjunto para guardar posiciones visitadas
        self.tree = {}  # Diccionario para representar el árbol de búsqueda
        print(f"BFS iniciado con agente {self.agent.getAgent_type()} desde ({self.x_ini}, {self.y_ini}) hacia ({self.x_fin}, {self.y_fin})")

    def run(self):
        if self.bfs(self.x_ini, self.y_ini) == True:
            print("Solución encontrada.")
        else:
            print("No se encontró solución.")
        self.mostrar_arbol()  # Mostrar el árbol al final del proceso

    def bfs(self, x, y):
        # Inicializamos la cola y añadimos la posición inicial
        queue = deque([(x, y)])
        self.visited.add((x, y))

        # Mientras haya nodos en la cola, seguimos explorando
        while queue:
            current_x, current_y = queue.popleft()

            pg.display.flip()
            pg.time.delay(300)

            # Si llegamos a la meta, retornamos True
            if (current_x, current_y) == (self.x_fin, self.y_fin):
                print(f"Meta alcanzada en ({current_x}, {current_y})")
                return True

            # Inicializar la lista de hijos en el árbol si aún no existe
            if (current_x, current_y) not in self.tree:
                self.tree[(current_x, current_y)] = []

            # Intentar mover en las 4 direcciones: arriba, abajo, izquierda, derecha
            for move, mover in self.agent.revisarPosiblesMovimientos(current_x, current_y):
                new_x, new_y = move
                if (new_x, new_y) not in self.visited:  # Si no se ha visitado
                    self.visited.add((new_x, new_y))  # Marcar como visitado
                    queue.append((new_x, new_y))  # Agregar a la cola

                    # Actualizar el árbol de búsqueda
                    self.tree[(current_x, current_y)].append((new_x, new_y))

                    # Mover el agente en el terreno
                    self.agent.mover_agente(self.terrain, mover)

        return False  # No se encontró la meta

    def mostrar_arbol(self):
        # Usaremos la librería networkx para crear y mostrar el árbol
        G = nx.DiGraph()

        # Agregar nodos y bordes del árbol
        for parent, children in self.tree.items():
            for child in children:
                G.add_edge(parent, child)

        # Dibujar el grafo
        pos = nx.spring_layout(G)  # Diseño del grafo
        plt.figure(figsize=(8, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=700)
        plt.title("Árbol de Búsqueda BFS")
        plt.show()
