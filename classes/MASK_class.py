import pygame as pg
import constants as c
from .TERRAIN_class import Terrain

class Mask_Map:
    masked_surface = None
    mask = None
    def __init__(self, terrain, screen):
        surface_size = (c.TILE_SIZE * (terrain.tam_col + 1), c.TILE_SIZE * (terrain.tam_fila + 1))
        #surface = pg.Surface(surface_size)
        terrain.draw_grid(screen)
        terrain.draw_matriz(screen)
        self.mask = pg.Mask(surface_size)
        # Definir qué píxeles de la máscara son visibles (valor 1 en la máscara)
        for y in range(0, c.TILE_SIZE):
            for x in range(0, c.TILE_SIZE * (terrain.tam_col+1)):
                self.mask.set_at((x, y), 1)
        # Definir qué píxeles de la máscara son visibles (valor 1 en la máscara)         
        for x in range(0, c.TILE_SIZE):
            for y in range(c.TILE_SIZE, c.TILE_SIZE * (terrain.tam_fila+1)):
                self.mask.set_at((x, y), 1)

        self.masked_surface = pg.Surface(surface_size, pg.SRCALPHA)
        # Copiar los píxeles visibles de la superficie original a la máscara
        for y in range(surface_size[1]):
            for x in range(surface_size[0]):
                if self.mask.get_at((x, y)):  # Si el píxel está visible en la máscara
                    self.masked_surface.set_at((x, y), screen.get_at((x, y)))
    
    def unmask(self, cell_x, cell_y, mascara, screen, terrain):
        terrain.draw_grid(screen)
        terrain.draw_matriz(screen)
        for y in range(((cell_y * c.TILE_SIZE) + 32), (((cell_y + 1) * c.TILE_SIZE) + 32)):  # Esto crea un cuadrado
            for x in range(((cell_x * c.TILE_SIZE) + 32), (((cell_x + 1) * c.TILE_SIZE) + 32)):
                self.mask.set_at((x, y), 1)  # Hacer visible esta área en la máscara
        
        for y in range(((cell_y * c.TILE_SIZE) + 32), (((cell_y + 1) * c.TILE_SIZE) + 32)):
            for x in range(((cell_x * c.TILE_SIZE) + 32), (((cell_x + 1) * c.TILE_SIZE) + 32)):
                if self.mask.get_at((x, y)):  # Si el píxel está visible en la máscara
                    self.masked_surface.set_at((x, y), screen.get_at((x, y)))
