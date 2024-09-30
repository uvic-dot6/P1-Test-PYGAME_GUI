import pygame as pg
from pygame.locals import *
import pygame_gui as pgui

pg.init()
"""
#CLASES
class App:
    def __init__(self):
        pg.init()
        flags = RESIZABLE
        App.screen = pg.display.set_mode((640,240),flags)
        App.running = True
    def run(self):
        while App.running:
            for event in pg.event.get():
                if event.type == QUIT:
                    App.running = False
        pg.quit()

if __name__ == '__main__':
            App().run()
"""
#FUNCIONES
def draw_matriz():
    for y in range(tam_fila):
        for x in range(tam_col):
            color = COLORES.get(matriz[y][x], (0, 0, 0))
            pg.draw.rect(screen, color, pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda))
            pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda), 1)
#VARIABLES
    #
COLORES = {
    1: (39, 237, 90),    # Verde - Bosque
    2: (38, 54, 255),    # Azul - Agua
    3: (218, 123, 40),    # Cafe - Tierra
    4: (73, 57, 48),  # Marron Oscuro - Montana
    5: (255, 222, 99),  # Amarillo - Arena
    6: (15, 128, 88),   # Verde Agua - Pantano
    7: (240, 240, 240) # Blanco - Nieve
}
    #Matriz
matriz = []
tam_col = 0
tam_fila = 0
mapa = open("test.txt", "r", encoding = "utf-8")
for x in mapa:
        fila = []
        for num in x.strip():  # Removemos los saltos de línea y espacios extra
            fila.append(int(num))  # Convertimos cada carácter en entero y lo agregamos a la fila
        matriz.append(fila)  # Agregamos la fila completa a la matriz
        tam_col = len(matriz[tam_fila])
        tam_fila += 1
mapa.close()

    #Variables Window
flags = RESIZABLE
tam_celda = 32
pg.display.set_caption("Practica 1 Agentes") #Nombre de la ventana
screen_width = tam_celda * tam_col #Anchor de la pantalla
screen_height = tam_celda * tam_fila #Altura de la pantalla
screen = pg.display.set_mode((screen_width, screen_height), flags) #Objeto Display

    #GUI
background = pg.Surface((screen_width, screen_height))
background.fill(pg.Color(81, 81, 81))
manager = pgui.UIManager((screen_width, screen_height)) #Objeto UIManager
clock = pg.time.Clock()

    #Variable Agent
player = pg.Rect((0, 0, 20, 20))#X,Y,width,heigth
    #Variable Tecla Pulsada

    #Variables GameLoop
run = True
   
#LOOP GAME
while run:
    time_delta = clock.tick(60)/1000.0
    
    #Mostrar Agent Window
        #screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    draw_matriz()
    #pg.draw.rect(screen, (255, 0, 0), player)
    
    #Entrada Teclado Movemennt
    key = pg.key.get_pressed()
    if key[pg.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pg.K_d] == True:
        player.move_ip(1, 0)
    elif key[pg.K_s] == True:
        player.move_ip(0, 1)
    elif key[pg.K_w] == True:
        player.move_ip(0, -1)
    
    #Eventos
    for event in pg.event.get():
        #Cerrar Window
        if event.type == pg.QUIT:
            run = False
        manager.process_events(event)
    
    manager.update(time_delta)
    
    manager.draw_ui(screen)
    
    pg.display.update()

pg.quit()