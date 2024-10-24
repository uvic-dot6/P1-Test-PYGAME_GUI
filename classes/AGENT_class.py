import pygame as pg
import constants as c
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
        self.human = pg.Rect((self.x+1) * c.TILE_SIZE + offset_x, (self.y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE)
        pg.draw.rect(screen, c.BLUE, self.human)
        screen.blit(self.image, ((self.x + 1) * c.TILE_SIZE + offset_x, (self.y + 1) * c.TILE_SIZE + offset_y))
        #screen.blit(self.image_human, ((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE))

    def actualizar_nuevo_costo(self,nuevocosto):
        self.cantidad_movimientos+=1
        self.costo_acumulado+=nuevocosto
    #def one_sensor(self, pos_x, pos_y, offset_x, offset_y):
        #unmask la casilla en la que apunta
    #def four_sensors(self, pos_x, pos_y, offset_x, offset_y):
        #unmask las cuatro casillas alrededor
    #def calculate_cost(self, pos_x, pos_y):
        #self.costo_actual += cost_movement.get()
    def mover_agente_up(self,terrain):
        cell_value = terrain.matriz[self.y-1][self.x]
        print(cell_value)
        cell_type = c.INT_TERRAIN.get(cell_value)
        if self.validar(cell_type):
            self.y-=1
            self.actualizar_nuevo_costo(self.cost_movement.get(cell_type))
    def mover_agente_down(self, terrain):
        cell_value = terrain.matriz[self.y+1][self.x]
        print(cell_value)
        cell_type = c.INT_TERRAIN.get(cell_value)
        if self.validar(cell_type):
            self.y += 1
            self.actualizar_nuevo_costo(self.cost_movement.get(cell_type))

    def mover_agente_left(self, terrain):
        cell_value = terrain.matriz[self.y][self.x-1]
        print(cell_value)
        cell_type = c.INT_TERRAIN.get(cell_value)
        if self.validar(cell_type):
            self.x -= 1
            self.actualizar_nuevo_costo(self.cost_movement.get(cell_type))

    def mover_agente_right(self, terrain):
        print("right")
        cell_value = terrain.matriz[self.y][self.x+1]
        print(cell_value)
        cell_type = c.INT_TERRAIN.get(cell_value)
        if self.validar(cell_type):
            self.x += 1
            self.actualizar_nuevo_costo(self.cost_movement.get(cell_type))

    def validar(self, cell_type):
        if self.cost_movement.get(cell_type) is not None:
            return True
        return False
    def getCantidad_movimientos(self):
        return self.cantidad_movimientos
    def getCosto_acumulado(self):
        print(self.costo_acumulado)
        return self.costo_acumulado