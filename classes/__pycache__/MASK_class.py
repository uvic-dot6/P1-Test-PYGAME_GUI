import pygame as pg
import constants as c
from TERRAIN_class import Terrain
from APP_class import App

class Mask_Map:
    
    def __init__(self, terrain):
        mask = pg.Mask(c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT)

        for y in range(0, c.TILE_SIZE):
            for x in range(0, c.TILE_SIZE * terrain.tam_col):
                mask.set_at((x, y), 1)\
                
        for x in range(0, c.TILE_SIZE):
            for y in range(c.TILE_SIZE, c.TILE_SIZE * terrain.tam_fila):
                mask.set_at((x, y), 1)