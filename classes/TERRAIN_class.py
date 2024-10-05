import constants as c
import pygame as pg
from pygame.locals import *

class Terrain:
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
    def draw_matriz(self, screen):
        for y in range(self.tam_fila):
            for x in range(self.tam_col):
                color = c.COLORES.get(self.matriz[y][x], c.BLACK) # Color correspondiente al valor actual de la matriz
                pg.draw.rect(screen, color, pg.Rect((x+1) * c.TILE_SIZE, (y+1) * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE)) # Dibujar celda
                pg.draw.rect(screen, c.BORDER_GRID, pg.Rect((x+1) * c.TILE_SIZE, (y+1) * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1) # Dibujar borde de la celda (grid)
    
    #Dibujar sistema de coordenadas
    def draw_grid(self, screen):
        # Dibuja los recuadros de las letras
        for x in range(self.tam_col + 1):
            pg.draw.rect(screen, c.BROWN, pg.Rect(x * c.TILE_SIZE, 0, c.TILE_SIZE, c.TILE_SIZE))
            pg.draw.rect(screen, c.WHITE, pg.Rect(x * c.TILE_SIZE, 0, c.TILE_SIZE, c.TILE_SIZE), 1)
        # Dibuja los recuadros de las numeros
        for y in range(1, self.tam_fila + 1):
            pg.draw.rect(screen, c.BROWN, pg.Rect(0, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
            pg.draw.rect(screen, c.WHITE, pg.Rect(0, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)
        
        #Etiquetar las filas A - Z
        for x in range(1, self.tam_col + 1):
            label = chr(64 + x)  # A es 65 en ASCII
            font = pg.font.Font(None, 24)
            text_surface = font.render(label, True, c.WHITE)
            screen.blit(text_surface, (4 + x * c.TILE_SIZE, 4))
        
        # Etiquetar las columnas con numeros
        for y in range(1, self.tam_fila + 1):
            label = str(y)
            font = pg.font.Font(None, 24)
            text_surface = font.render(label, True, c.WHITE)
            screen.blit(text_surface, (4, y * c.TILE_SIZE + 4))
    
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