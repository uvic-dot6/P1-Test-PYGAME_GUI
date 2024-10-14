#   Modulos usados: tkinter, pygame, pygame_gui, constants, terrain
import tkinter as tk
from tkinter import filedialog
import constants as c
import pygame as pg
from pygame.locals import *
import pygame_gui as pgui
from .TERRAIN_class import Terrain
from .MASK_class import Mask_Map

class App:
    selected_cell = None
    archivo = None
    obj_mask = True
    offset_x = 0  # Desplazamiento en el eje X
    offset_y = 0  # Desplazamiento en el eje Y
    
    def __init__(self):
        #Inicio del programa
        pg.init()

        #Nombre del programa mostrado
        pg.display.set_caption("Practica 1")

        #Reloj
        self.clock = pg.time.Clock()

        #Display y UIManager
        self.screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
        self.ui_manager = pgui.UIManager((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))

        #size_map = pg.Rect(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT)

        """ Definicion de los SIDE PANLES usados para la interfaz """
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

        """ Inicializar boton 'Load Map' en la pantalla de inicial """
        self.load_map = pgui.elements.UIButton(
            relative_rect=pg.Rect((350, 250), (100, 50)),
            text='Load Map',
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = True  # Se crea invisible al principio
        )

        
        self.terrain = None
        self.mascara = None

        #self.recreate_ui()

        """ Definicion de los botones """
        #self.hello_button = None
        self.type_terrain = None
        self.test_drop_down = None
        self.coordinates_cell_y = None
        self.coordinates_cell_x = None
        self.current_position = None
        self.save_map = None
        self.clear_map = None
        self.save_copy_map = None
        self.text_entry_line_1 = None
        self.text_entry_line_2 = None
        
        """ Metododo para inicializar los botones """
        self.init_ui()

        self.running = True
    
    def init_ui(self):
         # Inicializacion de los elementos de UI (Botones, Labels) sin mostrarlos al principio
        """
            self.hello_button = pgui.elements.UIButton(
                relative_rect = pg.Rect((c.SCREEN_WIDTH + 20, 20), (100, 50)),
                text = 'Say Hello',
                manager = self.ui_manager,
                visible = False  # Se crea invisible al principio
            )"""
            #LOAD MAP BUTTON
        self.load_map = pgui.elements.UIButton(
            relative_rect = pg.Rect((15, 15), (100, 50)),
            text = 'Load Map',
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = True  # Se crea invisible al principio
        )
            #CLEAR MAP
        self.clear_map = pgui.elements.UIButton(
            relative_rect = pg.Rect((130, 15), (100, 50)),
            text = 'Clear Map',
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = True  # Se crea invisible al principio
        )
            #SAVE MAP BUTTON
        self.save_map = pgui.elements.UIButton(
            relative_rect = pg.Rect((15, 80), (100, 50)),
            text = 'Save',
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = True  # Se crea invisible al principio
        )
            #SAVE AS A COPY MAP BUTTON
        self.save_copy_map = pgui.elements.UIButton(
            relative_rect = pg.Rect((130, 80), (100, 50)),
            text = 'Save As...',
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = True  # Se crea invisible al principio
        )
            #DROP DOWM MENU BUTTON TERRAIN
        self.test_drop_down = pgui.elements.UIDropDownMenu(
            ['Bosque', 'Agua', 'Tierra', 'Montaña', 'Arena', 'Pantano', 'Nieve'],
            'Bosque',
            pg.Rect((15, 85), (150, 50)),
            self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )
            #DROP DOWM MENU BUTTON MAZE
        self.maze_drop_down = pgui.elements.UIDropDownMenu(
            ['Wall','Road'],
            'Road',
            pg.Rect((15, 85), (150, 50)),
            self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )
            #CURRENT POSITION LABEL
        self.current_position = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 15), (120, 20)),
            text = 'Current Position',
            manager = self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )
            #COORDINATES LABEL
        self.coordinates_cell_y = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 35), (30, 20)),
            text = 'Y :',
            manager = self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )
        self.coordinates_cell_x = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 35), (30, 20)),
            text = 'X :',
            manager = self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )
            #TYPE TERRAIN LABEL
        self.type_terrain = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 60), (100, 20)),
            text = 'Type Terrain',
            manager = self.ui_manager,
            container = self.side_panel_top,
            visible = False  # Se crea invisible al principio
        )
            # TEXT ENTRY 1
        self.text_entry_line_1 = pgui.elements.UITextEntryLine(
            pg.Rect((120, 35), (40, 30)),
            self.ui_manager,
            container = self.side_panel_top,
            visible = False,
            initial_text = 'A - Z'
        )
        self.text_entry_line_1.set_allowed_characters('letters')
        self.text_entry_line_1.set_text_length_limit(1)
            # TEXT ENTRY 2
        self.text_entry_line_2 = pgui.elements.UITextEntryLine(
            relative_rect = pg.Rect((55, 35), (40, 30)),
            manager = self.ui_manager,
            container = self.side_panel_top,
            visible = False,
            initial_text = '0'
        )
        self.text_entry_line_2.set_allowed_characters('numbers')
        #self.text_entry_line_2.set_text_length_limit()

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

    def save_as_changes_map(self):
        #root = tk.Tk()
        archivo = filedialog.asksaveasfilename(
        defaultextension = ".txt",
        filetypes = (("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        if archivo:
            with open(archivo, 'w') as file:
                for x in range(self.terrain.tam_fila):
                    for y in range(self.terrain.tam_col):
                        contenido = str(self.terrain.matriz[x][y])
                        file.write(contenido)
                    if x != (self.terrain.tam_fila - 1):
                        file.write('\n')
                    
    def change_coordinate_Y(self, text):
        new_cell_pos = [self.selected_cell[0], self.terrain.convert_letter_to_coordinate(text)]
        self.selected_cell = new_cell_pos
        #print(new_cell_pos[0],new_cell_pos[1])
        self.update_ui(new_cell_pos, self.terrain)

    def change_coordinate_X(self, text):
        new_cell_pos = [int(text) - 1, self.selected_cell[1]]
        self.selected_cell = new_cell_pos
        #print(new_cell_pos[0],new_cell_pos[1])
        self.update_ui(new_cell_pos, self.terrain)
    
    def update_ui(self, cell_pos, terrain):
        # Actualiza la posición de los botones y los valores
            #Posicion relativa a su contenedor
        self.type_terrain.set_relative_position((15, 60))
        self.current_position.set_relative_position((15, 15))
        #self.coordinates_cell.set_relative_position((15, 35))
        
        # Elimina el menú desplegable existente
        if self.test_drop_down is not None:
            self.test_drop_down.kill()

        if self.coordinates_cell_y is not None:
            self.coordinates_cell_y.kill()  
        if self.coordinates_cell_x is not None:
            self.coordinates_cell_x.kill()  

        #Crea un nuevo label con el valor actualizado
        
        #new_coordinate = "X: " + str(cell_pos[0] + 1) + ", Y: " + terrain.convert_coordinate_to_letter(cell_pos[1])
        #str(cell_pos[0])

        self.coordinates_cell_y = pgui.elements.UILabel(
            relative_rect = pg.Rect((95, 40), (30, 20)),
            text = "Y :",
            container = self.side_panel_top,
            manager = self.ui_manager
        )
        self.coordinates_cell_x = pgui.elements.UILabel(
            relative_rect = pg.Rect((30, 40), (30, 20)),
            text = "X :",
            container = self.side_panel_top,
            manager = self.ui_manager
        )

        self.text_entry_line_1.set_text(terrain.convert_coordinate_to_letter(cell_pos[1]))
        self.text_entry_line_2.set_text(str(cell_pos[0] + 1))
        # Crea un nuevo menú desplegable con el valor actualizado de la celda seleccionada
            #Las opciones que sea van a mostrar son del terreno si el valor de la matriz es menor a 7
        print(cell_pos[0], cell_pos[1])
        if terrain.matriz[cell_pos[0]][cell_pos[1]] <= 7: 
            current_value = terrain.current_value(cell_pos[0], cell_pos[1])
            self.test_drop_down = pgui.elements.UIDropDownMenu(
                ['Bosque', 'Agua', 'Tierra', 'Montaña', 'Arena', 'Pantano', 'Nieve'],
                current_value,
                pg.Rect((15, 85), (150, 50)),
                self.ui_manager,
                container = self.side_panel_top
            )
            #En caso que no sea menor a 7 entonces se trata de un laberinto
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
        if not self.test_drop_down.visible:
            self.test_drop_down.show()
        self.type_terrain.show()
        #self.coordinates_cell.show()
        self.current_position.show()
        self.text_entry_line_1.show()
        self.text_entry_line_2.show()

    #PROCESADOR DE EVENTOS
    def process_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False

            self.ui_manager.process_events(event)

            if event.type == KEYDOWN:
                if event.key == K_LEFT and self.offset_x <= -c.TILE_SIZE:
                    #if self.offset_x <= -c.TILE_SIZE:
                        self.offset_x += c.TILE_SIZE
                elif event.key == K_RIGHT and self.offset_x >= -((self.terrain.tam_col-(c.SCREEN_WIDTH//(c.TILE_SIZE)))*c.TILE_SIZE):
                    #if self.offset_x >= -((self.terrain.tam_col-(c.SCREEN_WIDTH//(c.TILE_SIZE)))*c.TILE_SIZE):
                        self.offset_x -= c.TILE_SIZE
                elif event.key == K_UP and self.offset_y <= -c.TILE_SIZE:
                    #if self.offset_y <= -c.TILE_SIZE:
                        self.offset_y += c.TILE_SIZE
                elif event.key == K_DOWN and self.offset_y >= -((self.terrain.tam_fila-(c.SCREEN_HEIGHT//(c.TILE_SIZE)))*c.TILE_SIZE):
                    #if self.offset_y >= -((self.terrain.tam_fila-(c.SCREEN_HEIGHT//(c.TILE_SIZE)))*c.TILE_SIZE):
                        self.offset_y -= c.TILE_SIZE

            #IF BUTTON PRESSED
            if event.type == pgui.UI_BUTTON_PRESSED:
                #Boton de load map presionado
                if event.ui_element == self.load_map:
                    print('Haz presionado Load Map')
                    #Se carga el archivo txt
                    self.archivo = self.abrir_explorador_archivos()
                    #Se crea un objeto del tipo Terrain
                    self.terrain = Terrain(self.archivo)
                if event.ui_element == self.save_copy_map:
                    self.save_as_changes_map()
                    print("Haz presionado salvar como...")

            #Si existe un objeto Terrain se ejecuta este bloque de codigo
            if self.terrain:
                #Se detecta la posicion donde se presiona el click izquierdo del mouse
                if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Clic izquierdo
                    #Se guarda en una tupla los valores
                    mouse_pos = event.pos
                    #Se covierte a un numero entero para conocer la celda sobre la que se hizo click
                    cell_x = (mouse_pos[0] - c.TILE_SIZE - self.offset_x) // c.TILE_SIZE
                    cell_y = (mouse_pos[1] - c.TILE_SIZE - self.offset_y) // c.TILE_SIZE
                    #Se verifica si la posicion corresponde a alguna celda del mapa
                    #if mouse_pos[0] >= 32 and mouse_pos[1] >= 32 and 0 <= cell_x < self.terrain.tam_col and 0 <= cell_y < self.terrain.tam_fila:
                    if 0 <= cell_x < self.terrain.tam_col and 0 <= cell_y < self.terrain.tam_fila:
                        #self.mascara.unmask(cell_x, cell_y, self.mascara, self.screen, self.terrain)
                        self.selected_cell = (cell_y, cell_x)
                        print(f"Celda seleccionada: ({cell_y}, {cell_x})")
                        # Mostrar botones cuando una celda es seleccionada
                        self.update_ui(self.selected_cell, self.terrain)
            
                #IF DROP DOWN MENU
                if (event.type == pgui.UI_DROP_DOWN_MENU_CHANGED and event.ui_element == self.test_drop_down):
                    #Se detecta si se cambia el valor de la celda seleccionada
                        #El valor es guardado como texto
                    new_option = event.text
                        #Se realiza la conversion a su valor entero mediante un diccionario
                    new_value = c.TERRAIN_INT.get(new_option)
                    print(new_value, self.selected_cell[0], self.selected_cell[1])
                        #Se selecciona un celda
                    if self.selected_cell:
                        #Parametros: pos: x, pos: y, nuevo valor entero, display
                        self.terrain.change_value(self.selected_cell[0], self.selected_cell[1], new_value, self.screen)
                    #Se actualiza a la nueva opcion mostrada en el DROP DOWN MENU
                    self.update_ui(self.selected_cell, self.terrain)

                #TEXT ENTRY
                #if (event.type == pgui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#main_text_entry_1'):
                    #print(event.text)
                if event.type == pg.USEREVENT and event.user_type == pgui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == self.text_entry_line_1:
                        self.change_coordinate_Y(self.text_entry_line_1.get_text().upper())
                        self.text_entry_line_1.redraw()
                    if event.ui_element == self.text_entry_line_2:
                        self.change_coordinate_X(self.text_entry_line_2.get_text())
                        self.text_entry_line_2.redraw()

                
    def run(self):
        while self.running:
            #30 FPS
            self.time_delta = self.clock.tick(c.FPS)

            # Limpiar la pantalla antes de dibujar
            self.screen.fill(c.BLACK)

            # Dibujar Terrain
            if self.terrain:
                #self.terrain.draw_grid(self.screen, self.offset_x, self.offset_y)
                self.terrain.draw_matriz(self.screen, self.offset_x, self.offset_y)
                self.terrain.draw_grid(self.screen, self.offset_x, self.offset_y)
                #Crear Mascara
                #if self.obj_mask == True:
                    #self.mascara = Mask_Map(self.terrain, self.screen)
                    #lf.obj_mask = False
                    #print("Se ejecuto 1 vez")
                    #self.screen.blit(self.mascara.masked_surface, (0, 0))
                #self.screen.blit(self.mascara.masked_surface, (0, 0))
            
            # Check for inputs
                # Respond to input
            self.ui_manager.update(self.time_delta)
                # Dibujar la UI
            self.ui_manager.draw_ui(self.screen)
            
            # Actualizacion del display
            pg.display.update()
            
            # Procesador de eventos
            self.process_events()

        pg.quit()