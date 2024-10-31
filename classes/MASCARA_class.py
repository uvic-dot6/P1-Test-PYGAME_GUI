import pygame as pg
import constants as c
from .TERRAIN_class import Terrain

class Mask_map:
    masked_surface = []
    
    def __init__(self, terrain):
        for x in range(terrain.tam_fila):
            filas = []
            for y in range(terrain.tam_col):
                filas.append(0)
            self.masked_surface.append(filas)

    def draw_mask(self, offset_x, offset_y, terrain, screen):
        for y in range(terrain.tam_fila):
            for x in range(terrain.tam_col):
                if self.masked_surface[y][x] == 0:
                    pg.draw.rect(screen, c.BLACK_MASK, pg.Rect((x+1) * c.TILE_SIZE + offset_x, (y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE)) # Dibujar celda
                    pg.draw.rect(screen, c.BORDER_GRID, pg.Rect((x+1) * c.TILE_SIZE + offset_x, (y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE), 1) # Dibujar borde de la celda (grid)
                else:
                    color = c.COLORES.get(terrain.matriz[y][x], c.BLACK) # Color correspondiente al valor actual de la matriz
                    pg.draw.rect(screen, color, pg.Rect((x+1) * c.TILE_SIZE + offset_x, (y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE)) # Dibujar celda
                    pg.draw.rect(screen, c.BORDER_GRID, pg.Rect((x+1) * c.TILE_SIZE + offset_x, (y+1) * c.TILE_SIZE + offset_y, c.TILE_SIZE, c.TILE_SIZE), 1) # Dibujar borde de la celda (grid)

    def unmask_mask(self, x, y):
        self.masked_surface[y][x] = 1