import pygame as pg
import constants as c
from .DFS_class import DFS
from .BFS_class import BFS
from .A_class import AStar
from .TERRAIN_class import Terrain
class Agent:
    pos_i = None
    pos_f = None
    costo_actual = None
    costo_final = None
    def __init__(self, y, x,agent_type):
        
        self.costo_actual = 0
        self.x = x
        self.y = y
        self.costo_acumulado=0
        self.cantidad_movimientos=0
        self.ini_x=x
        self.ini_y=y
        self.meta_x=0
        self.meta_y=0
        self.terrain=None
        self.agent_type=agent_type
        self.priority=None
        print(f"Posicion Inicial Agente: X:{self.x}, Y:{self.y}")
        self.velocidad = 1
        self.human = pg.Rect((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE)
        if(agent_type=="Human"):
            img='/persona.png'
            self.cost_movement = {
                "Montaña": None,
                "Tierra": 1,
                "Agua": 2,
                "Arena": 3,
                "Bosque": 4,
                "Pantano": 5,
                "Nieve": 5,
                "Road": 1
            }
        elif (agent_type=="Monkey"):
            img='/mono.png'
            self.cost_movement = {
                "Montaña": None,
                "Tierra": 2,
                "Agua": 4,
                "Arena": 3,
                "Bosque": 1,
                "Pantano": 5,
                "Nieve": None,
                "Road": 1
            }
        elif(agent_type=="Octopus"):
            img='/pulpo.png'
            self.cost_movement = {
                "Montaña": None,
                "Tierra": 2,
                "Agua": 1,
                "Arena": None,
                "Bosque": 3,
                "Pantano": 2,
                "Nieve": None,
                "Road": 1
            }
        elif(agent_type=="Sasquatch"):
            img='/pie_grande.png'
            self.cost_movement = {
                "Montaña": 15,
                "Tierra": 4,
                "Agua": None,
                "Arena": None,
                "Bosque": 4,
                "Pantano": 5,
                "Nieve": 3,
                "Road": 1
            }
        self.image = pg.image.load("classes\images" + img)
        #self.image_human = pg.transform.rotate(self.image_human, 90)
    
    def draw_human(self, screen, offset_x, offset_y):
        self.offset_x=offset_x
        self.offset_y=offset_y
        self.screen=screen

        self.human = pg.Rect((self.x+1) * c.TILE_SIZE + offset_x, (self.y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE)
        pg.draw.rect(screen, c.BLUE, self.human)
        self.screen.blit(self.image, ((self.x + 1) * c.TILE_SIZE + offset_x, (self.y + 1) * c.TILE_SIZE + offset_y))
        #screen.blit(self.image_human, ((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE))
    def draw_agent_coordinates(self,x,y):
        self.sensor_cuatro(self.terrain,self.mascara,x,y)
        self.mascara.draw_mask(0, 0, self.terrain, self.screen)
        self.human = pg.Rect((x+1) * c.TILE_SIZE  , (y+1) * c.TILE_SIZE , c.TILE_SIZE, c.TILE_SIZE)
        pg.draw.rect(self.screen, c.BLUE, self.human)
        self.screen.blit(self.image, ((x + 1) * c.TILE_SIZE , (y + 1) * c.TILE_SIZE ))
        self.cantidad_movimientos+=1
    def clear_agent_view(self, screen):
        if self.human:
            screen.fill(c.WHITE, self.human)
            self.human = None

    def limpiarAnterior():
        pass
    def actualizar_nuevo_costo(self,nuevocosto):
        self.cantidad_movimientos+=1
        self.costo_acumulado+=nuevocosto
        # self.revisarPosiblesMovimientos(self.x,self.y)
    #def one_sensor(self, pos_x, pos_y, offset_x, offset_y):
        #unmask la casilla en la que apunta
    #def four_sensors(self, pos_x, pos_y, offset_x, offset_y):
        #unmask las cuatro casillas alrededor
    #def calculate_cost(self, pos_x, pos_y):
        #self.costo_actual += cost_movement.get()
    def mover_agente_up(self, terrain):
        cell_value = terrain.matriz[self.y-1][self.x]
        cell_type = c.INT_TERRAIN.get(cell_value)
        if self.validar(cell_type):
            self.terrain.addVisited(self.y,self.x)
            self.y-=1
            self.sensor_cuatro(terrain, self.mascara, self.x, self.y)
            self.actualizar_nuevo_costo(self.cost_movement.get(cell_type))

    def mover_agente_down(self, terrain):
        cell_value = terrain.matriz[self.y+1][self.x]
        cell_type = c.INT_TERRAIN.get(cell_value)
        if self.validar(cell_type):
            self.terrain.addVisited(self.y,self.x)
            self.y += 1
            self.sensor_cuatro(terrain, self.mascara, self.x, self.y)
            self.actualizar_nuevo_costo(self.cost_movement.get(cell_type))
            print(f'posicion despues abajo {self.x} y: {self.y}')

    def mover_agente_left(self, terrain):
        cell_value = terrain.matriz[self.y][self.x-1]
        cell_type = c.INT_TERRAIN.get(cell_value)
        if self.validar(cell_type):
            self.terrain.addVisited(self.y,self.x)
            self.x -= 1
            self.sensor_cuatro(terrain, self.mascara, self.x, self.y)
            self.actualizar_nuevo_costo(self.cost_movement.get(cell_type))

    def mover_agente_right(self, terrain):
        cell_value = terrain.matriz[self.y][self.x+1]
        cell_type = c.INT_TERRAIN.get(cell_value)
        if self.validar(cell_type):
            self.terrain.addVisited(self.y,self.x)
            self.x += 1
            self.sensor_cuatro(terrain, self.mascara, self.x, self.y)
            self.actualizar_nuevo_costo(self.cost_movement.get(cell_type))
    def mover_agente(self,movement):
        if movement=="UP":
            self.mover_agente_up(self.terrain)
        elif movement=="DOWN":
            self.mover_agente_down(self.terrain)
        elif movement=="LEFT":
            self.mover_agente_left(self.terrain)
        elif movement=="RIGHT":
            self.mover_agente_right(self.terrain)
    def validar(self, cell_type):
        if self.cost_movement.get(cell_type) is not None:
            return True
        return False
    def revisarPosiblesMovimientos(self,x,y):
        movimientos = []
        posibles_movimientos = {
            "A": ((x, y-1), "UP") if y > 0 and self.validar(c.INT_TERRAIN[self.terrain.matriz[y-1][x]]) else None,
            "B": ((x, y+1), "DOWN") if y < len(self.terrain.matriz)-1 and self.validar(c.INT_TERRAIN[self.terrain.matriz[y+1][x]]) else None,
            "D": ((x+1, y), "RIGHT") if x < len(self.terrain.matriz[0])-1 and self.validar(c.INT_TERRAIN[self.terrain.matriz[y][x+1]]) else None,
            "I": ((x-1, y), "LEFT") if x > 0 and self.validar(c.INT_TERRAIN[self.terrain.matriz[y][x-1]]) else None,
        }

        # Añadir movimientos en el orden de la prioridad
        for direction in self.priority:
            movimiento = posibles_movimientos.get(direction)
            if movimiento:
                movimientos.append(movimiento)
        # if len(movimientos) >2:
        #     self.terrain.addDecision(self.y,self.x)
        # if len(movimientos)==1:
        #     self.terrain.addVisited(self.y,self.x)
        return movimientos
    def resolverDFS(self):
        print("resolucion por Profundidad")
        dfs = DFS(self,self.terrain,self.ini_x,self.ini_y,self.terrain.getEndpoint_x(),self.terrain.getEndpoint_y())
        dfs.run()
    def resolverBFS(self):
        print("resolucion por anchuragod")
        bfs = BFS(self,self.terrain,self.ini_x,self.ini_y,self.terrain.getEndpoint_x(),self.terrain.getEndpoint_y())
        bfs.run()
    def resolverAstar(self):
        a_star = AStar(self,self.terrain,self.ini_x,self.ini_y,self.terrain.getEndpoint_x(),self.terrain.getEndpoint_y())
        a_star.run()
        print("terminado")


    def limpiarAnterior():
        pass
    def setTerrain(self, terrain:Terrain):
        self.terrain=terrain
    def getCantidad_movimientos(self):
        return self.cantidad_movimientos
    
    def getCosto_acumulado(self):
        return self.costo_acumulado
    
    def unmask_pos_ini(self, mascara, terrain):
        self.mascara=mascara
        mascara.unmask_mask(self.x, self.y)
        self.sensor_cuatro(terrain, self.mascara, self.x, self.y)

    def sensor_cuatro(self, terrain, mascara, x, y):
        #Derecha
        if x+1 < terrain.tam_col:
            self.mascara.unmask_mask(x+1, y)
        #Izquierda
        if x-1 >= 0:
            self.mascara.unmask_mask(x-1, y)
        #Arriba
        if y-1 >= 0:
            self.mascara.unmask_mask(x, y-1)
        #Abajo
        if y+1 < terrain.tam_fila:
            self.mascara.unmask_mask(x, y+1)

    #def one_sensor(self, pos_x, pos_y, offset_x, offset_y):
        #unmask la casilla en la que apunta
    #def four_sensors(self, pos_x, pos_y, offset_x, offset_y):
        #unmask las cuatro casillas alrededor
    #def calculate_cost(self, pos_x, pos_y):
        #self.costo_actual += cost_movement.get()
    def setMeta(self,x,y):
        self.meta_x=x
        self.meta_y=y
        print(x)
        print(y)
    def getIni_x(self):
        return self.ini_x
    def getFin_x(self):
        return self.ini_y
    def getMeta_x(self):
        return self.meta_x
    def getMeta_y(self):
        return self.meta_y
    def getAgent_type(self):
        return self.agent_type
    def setCosto(self,costo_acumulado):
        self.costo_acumulado=costo_acumulado
    def setPriority(self,priority):
        self.priority=priority
        print(self.priority)
