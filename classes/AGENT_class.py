import pygame as pg
import constants as c

class Agent_Human:
    pos_i = None
    pos_f = None
    costo_actual = None
    costo_final = None
    cost_movement = {
        "Montaña": None,
        "Tierra": 1,
        "Agua": 2,
        "Arena": 3,
        "Bosque": 4,
        "Pantano": 5,
        "Nieve": 5,
        "Road": 1
    }
    def __init__(self, y, x):
        self.costo_actual = 0
        self.x = x
        self.y = y
        print(f"Posicion Inicial Agente: X:{self.x}, Y:{self.y}")
        self.velocidad = 1
        self.human = pg.Rect((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE)
        self.image_human = pg.image.load("classes\images\persona.png")
        #self.image_human = pg.transform.rotate(self.image_human, 90)
    
    def draw_human(self, screen, offset_x, offset_y):
        self.human = pg.Rect((self.x+1) * c.TILE_SIZE + offset_x, (self.y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE)
        pg.draw.rect(screen, c.BLUE, self.human)
        screen.blit(self.image_human, ((self.x + 1) * c.TILE_SIZE + offset_x, (self.y + 1) * c.TILE_SIZE + offset_y))
        #screen.blit(self.image_human, ((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE))

    def actualizar_costo(self, terrain):
        cell_value = terrain.matriz[self.y][self.x]
        print(cell_value)
        cell_type = c.INT_TERRAIN.get(cell_value)
        print(cell_type)
        print(self.cost_movement.get(cell_type))
        self.costo_actual += self.cost_movement.get(cell_type)
        print(f"Costo Actual: {self.costo_actual}")
    #def one_sensor(self, pos_x, pos_y, offset_x, offset_y):
        #unmask la casilla en la que apunta
    #def four_sensors(self, pos_x, pos_y, offset_x, offset_y):
        #unmask las cuatro casillas alrededor
    #def calculate_cost(self, pos_x, pos_y):
        #self.costo_actual += cost_movement.get()

class Agent_Monkey:
    pos_i = None
    pos_f = None
    costo_actual = None
    costo_final = None
    cost_movement = {
        "Montaña": None,
        "Tierra": 1,
        "Agua": 2,
        "Arena": 3,
        "Bosque": 4,
        "Pantano": 5,
        "Nieve": 5,
        "Road": 1
    }
    def __init__(self, y, x):
        self.costo_actual = 0
        self.x = x
        self.y = y
        print(f"Posicion Inicial Agente: X:{self.x}, Y:{self.y}")
        self.velocidad = 1
        self.human = pg.Rect((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE)
        self.image_human = pg.image.load("classes\images\mono.png")
        #self.image_human = pg.transform.rotate(self.image_human, 90)
    
    def draw_human(self, screen, offset_x, offset_y):
        self.human = pg.Rect((self.x+1) * c.TILE_SIZE + offset_x, (self.y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE)
        pg.draw.rect(screen, c.BLUE, self.human)
        screen.blit(self.image_human, ((self.x + 1) * c.TILE_SIZE + offset_x, (self.y + 1) * c.TILE_SIZE + offset_y))
        #screen.blit(self.image_human, ((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE))

    def actualizar_costo(self, terrain):
        cell_value = terrain.matriz[self.y][self.x]
        print(cell_value)
        cell_type = c.INT_TERRAIN.get(cell_value)
        print(cell_type)
        print(self.cost_movement.get(cell_type))
        self.costo_actual += self.cost_movement.get(cell_type)
        print(f"Costo Actual: {self.costo_actual}")
    #def one_sensor(self, pos_x, pos_y, offset_x, offset_y):
        #unmask la casilla en la que apunta
    #def four_sensors(self, pos_x, pos_y, offset_x, offset_y):
        #unmask las cuatro casillas alrededor
    #def calculate_cost(self, pos_x, pos_y):
        #self.costo_actual += cost_movement.get()

class Agent_Octopus:
    pos_i = None
    pos_f = None
    costo_actual = None
    costo_final = None
    cost_movement = {
        "Montaña": None,
        "Tierra": 1,
        "Agua": 2,
        "Arena": 3,
        "Bosque": 4,
        "Pantano": 5,
        "Nieve": 5,
        "Road": 1
    }
    def __init__(self, y, x):
        self.costo_actual = 0
        self.x = x
        self.y = y
        print(f"Posicion Inicial Agente: X:{self.x}, Y:{self.y}")
        self.velocidad = 1
        self.human = pg.Rect((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE)
        self.image_human = pg.image.load("classes\images\pulpo.png")
        #self.image_human = pg.transform.rotate(self.image_human, 90)
    
    def draw_human(self, screen, offset_x, offset_y):
        self.human = pg.Rect((self.x+1) * c.TILE_SIZE + offset_x, (self.y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE)
        pg.draw.rect(screen, c.BLUE, self.human)
        screen.blit(self.image_human, ((self.x + 1) * c.TILE_SIZE + offset_x, (self.y + 1) * c.TILE_SIZE + offset_y))
        #screen.blit(self.image_human, ((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE))

    def actualizar_costo(self, terrain):
        cell_value = terrain.matriz[self.y][self.x]
        print(cell_value)
        cell_type = c.INT_TERRAIN.get(cell_value)
        print(cell_type)
        print(self.cost_movement.get(cell_type))
        self.costo_actual += self.cost_movement.get(cell_type)
        print(f"Costo Actual: {self.costo_actual}")
    #def one_sensor(self, pos_x, pos_y, offset_x, offset_y):
        #unmask la casilla en la que apunta
    #def four_sensors(self, pos_x, pos_y, offset_x, offset_y):
        #unmask las cuatro casillas alrededor
    #def calculate_cost(self, pos_x, pos_y):
        #self.costo_actual += cost_movement.get()

class Agent_Sasquatch:
    pos_i = None
    pos_f = None
    costo_actual = None
    costo_final = None
    cost_movement = {
        "Montaña": None,
        "Tierra": 1,
        "Agua": 2,
        "Arena": 3,
        "Bosque": 4,
        "Pantano": 5,
        "Nieve": 5,
        "Road": 1
    }
    def __init__(self, y, x):
        self.costo_actual = 0
        self.x = x
        self.y = y
        print(f"Posicion Inicial Agente: X:{self.x}, Y:{self.y}")
        self.velocidad = 1
        self.human = pg.Rect((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE)
        self.image_human = pg.image.load("classes\images\pie_grande.png")
        #self.image_human = pg.transform.rotate(self.image_human, 90)
    
    def draw_human(self, screen, offset_x, offset_y):
        self.human = pg.Rect((self.x+1) * c.TILE_SIZE + offset_x, (self.y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE)
        pg.draw.rect(screen, c.BLUE, self.human)
        screen.blit(self.image_human, ((self.x + 1) * c.TILE_SIZE + offset_x, (self.y + 1) * c.TILE_SIZE + offset_y))
        #screen.blit(self.image_human, ((self.x+1)*c.TILE_SIZE, (self.y+1)*c.TILE_SIZE))

    def actualizar_costo(self, terrain):
        cell_value = terrain.matriz[self.y][self.x]
        print(cell_value)
        cell_type = c.INT_TERRAIN.get(cell_value)
        print(cell_type)
        print(self.cost_movement.get(cell_type))
        self.costo_actual += self.cost_movement.get(cell_type)
        print(f"Costo Actual: {self.costo_actual}")
    #def one_sensor(self, pos_x, pos_y, offset_x, offset_y):
        #unmask la casilla en la que apunta
    #def four_sensors(self, pos_x, pos_y, offset_x, offset_y):
        #unmask las cuatro casillas alrededor
    #def calculate_cost(self, pos_x, pos_y):
        #self.costo_actual += cost_movement.get()