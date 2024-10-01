import constants as c
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
        
        for x in self.matriz:
            print(x)
    
    def draw_matriz(self, screen, tam_celda):
        for y in range(self.tam_fila):
            for x in range(self.tam_col):
                color = self.colores.get(self.matriz[y][x], (0, 0, 0))
                pg.draw.rect(screen, color, pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda))
                pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda), 1)
        
    def draw_box(self, x, y, screen, tam_celda):
        color = self.colores.get(self.matriz[x][y], (0, 0, 0))
        pg.draw.rect(screen, color, pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda))
        pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * tam_celda, y * tam_celda, tam_celda, tam_celda), 1)

    def change_value(self, x, y, new_value, screen, tam_celda):
        self.matriz[x][y] = new_value
        self.draw_box(x, y, screen, tam_celda)

    def current_value(self, x, y):
        return self.matriz[x][y]

class App:
    tam_celda = 32
    screen_width = 0
    screen_height = 0
    selected_cell = None
    
    def __init__(self, tam_col, tam_fila):
        pg.init()
        pg.display.set_caption("Practica 1")
        #lags = RESIZABLE
        self.clock = pg.time.Clock()
        self.definir_ancho_alto(tam_col, tam_fila)
        self.screen = pg.display.set_mode((self.screen_width + c.SIDE_PANEL, self.screen_height))
        #self.screen = pg.display.set_mode((self.screen_width + c.SIDE_PANEL, self.screen_height), flags)
        
        self.ui_manager = pgui.UIManager((self.screen_width + c.SIDE_PANEL, self.screen_height))
        #self.recreate_ui()
        #self.hello_button = None
        self.type_terrain= None
        self.test_drop_down = None
        self.coordinates_cell = None
        self.current_position = None
        
        # Inicializa los botones
        self.init_ui()

        self.running = True

    def definir_ancho_alto(self, tam_col, tam_fila):
        self.screen_width = self.tam_celda * tam_col
        self.screen_height = self.tam_celda * tam_fila
    
    def init_ui(self):
         # Inicializa los elementos de UI sin mostrarlos al principio
        """
        self.hello_button = pgui.elements.UIButton(
            relative_rect = pg.Rect((self.screen_width + 20, 20), (100, 50)),
            text = 'Say Hello',
            manager = self.ui_manager,
            visible = False  # Se crea invisible al principio
        )"""

        self.type_terrain = pgui.elements.UILabel(
            relative_rect = pg.Rect((self.screen_width + 20, 20), (100, 50)),
            text = 'Type Terrain',
            manager = self.ui_manager,
            visible = False  # Se crea invisible al principio
        )

        self.test_drop_down = pgui.elements.UIDropDownMenu(
            ['1', '2', '3', '4', '5', '6', '7'],
            '1',
            pg.Rect((self.screen_width + 20, 80), (100, 50)),
            self.ui_manager,
            visible = False  # Se crea invisible al principio
        )

        self.current_position = pgui.elements.UILabel(
            relative_rect = pg.Rect((self.screen_width + 20, 140), (120, 20)),
            text = 'Current Position',
            manager = self.ui_manager,
            visible = False  # Se crea invisible al principio
        )

        self.coordinates_cell = pgui.elements.UILabel(
            relative_rect = pg.Rect((self.screen_width + 20, 160), (120, 20)),
            text = 'X: 0, Y: 0',
            manager = self.ui_manager,
            visible = False  # Se crea invisible al principio
        )


    
    def update_ui(self, cell_pos, tablero):
        # Actualiza la posición de los botones y los valores
        #self.hello_button.set_position((self.screen_width + 20, 20))
        self.type_terrain.set_position((self.screen_width + 20, 20))
        self.current_position.set_position((self.screen_width + 20, 140))
        self.coordinates_cell.set_position((self.screen_width + 20, 160))
        
        # Elimina el menú desplegable existente
        if self.test_drop_down is not None:
            self.test_drop_down.kill()
        if self.coordinates_cell is not None:
            self.coordinates_cell.kill()

        #Crea un nuevo label con el valor actualizado
        new_coordinate = "X: " + str(cell_pos[0]) + ", Y: " + str(cell_pos[1])
        self.coordinates_cell = pgui.elements.UILabel(
            relative_rect = pg.Rect((self.screen_width + 20, 160), (120, 20)),
            text = new_coordinate,
            manager = self.ui_manager
        )
        # Crea un nuevo menú desplegable con el valor actualizado de la celda seleccionada
        current_value = str(tablero.current_value(cell_pos[0], cell_pos[1]))
        self.test_drop_down = pgui.elements.UIDropDownMenu(
            ['1', '2', '3', '4', '5', '6', '7'],
            current_value,
            pg.Rect((self.screen_width + 20, 80), (100, 50)),
            self.ui_manager
        )

        # Mostrar los elementos si están ocultos
        #if not self.hello_button.visible:
            #self.hello_button.show()
        if not self.test_drop_down.visible:
            self.test_drop_down.show()
        self.type_terrain.show()
        self.coordinates_cell.show()
        self.current_position.show()

    def process_events(self, tablero):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Clic izquierdo
                mouse_pos = event.pos
                cell_x = mouse_pos[0] // self.tam_celda
                cell_y = mouse_pos[1] // self.tam_celda

                if 0 <= cell_x < tablero.tam_col and 0 <= cell_y < tablero.tam_fila:
                    self.selected_cell = (cell_y, cell_x)
                    print(f"Celda seleccionada: ({cell_y}, {cell_x})")
                    # Mostrar botones cuando una celda es seleccionada
                    self.update_ui(self.selected_cell, tablero)
            
            self.ui_manager.process_events(event)

            #if event.type == pgui.UI_BUTTON_PRESSED:
                #if event.ui_element == self.hello_button:
                    #print('Hello World!')

            if (event.type == pgui.UI_DROP_DOWN_MENU_CHANGED and event.ui_element == self.test_drop_down):
                new_value = int(event.text)
                print(new_value, self.selected_cell[0], self.selected_cell[1])
                if self.selected_cell:
                    tablero.change_value(self.selected_cell[0], self.selected_cell[1], new_value, self.screen, self.tam_celda)

                self.update_ui(self.selected_cell, tablero)
                
    def run(self, tablero):
        while self.running:
            self.time_delta = self.clock.tick(c.FPS)

            # Limpiar la pantalla antes de dibujar
            self.screen.fill((0, 0, 0))
            # Dibujar tablero
            tablero.draw_matriz(self.screen, self.tam_celda)
            # Check for inputs
            self.process_events(tablero)
            # Respond to input
            self.ui_manager.update(self.time_delta)
            # Dibujar la UI
            self.ui_manager.draw_ui(self.screen)
            pg.display.update()
        pg.quit()

########################################    M A I N
if __name__ == '__main__':
    tablero = Tablero()
    tablero.llenar_matriz()
    app = App(tablero.tam_col, tablero.tam_fila)

    app.run(tablero)