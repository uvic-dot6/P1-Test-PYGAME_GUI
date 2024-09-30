import pygame as pg
from pygame.locals import *
import pygame_gui as pgui


class Tablero:
    matriz = []
    tam_fila = 0
    tam_col = 0
    colores = {
        1: (39, 237, 90),    # Verde - Bosque
        2: (38, 54, 255),    # Azul - Agua
        3: (218, 123, 40),    # Cafe - Tierra
        4: (73, 57, 48),  # Marron Oscuro - Montana
        5: (255, 222, 99),  # Amarillo - Arena
        6: (15, 128, 88),   # Verde Agua - Pantano
        7: (240, 240, 240) # Blanco - Nieve
    }

    #def __init__(self, ):
            
    def llenar_matriz(self):
        mapa = open("test.txt", "r", encoding = "utf-8")
        for x in mapa:
            filas = []
            for num_sel in x.strip():  # Removemos los saltos de línea y espacios extra
                filas.append(int(num_sel))  # Convertimos cada carácter en entero y lo agregamos a la fila
            self.matriz.append(filas)  # Agregamos la fila completa a la matriz
            self.tam_col = len(self.matriz[self.tam_fila])
            self.tam_fila += 1
        mapa.close()
    
    def draw_matriz(self, screen):
        for y in range(tam_fila):
            for x in range(tam_col):
                color = colores.get(matriz[y][x], (0, 0, 0))
                pg.draw.rect(screen, color, pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda))
                pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda), 1)

class App:
    tam_celda = 32
    screen_width = 0
    screen_height = 0

    def __init__(self, tam_col, tam_fila):
        pg.init()
        flags = RESIZABLE
        self.definir_ancho_alto(tam_col, tam_fila)
        App.screen = pg.display.set_mode((self.screen_width, self.screen_height), flags)
        App.running = True

    def definir_ancho_alto(self, tam_col, tam_fila):
        self.screen_width = self.tam_celda * tam_col
        self.screen_height = self.tam_celda * tam_fila

    def run(self):
        while App.running:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.App.running = False
        pg.quit()

########################################    M A I N
if __name__ == '__main__':
    tablero = Tablero()
    tablero.llenar_matriz()

    App(tablero.tam_col,tablero.tam_fila).run()