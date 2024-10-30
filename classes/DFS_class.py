from .AGENT_class import *
from .TERRAIN_class import *
from .ARBOLVIEW_class import *
from .NODO_class import *
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
        self.costo = 0
        self.movimientos= 0
        self.nodo = Nodo(x_ini,  y_ini, 0,None)
        self.nodo_raiz = self.nodo 
        self.visited = set()  # Conjunto para guardar posiciones visitadas
        self.tree = {}  # Diccionario para representar el árbol de búsqueda
        print(f"DFS iniciado con agente {self.agent.getAgent_type()} desde ({self.x_ini}, {self.y_ini}) hacia ({self.x_fin}, {self.y_fin})")

    def run(self):
        if self.dfs(self.x_ini, self.y_ini,self.nodo_raiz) == True:
            print("Solución encontrada.")
        else:
            print("No se encontró solución.")
        self.mostrar_arbol()  # Mostrar el árbol al final del proceso

    def dfs(self, x, y, nodo_padre):
        pg.display.flip()
        pg.time.delay(300)

        # Verificar si se ha alcanzado la meta
        if (x, y) == (self.x_fin, self.y_fin):
            print(f"Meta alcanzada en ({x}, {y})")
            nodo_meta = Nodo(x, y, self.costo, nodo_padre)
            nodo_padre.hijos.append(nodo_meta)
            return True

        # Marcar la celda como visitada
        self.visited.add((x, y))

        # Inicializar la lista de hijos en el árbol si aún no existe
        if (x, y) not in self.tree:
            self.tree[(x, y)] = []

        # Obtener los movimientos posibles en las direcciones permitidas
        movimientos = self.agent.revisarPosiblesMovimientos(x, y)
        for move, mover in movimientos:
            new_x, new_y = move
            if len(movimientos)>2 :
                nuevo_nodo = Nodo(self.agent.x, self.agent.y, self.costo, nodo_padre)
                nodo_padre.hijos.append(nuevo_nodo)  # Agregar el nuevo nodo como hijo del nodo actual
            elif len(movimientos)==1 and nodo_padre is not self.nodo_raiz:
                nuevo_nodo = Nodo(self.agent.x, self.agent.y, self.costo, nodo_padre)
                nodo_padre.hijos.append(nuevo_nodo)
            else:
                nuevo_nodo=nodo_padre
            if (new_x, new_y) not in self.visited:  # Si no se ha visitado
                
                # Mover al agente en el entorno y actualizar la visualización
                self.agent.mover_agente(mover)
                self.agent.clear_agent_view(self.agent.screen)
                self.agent.mascara.draw_mask(0, 0, self.terrain, self.agent.screen)
                self.agent.draw_human(self.agent.screen, 0, 0)
                self.terrain.draw_i(self.agent.screen, 0, 0)
                self.terrain.draw_f(self.agent.screen, 0, 0)
                self.terrain.draw_v(self.agent.screen, 0, 0)
                self.terrain.draw_o(self.agent.screen, 0, 0)

                # Actualizar el árbol de búsqueda
                self.tree[(x, y)].append((new_x, new_y))

                # Llamada recursiva pasando el nuevo nodo como el nodo padre
                if self.dfs(new_x, new_y, nuevo_nodo):
                    return True

                # Si no se encuentra la meta, retroceder en la posición del agente
                self.agent.x, self.agent.y = x, y  # Regresar a la posición anterior

        return False

    def mostrar_arbol(self):
        self.show_tree= SHOWTREE(self.tree)
        self.show_tree.graficar_arbol(self.nodo_raiz)
        
