from .AGENT_class import *
from .TERRAIN_class import *
from .ARBOLVIEW_class import *
import matplotlib.pyplot as plt
import networkx as nx

class DFS:
    def __init__(self, agent, terrain, x_ini, y_ini, x_fin, y_fin):
        self.agent = agent
        self.terrain = terrain
        self.x_ini = x_ini
        self.y_ini = y_ini
        self.x_fin = x_fin
        self.y_fin = y_fin
        self.visited = set()  # Conjunto para guardar posiciones visitadas
        self.tree = {}  # Diccionario para representar el árbol de búsqueda
        print(f"DFS iniciado con agente {self.agent.getAgent_type()} desde ({self.x_ini}, {self.y_ini}) hacia ({self.x_fin}, {self.y_fin})")

    def run(self):
        if self.dfs(self.x_ini, self.y_ini) == True:
            print("Solución encontrada.")
        else:
            print("No se encontró solución.")
        self.mostrar_arbol()  # Mostrar el árbol al final del proceso

    def dfs(self, x, y):
        pg.display.flip()
        pg.time.delay(300)
        if (x, y) == (self.x_fin, self.y_fin):
            print(f"Meta alcanzada en ({x}, {y})")
            return True

        self.visited.add((x, y))

        # Inicializar la lista de hijos en el árbol si aún no existe
        if (x, y) not in self.tree:
            self.tree[(x, y)] = []

        # Intentar mover en las 4 direcciones: arriba, abajo, izquierda, derecha
        for move, mover in self.agent.revisarPosiblesMovimientos(x, y):
            new_x, new_y = move
            if (new_x, new_y) not in self.visited:  # Si no se ha visitado
                self.agent.mover_agente(mover)
                self.agent.clear_agent_view(self.agent.screen)
                # self.terrain.draw_matriz(self.agent.screen,0,0)
                self.agent.mascara.draw_mask(0,0, self.terrain, self.agent.screen)
                self.agent.draw_human(self.agent.screen,0,0)
                self.terrain.draw_i(self.agent.screen, 0,0)
                self.terrain.draw_f(self.agent.screen, 0,0)
                self.terrain.draw_v(self.agent.screen, 0,0)
                self.terrain.draw_o(self.agent.screen, 0,0)

                # Actualizar el árbol de búsqueda
                self.tree[(x, y)].append((new_x, new_y))

                if self.dfs(new_x, new_y):
                    return True

                # Si no se encuentra la meta, retrocedemos el movimiento
                self.agent.x, self.agent.y = x, y  # Regresamos a la posición anterior

        return False

    def mostrar_arbol(self):
        self.show_tree= SHOWTREE(self.tree)
        self.show_tree.mostrar_arbol()
