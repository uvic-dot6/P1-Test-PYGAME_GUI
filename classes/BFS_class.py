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
        self.queue = deque([(x_ini, y_ini)])  # Cola para BFS
        print(f"BFS iniciado con agente {self.agent.getAgent_type()} desde ({self.x_ini}, {self.y_ini}) hacia ({self.x_fin}, {self.y_fin})")

    def run(self):
        if self.bfs():
            print("Solución encontrada.")
        else:
            print("No se encontró solución.")

    def bfs(self):
        while self.queue:
            x, y = self.queue.popleft()
            pg.display.flip()
            pg.time.delay(300)

            if (x, y) == (self.x_fin, self.y_fin):
                print(f"Meta alcanzada en ({x}, {y})")
                return True

            self.visited.add((x, y))

            # Revisar los posibles movimientos
            for move, mover in self.agent.revisarPosiblesMovimientos(x, y):
                new_x, new_y = move
                if (new_x, new_y) not in self.visited and (new_x, new_y) not in self.queue:
                    self.agent.mover_agente(self.terrain, mover)
                    self.queue.append((new_x, new_y))

        return False
