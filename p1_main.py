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
        
        #for x in self.matriz:
            #print(x)
    
    def draw_matriz(self, screen, tam_celda):
        for y in range(self.tam_fila):
            for x in range(self.tam_col):
                color = self.colores.get(self.matriz[y][x], (0, 0, 0))
                pg.draw.rect(screen, color, pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda))
                pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda), 1)
        
    def draw_box(self, x, y, screen, tam_celda):
        color = self.colores.get(self.matriz[y][x], (0, 0, 0))
        pg.draw.rect(screen, color, pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda))
        pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda), 1)

    def change_value(self, x, y, new_value, screen, tam_celda):
        self.matriz[x][y] = new_value
        self.draw_box(x, y, screen, tam_celda)

class App:
    tam_celda = 32
    screen_width = 0
    screen_height = 0

    def __init__(self, tam_col, tam_fila):
        pg.init()
        flags = RESIZABLE
        self.definir_ancho_alto(tam_col, tam_fila)
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height), flags)
        self.running = True

    def definir_ancho_alto(self, tam_col, tam_fila):
        self.screen_width = self.tam_celda * tam_col
        self.screen_height = self.tam_celda * tam_fila

    def run(self, tablero):
        while self.running:
            tablero.draw_matriz(self.screen, self.tam_celda)
            for event in pg.event.get():
                if event.type == QUIT:
                    self.running = False
            pg.display.update()
        pg.quit()

########################################    M A I N
if __name__ == '__main__':
    tablero = Tablero()
    tablero.llenar_matriz()

    App(tablero.tam_col,tablero.tam_fila).run(tablero)