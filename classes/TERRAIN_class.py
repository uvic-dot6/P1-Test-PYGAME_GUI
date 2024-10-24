import constants as c
import pygame as pg
from pygame.locals import *

class Terrain:
    visited = [(1,1),(1,2),(1,3),(2,3)]
    decision = [(1,1),(1,2),(1,3),(2,3)]
    initial_point = None #(X,Y)
    end_point = None #(X,Y)
    actual_position = []
    
    text_list = []
    num_list = []
    matriz = []
    tam_fila = 0
    tam_col = 0

    def __init__(self, file):
        self.llenar_matriz(file)
    
    #Crear mapa
    def llenar_matriz(self, file):
        with open(file, "r", encoding = "utf-8") as mapa: #Se abre el nuevo archivo
            for x in mapa: #Se recorre cada renglon del mapa
                filas = [] #Se crea una nueva fila
                for num_sel in x.strip():  # Removemos los saltos de línea y espacios extra
                    filas.append(int(num_sel))  # Convertimos cada carácter en entero y lo agregamos a la fila
                self.matriz.append(filas)  # Agregamos la fila completa a la matriz
                self.tam_fila += 1 # Cada vez que se agrega una fila se suma
        self.tam_col = len(self.matriz[self.tam_fila-1]) # Se obtiene el valor de la ultima fila agregada para obtener el numero de columnas
        
        for x in self.matriz:
            print(x)
    
    #Dibujar el terreno
    def draw_matriz(self, screen, offset_x, offset_y):
        for y in range(self.tam_fila):
            for x in range(self.tam_col):
                color = c.COLORES.get(self.matriz[y][x], c.BLACK) # Color correspondiente al valor actual de la matriz
                
                pg.draw.rect(screen, color, pg.Rect((x+1) * c.TILE_SIZE + offset_x, (y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE)) # Dibujar celda
                pg.draw.rect(screen, c.BORDER_GRID, pg.Rect((x+1) * c.TILE_SIZE + offset_x, (y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE), 1) # Dibujar borde de la celda (grid)
                
                
    #Dibujar sistema de coordenadas
    def draw_grid(self, screen, offset_x, offset_y):
        # Dibujar los recuadros de las etiquetas (columnas)
        for x in range(self.tam_col + 1):
            label_x = x - (offset_x // c.TILE_SIZE)
            if label_x >= 0 and label_x <= self.tam_col: 
                pg.draw.rect(screen, c.BLUE, pg.Rect(x * c.TILE_SIZE + offset_x % c.TILE_SIZE, 0, c.TILE_SIZE, c.TILE_SIZE))
                pg.draw.rect(screen, c.BLUE_BORDER, pg.Rect(x * c.TILE_SIZE + offset_x % c.TILE_SIZE, 0, c.TILE_SIZE, c.TILE_SIZE), 1)

        # Dibujar los recuadros de las etiquetas (filas)
        for y in range(1, self.tam_fila + 1):
            label_y = y - (offset_y // c.TILE_SIZE)
            if label_y > 0 and label_y <= self.tam_fila:
                pg.draw.rect(screen, c.BLUE, pg.Rect(0, y * c.TILE_SIZE + offset_y % c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
                pg.draw.rect(screen, c.BLUE_BORDER, pg.Rect(0, y * c.TILE_SIZE + offset_y % c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)
        
        #Etiquetar las filas A - Z
        for x in range(1, self.tam_col + 1):
            label_x = x - (offset_x // c.TILE_SIZE)
            if label_x > 0 and label_x <= self.tam_col:  # Mostrar solo las etiquetas visibles
                label = chr(64 + label_x)  # A es 65 en ASCII
                font = pg.font.Font(None, 24)
                text_surface = font.render(label, True, c.WHITE)
                screen.blit(text_surface, (4 + x * c.TILE_SIZE + offset_x % c.TILE_SIZE, 4))
        
        # Etiquetar las columnas con numeros
        for y in range(1, self.tam_fila + 1):
            label_y = y - (offset_y // c.TILE_SIZE)
            if label_y > 0 and label_y <= self.tam_fila:  # Mostrar solo las etiquetas visibles
                label = str(label_y)
                font = pg.font.Font(None, 24)
                text_surface = font.render(label, True, c.WHITE)
                screen.blit(text_surface, (4, y * c.TILE_SIZE + 4 + offset_y % c.TILE_SIZE))
    
    #Cambiar un valor de la matriz
    def change_value(self, x, y, new_value, screen):
        self.matriz[x][y] = new_value
        self.draw_box(x, y, screen)    
    
    #Dibujar una celda
    def draw_box(self, x, y, screen):
        color = c.COLORES.get(self.matriz[x][y], c.BLACK)
        pg.draw.rect(screen, color, pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
        pg.draw.rect(screen, c.BORDER_GRID, pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)

    #Consultar el valor actual de la celda
    def current_value(self, x, y):
        value_matriz = self.matriz[x][y]
        return c.INT_TERRAIN.get(value_matriz)
    
    def convert_coordinate_to_letter(self, x):
        return chr(x + 65)
    def convert_letter_to_coordinate(self, text):
        a = ord(text) - 65
        print(a)
        return a
    
    def asignar_celda_inicial(self, x, y):
        #print(f"Valor de X: {x}")
        #print(f"Valor de Y: {y}")
        self.initial_point = (x, y)
    def asignar_celda_final(self, x, y):
        self.end_point = (x, y)
    
    def draw_i(self, screen, offset_x, offset_y):
        label = chr(73)  # I es 73 en ASCII
        font = pg.font.Font(None, 18)
        text_surface = font.render(label, True, c.WHITE, c.BLACK)
        screen.blit(text_surface, (2 + (self.initial_point[1]+1) * c.TILE_SIZE + offset_x, (self.initial_point[0]+1) * c.TILE_SIZE + offset_y + 16))

    def draw_f(self, screen, offset_x, offset_y):
        label = chr(70)  # F es 73 en ASCII
        font = pg.font.Font(None, 18)
        text_surface = font.render(label, True, c.WHITE, c.BLACK)
        screen.blit(text_surface, (16 + (self.end_point[1]+1) * c.TILE_SIZE + offset_x, (self.end_point[0]+1) * c.TILE_SIZE + offset_y + 16))

    def draw_v(self, screen, offset_x, offset_y):
        label = chr(86) # V es 86 en ASCII
        font = pg.font.Font(None, 18)
        text_surface = font.render(label, True, c.WHITE, c.BLACK)
        for v in self.visited:
            screen.blit(text_surface, (2 + v[1] * c.TILE_SIZE + offset_x, v[0] * c.TILE_SIZE + offset_y + 1))

    def draw_o(self, screen, offset_x, offset_y):
        label = chr(79) # O es 79 en ASCII
        font = pg.font.Font(None, 18)
        text_surface = font.render(label, True, c.WHITE, c.BLACK)
        for o in self.decision:
            screen.blit(text_surface, (16 + o[1] * c.TILE_SIZE + offset_x, o[0] * c.TILE_SIZE + offset_y + 1))
