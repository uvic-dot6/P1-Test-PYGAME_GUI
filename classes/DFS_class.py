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
        self.nodo = Nodo(x_ini,  y_ini, 0,0)
        self.nodo_raiz = self.nodo 
        self.visited = set()  # Conjunto para guardar posiciones visitadas
        self.tree = {}  # Diccionario para representar el árbol de búsqueda
        print(f"DFS iniciado con agente {self.agent.getAgent_type()} desde ({self.x_ini}, {self.y_ini}) hacia ({self.x_fin}, {self.y_fin})")

    def run(self):
        if self.dfs(self.x_ini, self.y_ini,self.nodo_raiz) == True:
            print("Solución encontrada.")
        else:
            print("No se encontró solución.")
        self.mostrar_arbol()

    def dfs(self, x, y, nodo_padre, costo_acumulado=0):
        pg.display.flip()
        pg.time.delay(300)

        # Verificar si se ha alcanzado la meta
        if (x, y) == (self.x_fin, self.y_fin):
            print(f"Meta alcanzada en ({x}, {y}) con costo acumulado: {costo_acumulado}")
            #cada decision
            nodo_meta = Nodo(x, y, costo_acumulado, 0)
            nodo_padre.hijos.append(nodo_meta)
            nodo_meta.setMeta()
            self.agent.setCosto(costo_acumulado)  
            return True
        self.visited.add((x, y))

        movimientos = self.agent.revisarPosiblesMovimientos(x, y)
        for move, mover in movimientos:
            new_x, new_y = move
            ##para nodos por cada decison  

            if len(movimientos) > 2 or (len(movimientos) == 1 and nodo_padre is not self.nodo_raiz):
                    nuevo_nodo = Nodo(x, y, costo_acumulado, nodo_padre)
                    nodo_padre.hijos.append(nuevo_nodo)
                    nuevo_nodo.setCosto(costo_acumulado)
            else:
                nuevo_nodo = nodo_padre 

            # Si el nodo no es la raíz, crear un nodo hijo con el costo acumulado
            if (new_x, new_y) not in self.visited:                   
                costo_movimiento = self.agent.cost_movement.get(c.INT_TERRAIN.get(self.terrain.matriz[new_y][new_x]), 1)
                nuevo_costo_acumulado = costo_acumulado + costo_movimiento
                
                #  muestreo de nodos paso a paso 
                # nuevo_nodo = Nodo(new_x, new_y, nuevo_costo_acumulado, 0)
                # nodo_padre.hijos.append(nuevo_nodo)
                if len(movimientos) >2:
                    self.terrain.addDecision(self.agent.y,self.agent.x)
                self.agent.mover_agente(mover)
                
                self.terrain.addVisited(self.agent.y,self.agent.x)  
                self.agent.clear_agent_view(self.agent.screen)
                self.agent.mascara.draw_mask(0, 0, self.terrain, self.agent.screen)
                self.agent.draw_human(self.agent.screen, 0, 0)
                self.terrain.draw_i(self.agent.screen, 0, 0)
                self.terrain.draw_f(self.agent.screen, 0, 0)
                self.terrain.draw_v(self.agent.screen, 0, 0)
                self.terrain.draw_o(self.agent.screen, 0, 0)

                # Llamada recursiva pasando el nuevo nodo y el costo acumulado actualizado
                if self.dfs(new_x, new_y, nuevo_nodo, nuevo_costo_acumulado):
                    return True

                self.agent.x = x
                self.agent.y = y  # Regresar a la posición anterior

        return False



    def mostrar_arbol(self):
        self.show_tree= SHOWTREE(self.tree)
        self.show_tree.graficar_arbol(self.nodo_raiz)
        
