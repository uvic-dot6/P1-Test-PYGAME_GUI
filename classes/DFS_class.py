from .AGENT_class import *
from .TERRAIN_class import *
class DFS:
    def __init__(self, agent, terrain, x_ini, y_ini, x_fin, y_fin):
        self.agent = agent
        self.terrain = terrain
        self.x_ini = x_ini
        self.y_ini = y_ini
        self.x_fin = x_fin
        self.y_fin = y_fin# Pantalla de pygame para mostrar los movimientos
        self.visited = set()  # Conjunto para guardar posiciones visitadas
        print(f"DFS iniciado con agente {self.agent.getAgent_type()} desde ({self.x_ini}, {self.y_ini}) hacia ({self.x_fin}, {self.y_fin})")

    def run(self):
        if self.dfs(self.x_ini, self.y_ini) == True:
            print("Solución encontrada.")
        else:
            print("No se encontró solución.")

    def dfs(self, x, y):
        pg.display.flip()  
        pg.time.delay(300)  
        if (x, y) == (self.x_fin, self.y_fin):
            print(f"Meta alcanzada en ({x}, {y})")
            return True
        
        self.visited.add((x, y))
        
        # Intentar mover en las 4 direcciones: arriba, abajo, izquierda, derecha
        for move, mover in self.agent.revisarPosiblesMovimientos(x, y):
            new_x, new_y = move
            if (new_x, new_y) not in self.visited:  # Si no se ha visitado
                self.agent.mover_agente(self.terrain,mover)
                if self.dfs(new_x, new_y):
                    return True
                # Si no se encuentra la meta, retrocedemos el movimiento
                self.agent.x, self.agent.y = x, y  # Regresamos a la posición anterior

        return False


