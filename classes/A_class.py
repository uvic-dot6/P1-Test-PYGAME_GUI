import heapq
import pygame as pg
import time
from .AGENT_class import *
from .TERRAIN_class import *
from .ARBOLVIEW_class import *
from .NODO_class import *

class AStar:
    def __init__(self, agent, terrain, x_ini, y_ini, x_fin, y_fin):
        self.agent = agent
        self.terrain = terrain
        self.x_ini = x_ini
        self.y_ini = y_ini
        self.x_fin = x_fin
        self.y_fin = y_fin
        self.costo = 0
        self.camino = []
        self.visited = set()
        # Inicializamos la raíz con una lista vacía de movimientos
        self.nodo_raiz = NodoInformado(x_ini, y_ini, 0, self.calcular_distancia(x_ini, y_ini), [])
        print(f"A* iniciado con agente {self.agent.getAgent_type()} desde ({self.x_ini}, {self.y_ini}) hacia ({self.x_fin}, {self.y_fin})")

    def calcular_distancia(self, x, y):
        return abs(x - self.x_fin) + abs(y - self.y_fin)

    def run(self):
        if self.astar():
            print("Solución encontrada.")
            self.agent.x = self.x_fin
            self.agent.y = self.y_fin
            self.agent.clear_agent_view(self.agent.screen)
            self.agent.draw_agent_coordinates(self.x_fin, self.y_fin)
            self.terrain.draw_i(self.agent.screen, 0, 0)
            self.terrain.draw_f(self.agent.screen, 0, 0)
            self.terrain.draw_v(self.agent.screen, 0, 0)
            self.terrain.draw_o(self.agent.screen, 0, 0)
            print(f'CAMINO: {self.camino}')
            pg.display.flip()
            pg.time.delay(400)
        else:
            print("No se encontró solución.")
        self.mostrar_arbol()

    def astar(self):
        open_list = []
        heapq.heappush(open_list, (0, self.nodo_raiz))

        while open_list:
            heuristica,current_node = heapq.heappop(open_list)
            x = current_node.x
            y = current_node.y

            '''
                SE LLEGA A LA META RETORNA LA FUNCION
            '''
            if (x, y) == (self.x_fin, self.y_fin):
                print(f"Meta alcanzada en ({x}, {y}) con costo acumulado: {current_node.getCosto()}")
                self.agent.setCosto(current_node.getCosto())
                self.camino = current_node.movimientos  # Guardamos el camino óptimo
                return True

            self.visited.add((x, y))
            movimientos = self.agent.revisarPosiblesMovimientos(x, y)

            '''
                INTENTAR TODOS LOS MOVIMIENTOS EN ESE PUNTO
            '''
            for move, mover in movimientos:
                new_x, new_y = move
                self.agent.x = current_node.x
                self.agent.y = current_node.y

                if (new_x, new_y) not in self.visited:
                    cost_movement = self.agent.cost_movement.get(c.INT_TERRAIN.get(self.terrain.matriz[new_y][new_x]), 1)
                    new_acumulate_cost = current_node.getCosto() + cost_movement
                    distancia = self.calcular_distancia(new_x, new_y)
                    movimientos_nuevo = current_node.movimientos + [mover]
                    nuevo_nodo = NodoInformado(new_x, new_y, new_acumulate_cost, distancia, movimientos_nuevo)
                    nuevo_nodo.padre = current_node
                    current_node.hijos.append(nuevo_nodo)
                    heapq.heappush(open_list, (nuevo_nodo.getHeuristica(), nuevo_nodo))

                    if (new_x, new_y) == (self.x_fin, self.y_fin):
                        nuevo_nodo.setMeta()
                        break
                    if len(movimientos) > 2:
                        self.terrain.addDecision(current_node.y, current_node.x)
                    self.terrain.addVisited(new_y, new_x)
                    self.agent.clear_agent_view(self.agent.screen)
                    self.agent.mover_agente(mover)
                    self.agent.clear_agent_view(self.agent.screen)
                    self.terrain.draw_matriz(self.agent.screen, 0, 0)
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
        self.show_tree = SHOWTREEinformado()
        self.show_tree.graficar_arbol(self.nodo_raiz)
