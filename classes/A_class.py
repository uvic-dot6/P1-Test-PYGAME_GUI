import heapq
from .AGENT_class import *
from .TERRAIN_class import *

class AStar:
    def __init__(self, agent, terrain, x_ini, y_ini, x_fin, y_fin):
        self.agent = agent
        self.terrain = terrain
        self.x_ini = x_ini
        self.y_ini = y_ini
        self.x_fin = x_fin
        self.y_fin = y_fin
        self.visited = set()  # Conjunto para guardar posiciones visitadas
        self.priority_queue = []  # Cola de prioridad (min-heap)
        heapq.heappush(self.priority_queue, (0, x_ini, y_ini))  # Inicializar con el nodo inicial
        self.came_from = {}  # Para rastrear el camino
        self.cost_so_far = {(x_ini, y_ini): 0}  # Costo acumulado
        print(f"A* iniciado con agente {self.agent.getAgent_type()} desde ({self.x_ini}, {self.y_ini}) hacia ({self.x_fin}, {self.y_fin})")

    def run(self):
        if self.a_star():
            print("Solución encontrada.")
        else:
            print("No se encontró solución.")

    def heuristic(self, x, y):
        # Heurística Manhattan (puedes cambiarla a otra, como la euclidiana)
        return abs(x - self.x_fin) + abs(y - self.y_fin)

    def a_star(self):
        while self.priority_queue:
            _, x, y = heapq.heappop(self.priority_queue)
            pg.display.flip()
            pg.time.delay(300)

            if (x, y) == (self.x_fin, self.y_fin):
                print(f"Meta alcanzada en ({x}, {y})")
                return True

            self.visited.add((x, y))

            # Revisar los posibles movimientos
            for move, mover in self.agent.revisarPosiblesMovimientos(x, y):
                new_x, new_y = move
                new_cost = self.cost_so_far[(x, y)] + 1  # Costo de movimiento (aquí 1, pero puede cambiar)
                
                if (new_x, new_y) not in self.cost_so_far or new_cost < self.cost_so_far[(new_x, new_y)]:
                    self.cost_so_far[(new_x, new_y)] = new_cost
                    priority = new_cost + self.heuristic(new_x, new_y)  # f(n) = g(n) + h(n)
                    heapq.heappush(self.priority_queue, (priority, new_x, new_y))
                    self.came_from[(new_x, new_y)] = (x, y)  # Rastrear el camino
                    self.agent.mover_agente(self.terrain, mover)

        return False
