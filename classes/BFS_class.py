import pygame as pg
import time
from collections import deque
from .AGENT_class import *
from .TERRAIN_class import *
from .ARBOLVIEW_class import *
from .NODO_class import *

class BFS:
    def __init__(self, agent, terrain, x_ini, y_ini, x_fin, y_fin):
        self.agent = agent
        self.terrain = terrain
        self.x_ini = x_ini
        self.y_ini = y_ini
        self.x_fin = x_fin
        self.y_fin = y_fin
        self.costo = 0
        self.camino=[]
        self.visited = set()
        self.nodo_raiz = NodoInformado(x_ini, y_ini, 0, 0)  # La distancia es irrelevante en BFS
        print(f"BFS iniciado con agente {self.agent.getAgent_type()} desde ({self.x_ini}, {self.y_ini}) hacia ({self.x_fin}, {self.y_fin})")

    def run(self):
        if self.bfs():
            print("Solución encontrada.")
            self.agent.x = self.x_fin
            self.agent.y = self.y_fin
            self.agent.clear_agent_view(self.agent.screen)
            self.agent.draw_agent_coordinates(self.x_fin, self.y_fin)
            self.terrain.draw_i(self.agent.screen, 0, 0)
            self.terrain.draw_f(self.agent.screen, 0, 0)
            self.terrain.draw_v(self.agent.screen, 0, 0)
            self.terrain.draw_o(self.agent.screen, 0, 0)
            pg.display.flip()
            pg.time.delay(400)
        else:
            print("No se encontró solución.")
        self.mostrar_arbol()

    def bfs(self):
        queue = deque([(self.nodo_raiz)])

        while queue:
            current_node = queue.popleft()
            x = current_node.x
            y = current_node.y

            if (x, y) == (self.x_fin, self.y_fin):
                print(f"Meta alcanzada en ({x}, {y}) con costo acumulado: {current_node.costo}")
                return True

            self.visited.add((x, y))

            movimientos = self.agent.revisarPosiblesMovimientos(x, y)
            for move, mover in movimientos:
                self.agent.x=current_node.x
                self.agent.y=current_node.y
                new_x, new_y = move
                if (new_x, new_y) not in self.visited:
                    costo_movimiento = self.agent.cost_movement.get(c.INT_TERRAIN.get(self.terrain.matriz[new_y][new_x]), 1)
                    nuevo_costo_acumulado = current_node.costo + costo_movimiento
                    nuevo_nodo = Nodo(new_x, new_y, nuevo_costo_acumulado, 0)
                    nuevo_nodo.padre = current_node
                    current_node.hijos.append(nuevo_nodo)
                    queue.append(nuevo_nodo)

                    if (new_x, new_y) == (self.x_fin, self.y_fin):
                        nuevo_nodo.setMeta()
                        break

                    if len(movimientos) > 2:
                        self.terrain.addDecision(current_node.y, current_node.x)
                    self.terrain.addVisited(new_y, new_x)
                    self.agent.clear_agent_view(self.agent.screen)
                    # self.agent.draw_agent_coordinates(new_x, new_y)
                    self.agent.mover_agente(mover)
                    self.agent.clear_agent_view(self.agent.screen)
                    self.terrain.draw_matriz(self.agent.screen,0,0)
                    self.agent.mascara.draw_mask(0, 0, self.terrain, self.agent.screen)
                    self.agent.draw_human(self.agent.screen, 0, 0)
                    
                    self.terrain.draw_i(self.agent.screen, 0, 0)
                    self.terrain.draw_f(self.agent.screen, 0, 0)
                    self.terrain.draw_v(self.agent.screen, 0, 0)
                    self.terrain.draw_o(self.agent.screen, 0, 0)

                    pg.display.flip()
                    pg.time.delay(400)

        return False

    def mostrar_arbol(self):
        self.show_tree = SHOWTREE(None)
        self.show_tree.graficar_arbol(self.nodo_raiz)
