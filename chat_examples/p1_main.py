import tkinter as tk
from tkinter import filedialog
import constants as c
import pygame as pg
from pygame.locals import *
import pygame_gui as pgui

class Terrain:
    matriz = []
    tam_fila = 0
    tam_col = 0

    def __init__(self, file):
        self.llenar_matriz(file)

            
    def llenar_matriz(self, file):
        with open(file, "r", encoding = "utf-8") as mapa:
        #mapa = open("maze.txt", "r", encoding = "utf-8")
            for x in mapa:
                filas = []
                for num_sel in x.strip():  # Removemos los saltos de línea y espacios extra
                    filas.append(int(num_sel))  # Convertimos cada carácter en entero y lo agregamos a la fila
                self.matriz.append(filas)  # Agregamos la fila completa a la matriz
                self.tam_col = len(self.matriz[self.tam_fila])
                self.tam_fila += 1
            #mapa.close()
        for x in self.matriz:
            print(x)
    
    def draw_matriz(self, screen):
        for y in range(self.tam_fila):
            for x in range(self.tam_col):
                #color = self.colores.get(self.matriz[y][x], c.BLACK)
                color = c.COLORES.get(self.matriz[y][x], c.BLACK)
                pg.draw.rect(screen, color, pg.Rect((x+1) * c.TILE_SIZE, (y+1) * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
                pg.draw.rect(screen, c.BORDER_GRID, pg.Rect((x+1) * c.TILE_SIZE, (y+1) * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)
    
    def draw_grid(self, screen):
        for x in range(self.tam_col + 1):
            pg.draw.rect(screen, c.BROWN, pg.Rect(x * c.TILE_SIZE, 0, c.TILE_SIZE, c.TILE_SIZE))
            pg.draw.rect(screen, c.WHITE, pg.Rect(x * c.TILE_SIZE, 0, c.TILE_SIZE, c.TILE_SIZE), 1)
        for y in range(1, self.tam_fila + 1):
            pg.draw.rect(screen, c.BROWN, pg.Rect(0, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
            pg.draw.rect(screen, c.WHITE, pg.Rect(0, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)
        
        #Etiquetar las filas
        for x in range(1, self.tam_col + 1):
            label = chr(64 + x)  # A es 65 en ASCII
            font = pg.font.Font(None, 24)
            text_surface = font.render(label, True, c.WHITE)
            screen.blit(text_surface, (4 + x * c.TILE_SIZE, 4))
        
        # Etiquetar las columnas
        for y in range(1, self.tam_fila + 1):
            label = str(y)
            font = pg.font.Font(None, 24)
            text_surface = font.render(label, True, c.WHITE)
            screen.blit(text_surface, (4, y * c.TILE_SIZE + 4))
    
    def change_value(self, x, y, new_value, screen):
        self.matriz[x][y] = new_value
        self.draw_box(x, y, screen)    
    
    def draw_box(self, x, y, screen):
        #color = self.colores.get(self.matriz[x][y], (0, 0, 0))
        color = c.COLORES.get(self.matriz[x][y], c.BLACK)
        pg.draw.rect(screen, color, pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE))
        pg.draw.rect(screen, c.BORDER_GRID, pg.Rect(x * c.TILE_SIZE, y * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE), 1)

    def current_value(self, x, y):
        TERRAIN_TYPE = {
        1: "Bosque",    # Verde - Bosque
        2: "Agua",    # Azul - Agua
        3: "Tierra",    # Cafe - Tierra
        4: "Montaña",  # Marron Oscuro - Montana
        5: "Arena",  # Amarillo - Arena
        6: "Pantano",   # Verde Agua - Pantano
        7: "Nieve", # Blanco - Nieve
        8: "Wall", #Negro - Wall
        9: "Road" #Blanco - Road
        }
        value_matriz = self.matriz[x][y]
        return TERRAIN_TYPE.get(value_matriz)

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

        # Inicializar boton cargar mapa
        self.load_map = pgui.elements.UIButton(
            relative_rect=pg.Rect((350, 250), (100, 50)),
            text='Load Map',
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = True  # Se crea invisible al principio
        )
        self.terrain = None

        #self.recreate_ui()
        #self.hello_button = None
        #self.load_map = None
        #self.load_maze = None
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

        """self.load_maze = pgui.elements.UIButton(
            relative_rect = pg.Rect((130, 15), (100, 50)),
            text = 'Load Maze',
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = True  # Se crea invisible al principio
        )"""

        self.type_terrain = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 60), (100, 20)),
            text = 'Type Terrain',
            manager = self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )

        self.test_drop_down = pgui.elements.UIDropDownMenu(
            ['Bosque', 'Agua', 'Tierra', 'Montaña', 'Arena', 'Pantano', 'Nieve'],
            'Bosque',
            pg.Rect((15, 85), (150, 50)),
            self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )

        self.maze_drop_down = pgui.elements.UIDropDownMenu(
            ['Wall','Road'],
            'Road',
            pg.Rect((15, 85), (150, 50)),
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

    def abrir_explorador_archivos(self):
        # Crear una instancia de Tkinter y ocultar la ventana
        root = tk.Tk()
        root.withdraw()

        # Abrir el explorador de archivos y obtener el archivo seleccionado
        file = filedialog.askopenfilename(
            filetypes=[("Archivos de Texto", "*.txt")],  # Filtrar solo archivos .txt
            title="Selecciona un archivo de texto"
        )

        if file:  # Si se selecciona un archivo
            print(f"Archivo seleccionado: {file}")
            return file
        else:
            print("No se seleccionó ningún archivo")
            return None

    def update_ui(self, cell_pos, terrain):
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
        if terrain.matriz[cell_pos[0]][cell_pos[1]] <= 7: 
            current_value = terrain.current_value(cell_pos[0], cell_pos[1])
            self.test_drop_down = pgui.elements.UIDropDownMenu(
                ['Bosque', 'Agua', 'Tierra', 'Montaña', 'Arena', 'Pantano', 'Nieve'],
                current_value,
                pg.Rect((15, 85), (150, 50)),
                self.ui_manager,
                container = self.side_panel_top
            )
        else:
            current_value = terrain.current_value(cell_pos[0], cell_pos[1])
            self.test_drop_down = pgui.elements.UIDropDownMenu(
                ['Wall', 'Road'],
                current_value,
                pg.Rect((15, 85), (150, 50)),
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

    def process_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False

            self.ui_manager.process_events(event)

            #IF BUTTON PRESSED
            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == self.load_map:
                    print('Haz presionado Load Map')
                    archivo = self.abrir_explorador_archivos()
                    self.terrain = Terrain(archivo)
                #if event.ui_element == self.load_maze:
                    #print('Haz presionado Load Maze')

            if self.terrain:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Clic izquierdo
                    mouse_pos = event.pos
                    cell_x = (mouse_pos[0] - 32) // c.TILE_SIZE
                    cell_y = (mouse_pos[1] -32) // c.TILE_SIZE

                    if mouse_pos[0] >= 32 and mouse_pos[1] >= 32 and 0 <= cell_x < self.terrain.tam_col and 0 <= cell_y < self.terrain.tam_fila:
                        self.selected_cell = (cell_y, cell_x)
                        print(f"Celda seleccionada: ({cell_y}, {cell_x})")
                        # Mostrar botones cuando una celda es seleccionada
                        self.update_ui(self.selected_cell, self.terrain)
            
                #IF DROP DOWN MENU
                if (event.type == pgui.UI_DROP_DOWN_MENU_CHANGED and event.ui_element == self.test_drop_down):
                    if self.terrain.matriz[self.selected_cell[0]][self.selected_cell[1]] <= 7:
                        Bio = {
                            "Bosque": 1,    # Verde - Bosque
                            "Agua": 2,    # Azul - Agua
                            "Tierra": 3,    # Cafe - Tierra
                            "Montaña": 4,  # Marron Oscuro - Montana
                            "Arena": 5,  # Amarillo - Arena
                            "Pantano": 6,   # Verde Agua - Pantano
                            "Nieve": 7 # Blanco - Nieve
                        }
                        new_option = event.text
                        new_value = Bio.get(new_option)
                        print(new_value, self.selected_cell[0], self.selected_cell[1])
                        if self.selected_cell:
                            self.terrain.change_value(self.selected_cell[0], self.selected_cell[1], new_value, self.screen)

                        self.update_ui(self.selected_cell, self.terrain)
                    else:
                        Bio = {
                            "Wall": 8,    # Verde - Wall
                            "Road": 9    # Azul - Road
                        }
                        new_option = event.text
                        new_value = Bio.get(new_option)
                        print(new_value, self.selected_cell[0], self.selected_cell[1])
                        if self.selected_cell:
                            self.terrain.change_value(self.selected_cell[0], self.selected_cell[1], new_value, self.screen)

                        self.update_ui(self.selected_cell, self.terrain)
                
    def run(self):
        while self.running:
            self.time_delta = self.clock.tick(c.FPS)

            # Limpiar la pantalla antes de dibujar
            self.screen.fill((0, 0, 0))
            # Dibujar Terrain
            if self.terrain:
                self.terrain.draw_grid(self.screen)
                self.terrain.draw_matriz(self.screen)
            # Check for inputs
                # Respond to input
            self.ui_manager.update(self.time_delta)
                # Dibujar la UI
            self.ui_manager.draw_ui(self.screen)
            
            pg.display.update()
            
            self.process_events()

        pg.quit()

########################################    M A I N
if __name__ == '__main__':
    app = App()
    app.run()