import pygame as pg
import constants as c
from .TERRAIN_class import Terrain

class Mask_Map:
    masked_surface = None
    mask = None
    def __init__(self, terrain, screen, offset_x, offset_y):
        #(Columna,Fila)
        #Crea una superficie del tamaño del mapa
        surface_size = (c.TILE_SIZE * (terrain.tam_col + 1), c.TILE_SIZE * (terrain.tam_fila + 1))
        #surface = pg.Surface(surface_size)

        terrain.draw_grid(screen, offset_x, offset_y)   #Dibuja el grid
        terrain.draw_matriz(screen, offset_x, offset_y) #Dibuja la matriz

        self.mask = pg.Mask(surface_size)   #Crea una mascara del tamaño del mapa

        # Definir qué píxeles de la máscara son visibles (valor 1 en la máscara)
        #set_at define un pixel como visible
        for y in range(0, c.TILE_SIZE):
            for x in range(0, c.TILE_SIZE * (terrain.tam_col+1)):
                self.mask.set_at((x, y), 1) #Desenmascara los numeros
        # Definir qué píxeles de la máscara son visibles (valor 1 en la máscara)         
        for x in range(0, c.TILE_SIZE):
            for y in range(c.TILE_SIZE, c.TILE_SIZE * (terrain.tam_fila+1)):
                self.mask.set_at((x, y), 1) #Desenmascara las letras

        #Area que se muestra en la pantalla
        self.masked_surface = pg.Surface(surface_size, pg.SRCALPHA)
        self.pixeles_iniciales(screen)

    def pixeles_iniciales(self,screen):    
        # Copiar los píxeles visibles de la superficie original a la máscara
        # Aqui se "guardan" los pixeles originales que se pueden ver junto a la mascara en masked_surface
        #print(f"N:{surface_size[1]} M:{surface_size[0]}")
        for y in range(c.SCREEN_WIDTH):
            for x in range(c.SCREEN_HEIGHT):
                #print(f"N:{y} M:{x}")
                if self.mask.get_at((x, y)):  # Si el píxel está visible en la máscara
                    self.masked_surface.set_at((x, y), screen.get_at((x, y))) # Dibuja los pixeles visibles sin offset
    
    def unmask(self, cell_x, cell_y, mascara, screen, terrain, offset_x, offset_y, initial, agent):
        
        terrain.draw_matriz(screen, offset_x, offset_y)
        
        """if initial == False: 
            #agent.draw_human(screen, offset_x, offset_y)
            terrain.draw_i(screen, offset_x, offset_y)
            terrain.draw_f(screen, offset_x, offset_y)
            terrain.draw_v(screen, offset_x, offset_y)
            terrain.draw_o(screen, offset_x, offset_y)"""

        terrain.draw_grid(screen, offset_x, offset_y)

        for y in range(((cell_y * c.TILE_SIZE) + 32), (((cell_y + 1) * c.TILE_SIZE) + 32)):  # Esto crea un cuadrado
            for x in range(((cell_x * c.TILE_SIZE) + 32), (((cell_x + 1) * c.TILE_SIZE) + 32)):
                self.mask.set_at((x, y), 1)  # Hacer visible esta área en la máscara(BORRAR)
        
        for y in range(((cell_y * c.TILE_SIZE) + 32), (((cell_y + 1) * c.TILE_SIZE) + 32)):
            for x in range(((cell_x * c.TILE_SIZE) + 32), (((cell_x + 1) * c.TILE_SIZE) + 32)):
                if self.mask.get_at((x, y)):  # Si el píxel está visible en la máscara(PEGAR)
                    self.masked_surface.set_at((x, y), screen.get_at((x, y)))
