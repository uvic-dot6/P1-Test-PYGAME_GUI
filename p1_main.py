import constants as c
import pygame as pg
from pygame.locals import *
import pygame_gui as pgui



class Maze:
    matriz = []
    tam_fila = 0
    tam_col = 0
    
    colores = {
        1: (255, 255, 255),    # Blanco - Road
        2: (0, 0, 0)    # Negro - Wall

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
    
    def draw_matriz(self, screen):
        for y in range(self.tam_fila):
            for x in range(self.tam_col):
                color = self.colores.get(self.matriz[y][x], (0, 0, 0))
                pg.draw.rect(screen, color, pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
                pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)
    
    def change_value(self, x, y, new_value, screen):
        self.matriz[x][y] = new_value
        self.draw_box(x, y, screen)    
    
    def draw_box(self, x, y, screen):
        color = self.colores.get(self.matriz[x][y], (0, 0, 0))
        pg.draw.rect(screen, color, pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
        pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)

    def current_value(self, x, y):
        return self.matriz[x][y]

class Terrain:
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
    
    def draw_matriz(self, screen):
        for y in range(self.tam_fila):
            for x in range(self.tam_col):
                color = self.colores.get(self.matriz[y][x], (0, 0, 0))
                pg.draw.rect(screen, color, pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
                pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)
    
    def change_value(self, x, y, new_value, screen):
        self.matriz[x][y] = new_value
        self.draw_box(x, y, screen)    
    
    def draw_box(self, x, y, screen):
        color = self.colores.get(self.matriz[x][y], (0, 0, 0))
        pg.draw.rect(screen, color, pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
        pg.draw.rect(screen, (81, 81, 81), pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)

    def current_value(self, x, y):
        return self.matriz[x][y]

class App:
    selected_cell = None
    
    def __init__(self):
        pg.init()
        pg.display.set_caption("Practica 1")
        #lags = RESIZABLE
        self.clock = pg.time.Clock()
        #self.definir_ancho_alto(tam_col, tam_fila)
        self.screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
        #self.screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, self.screen_height), flags)
        self.ui_manager = pgui.UIManager((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
        #Side Panel
            #1
        self.side_panel_layout_rect = pg.Rect(0, 0, c.SIDE_PANEL, c.SCREEN_HEIGHT//2)
        screen_width = self.screen.get_width()
        self.side_panel_layout_rect.topright = (screen_width, 0)
        self.side_panel_top = pgui.elements.UIPanel(
            relative_rect = self.side_panel_layout_rect,  # Panel lateral en el lado derecho
            starting_height = 1,
            manager = self.ui_manager
        )
            #2
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        self.side_panel_layout_rect.bottomright = (screen_width, screen_height)
        self.side_panel_bottom = pgui.elements.UIPanel(
            relative_rect = self.side_panel_layout_rect,  # Panel lateral en el lado derecho
            starting_height = 1,
            manager = self.ui_manager
        )
        #self.recreate_ui()
        #self.hello_button = None
        self.load_map = None
        self.type_terrain = None
        self.test_drop_down = None
        self.coordinates_cell = None
        self.current_position = None
        
        # Inicializa los botones
        self.init_ui()

        self.running = True

    #def definir_ancho_alto(self, tam_col, tam_fila):
        #c.SCREEN_WIDTH = self.c.TILE_SIZE * tam_col
        #self.screen_height = self.c.TILE_SIZE * tam_fila
    
    def init_ui(self):
         # Inicializa los elementos de UI sin mostrarlos al principio
        """
        self.hello_button = pgui.elements.UIButton(
            relative_rect = pg.Rect((c.SCREEN_WIDTH + 20, 20), (100, 50)),
            text = 'Say Hello',
            manager = self.ui_manager,
            visible = False  # Se crea invisible al principio
        )"""
        self.load_map = pgui.elements.UIButton(
            relative_rect = pg.Rect((15, 15), (100, 50)),
            text = 'Load Map',
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = True  # Se crea invisible al principio
        )

        self.type_terrain = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 60), (100, 20)),
            text = 'Type Terrain',
            manager = self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )

        self.test_drop_down = pgui.elements.UIDropDownMenu(
            ['1', '2', '3', '4', '5', '6', '7'],
            '1',
            pg.Rect((15, 85), (100, 50)),
            self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )

        self.current_position = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 15), (120, 20)),
            text = 'Current Position',
            manager = self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )

        self.coordinates_cell = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 35), (100, 20)),
            text = 'X: 0, Y: 0',
            manager = self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )
        


    
    def update_ui(self, cell_pos, Terrain):
        # Actualiza la posición de los botones y los valores
        #self.hello_button.set_position((c.SCREEN_WIDTH + 20, 20))
        #self.load_map.set_position((15, 15))
        self.type_terrain.set_relative_position((15, 60))
        self.current_position.set_relative_position((15, 15))
        self.coordinates_cell.set_relative_position((15, 35))
        
        # Elimina el menú desplegable existente
        if self.test_drop_down is not None:
            self.test_drop_down.kill()
        if self.coordinates_cell is not None:
            self.coordinates_cell.kill()

        #Crea un nuevo label con el valor actualizado
        new_coordinate = "X: " + str(cell_pos[0]) + ", Y: " + str(cell_pos[1])
        self.coordinates_cell = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 35), (100, 20)),
            text = new_coordinate,
            container = self.side_panel_top,
            manager = self.ui_manager
        )
        # Crea un nuevo menú desplegable con el valor actualizado de la celda seleccionada
        current_value = str(Terrain.current_value(cell_pos[0], cell_pos[1]))
        self.test_drop_down = pgui.elements.UIDropDownMenu(
            ['1', '2', '3', '4', '5', '6', '7'],
            current_value,
            pg.Rect((15, 85), (100, 50)),
            self.ui_manager,
            container = self.side_panel_top
        )

        # Mostrar los elementos si están ocultos
        #if not self.hello_button.visible:
            #self.hello_button.show()
        if not self.test_drop_down.visible:
            self.test_drop_down.show()
        self.type_terrain.show()
        self.coordinates_cell.show()
        self.current_position.show()

    def process_events(self, Terrain):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False

            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Clic izquierdo
                mouse_pos = event.pos
                cell_x = mouse_pos[0] // c.TILE_SIZE
                cell_y = mouse_pos[1] // c.TILE_SIZE

                if 0 <= cell_x < Terrain.tam_col and 0 <= cell_y < Terrain.tam_fila:
                    self.selected_cell = (cell_y, cell_x)
                    print(f"Celda seleccionada: ({cell_y}, {cell_x})")
                    # Mostrar botones cuando una celda es seleccionada
                    self.update_ui(self.selected_cell, Terrain)
            
            self.ui_manager.process_events(event)

            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == self.load_map:
                    print('Haz presionado Load Map')

            if (event.type == pgui.UI_DROP_DOWN_MENU_CHANGED and event.ui_element == self.test_drop_down):
                new_value = int(event.text)
                print(new_value, self.selected_cell[0], self.selected_cell[1])
                if self.selected_cell:
                    Terrain.change_value(self.selected_cell[0], self.selected_cell[1], new_value, self.screen)

                self.update_ui(self.selected_cell, Terrain)
                
    def run(self, Terrain):
        while self.running:
            self.time_delta = self.clock.tick(c.FPS)

            # Limpiar la pantalla antes de dibujar
            self.screen.fill((0, 0, 0))
            # Dibujar Terrain
            Terrain.draw_matriz(self.screen)
            # Check for inputs
            self.process_events(Terrain)
            # Respond to input
            self.ui_manager.update(self.time_delta)
            # Dibujar la UI
            self.ui_manager.draw_ui(self.screen)
            pg.display.update()
        pg.quit()

########################################    M A I N
if __name__ == '__main__':
    Terrain = Terrain()
    Terrain.llenar_matriz()
    app = App()

    app.run(Terrain)