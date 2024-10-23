#   Modulos usados: tkinter, pygame, pygame_gui, constants, terrain
import tkinter as tk
from tkinter import filedialog
import constants as c
import pygame as pg
from pygame.locals import *
import pygame_gui as pgui
from .TERRAIN_class import Terrain
from .MASK_class import Mask_Map
from .AGENT_class import *
from AGENT_VIEW.SELECT_AGENT import SeleccionarAgente

class App:
    initial = True
    selected_cell = None
    archivo = None
    obj_mask = True
    datos_iniciales = True
    offset_x = 0  # Desplazamiento en el eje X
    offset_y = 0  # Desplazamiento en el eje Y
    x_initial = None
    y_initial = None
    
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
        self.ui_manager.get_theme().load_theme("AGENT_VIEW/Styles.json")
        self.ui_manager.get_theme().load_theme('AGENT_VIEW/buttonAgents.json')
        self.ui_manager.get_theme().load_theme('front/Sensores/buttonSensores.json')
        self.ui_manager.get_theme().load_theme('front/Sensores/StylesSensors.json')
        self.ui_manager.agent = None
        self.terrain = None
        self.mascara = None

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
        self.side_panel_layout_rect = pg.Rect(0, 0, c.SIDE_PANEL, c.SCREEN_HEIGHT//4)
        self.side_panel_layout_rect.bottomright = (screen_width, screen_height)
        self.side_panel_bottom = pgui.elements.UIPanel(
            relative_rect = self.side_panel_layout_rect,  # Panel lateral en el lado derecho
            starting_height = 1,
            manager = self.ui_manager
        )
            #3
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        self.side_panel_layout_rect.bottomright = (screen_width, screen_height*(3/4))
        self.side_panel_midle = pgui.elements.UIPanel(
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

        #self.recreate_ui()

        """ Definicion de los botones """
        #self.hello_button = None
        self.type_terrain = None
        self.test_drop_down = None
        self.coordinates_cell_y = None
        self.coordinates_cell_x = None
        self.current_position = None
        #self.save_map = None
        #self.clear_map = None
        self.save_copy_map = None
        self.text_entry_line_1 = None
        self.text_entry_line_2 = None
        #Entrada de la posicion inicial y final
        self.text_entry_line_3 = None
        self.text_entry_line_4 = None
        self.text_entry_line_5 = None
        self.text_entry_line_6 = None
        self.state="menu"
        self.agent_type=None
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
            #SAVE AS A COPY MAP BUTTON
        self.save_copy_map = pgui.elements.UIButton(
            relative_rect = pg.Rect((130, 15), (100, 50)),
            text = 'Save As...',
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = True  # Se crea invisible al principio
        )
        self.load_agent= pgui.elements.UIButton(
            relative_rect=pg.Rect((15,115, ), (100, 50)),
            text='Seleccionar Agente',
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
            #INITIAL POSITION LABEL
        self.initial_position = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 15), (120, 20)),
            text = 'Posición Inicial',
            manager = self.ui_manager,
            container = self.side_panel_midle,
            visible = False  # Se crea invisible al principio
        )
            #FINAL POSITION LABEL
        self.final_position = pgui.elements.UILabel(
            relative_rect = pg.Rect((15, 75), (120, 20)),
            text = 'Posición Final',
            manager = self.ui_manager,
            container = self.side_panel_midle,
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
            # TEXT ENTRY 3
        self.text_entry_line_3 = pgui.elements.UITextEntryLine(
            pg.Rect((15, 80), (100, 30)),
            self.ui_manager,
            container = self.side_panel_bottom,
            visible = False,
            initial_text = 'A - Z'
        )
        self.text_entry_line_3.set_allowed_characters('letters')
        self.text_entry_line_3.set_text_length_limit(1)
            # TEXT ENTRY 4
        self.text_entry_line_4 = pgui.elements.UITextEntryLine(
            relative_rect = pg.Rect((130, 80), (100, 30)),
            manager = self.ui_manager,
            container = self.side_panel_bottom,
            visible = False,
            initial_text = '0'
        )
        self.text_entry_line_4.set_allowed_characters('numbers')
        #self.text_entry_line_2.set_text_length_limit()
            # TEXT ENTRY 5
        self.text_entry_line_5 = pgui.elements.UITextEntryLine(
            pg.Rect((55, 35), (40, 30)),
            self.ui_manager,
            container = self.side_panel_midle,
            visible = False,
            initial_text = '1a'
        )
        self.text_entry_line_5.set_allowed_characters('alpha_numeric')
        self.text_entry_line_5.set_text_length_limit(3)
            # TEXT ENTRY 6
        self.text_entry_line_6 = pgui.elements.UITextEntryLine(
            relative_rect = pg.Rect((55, 100), (40, 30)),
            manager = self.ui_manager,
            container = self.side_panel_midle,
            visible = False,
            initial_text = '1b'
        )
        self.text_entry_line_6.set_allowed_characters('alpha_numeric')
        self.text_entry_line_6.set_text_length_limit(3)

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

    def gestionar_teclas(self, event):
    # Verificar que el evento sea de tipo KEYDOWN
        if event.type == pg.KEYDOWN and (not self.text_entry_line_5.is_focused and not self.text_entry_line_6.is_focused):
            if event.key == pg.K_a and (self.agent.x > 0):
                #print(self.agent.x)
                self.agent.x -= 1  # Mover hacia la izquierda
                self.agent.actualizar_costo(self.terrain)
            elif event.key == pg.K_d and (self.agent.x < self.terrain.tam_col - 1):
                #print(self.agent.x)
                self.agent.x += 1  # Mover hacia la derecha
                self.agent.actualizar_costo(self.terrain)
            elif event.key == pg.K_s and (self.agent.y < self.terrain.tam_fila - 1):
                #print(self.agent.y)
                self.agent.y += 1  # Mover hacia abajo
                self.agent.actualizar_costo(self.terrain)
            elif event.key == pg.K_w and (self.agent.y > 0):
                #print(self.agent.y)
                self.agent.y -= 1  # Mover hacia arriba
                self.agent.actualizar_costo(self.terrain)


    #Funcion para definir el inicio, final, y agente a seleccionar
    def initial_screen(self):
        if self.terrain:
            self.initial_position.show()
            self.final_position.show()
            self.text_entry_line_5.show()
            self.text_entry_line_6.show()
            self.process_events()
            if self.terrain.initial_point is not None and self.terrain.end_point is not None and self.agent_type is not None:
                if self.agent_type=="Human":
                    self.agent = Agent_Human(self.x_initial, self.y_initial)
                elif self.agent_type=="Monkey":
                    self.agent = Agent_Monkey(self.x_initial, self.y_initial)
                elif self.agent_type=="Octopus":
                    self.agent = Agent_Octopus(self.x_initial, self.y_initial)
                elif self.agent_type=="Sasquatch":
                    self.agent = Agent_Sasquatch(self.x_initial, self.y_initial)
                self.initial = False
                print("INITIAL ES F A L S O")
            #self.process_events()
            #Display Mapa
            #Indicar Inicio
            #Indicar Final
            #Seleccionar Agente
            #Indicar Prioridad para Busqueda No Informada Profundidad
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
        
            #self.text_entry_line_6.set_text(str(cell_pos[0] + 1))
        
        self.text_entry_line_1.set_text(terrain.convert_coordinate_to_letter(cell_pos[1]))
        self.text_entry_line_2.set_text(str(cell_pos[0]+1))
        
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
            
            #key = pg.key.get_pressed()
            self.gestionar_teclas(event)

            if (not self.text_entry_line_5.is_focused and not self.text_entry_line_6.is_focused and not self.text_entry_line_1.is_focused and not self.text_entry_line_2.is_focused) and event.type == KEYDOWN:
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
                if event.ui_element==self.load_agent:
                    self.current_view=None
                    self.current_view=SeleccionarAgente(self.screen,self.ui_manager)
                    self.state="agent"
            if self.state=="agent" :
                    self.current_view.process_events(event)
                    self.agent_type=self.current_view.get_agent()
                    #print(self.agent_type)
                    if self.agent_type is not None:
                        print(self.agent_type)
                        self.state="menu"
                        self.current_view=None
                        self.current_view=self.screen
                    
            #Seleccionar inicio y fin
            """if self.terrain:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    print("Selecciona tu posicion de inicio")
                    mouse_pos = event.pos
                    #Se covierte a un numero entero para conocer la celda sobre la que se hizo click
                    cell_x = (mouse_pos[0] - c.TILE_SIZE - self.offset_x) // c.TILE_SIZE
                    cell_y = (mouse_pos[1] - c.TILE_SIZE - self.offset_y) // c.TILE_SIZE
                    if 0 <= cell_x < self.terrain.tam_col and 0 <= cell_y < self.terrain.tam_fila:
                        #self.mascara.unmask(cell_x, cell_y, self.mascara, self.screen, self.terrain)
                        self.selected_cell = (cell_y, cell_x)
                        print(f"Celda seleccionada: ({cell_y}, {cell_x})")"""
            #Si existe un objeto Terrain se ejecuta este bloque de codigo
            if self.initial == False:
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
            
            else:
                if event.type == pg.USEREVENT and event.user_type == pgui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == self.text_entry_line_5:
                        string_5 = self.text_entry_line_5.get_text()
                        letter = string_5[-1].upper()
                        self.y_initial = self.terrain.convert_letter_to_coordinate(letter)
                        self.x_initial = int(string_5[0:-1])-1
                        self.selected_cell = [self.x_initial, self.y_initial]
                        self.terrain.asignar_celda_inicial(self.x_initial, self.y_initial)
                        #self.update_ui(self.selected_cell, self.terrain)
                        self.text_entry_line_5.set_text(str(self.terrain.initial_point[0]+1) + self.terrain.convert_coordinate_to_letter(self.terrain.initial_point[1]))
                        self.text_entry_line_5.redraw()
                        self.text_entry_line_5.disable()
                    
                    if event.ui_element == self.text_entry_line_6:
                        string_5 = self.text_entry_line_6.get_text()
                        letter = string_5[-1].upper()
                        y_initial = self.terrain.convert_letter_to_coordinate(letter)
                        x_initial = int(string_5[0:-1])-1
                        #final_cell = [x_initial, y_initial]
                        self.terrain.asignar_celda_final(x_initial, y_initial)
                        self.text_entry_line_6.set_text(str(self.terrain.end_point[0]+1) + self.terrain.convert_coordinate_to_letter(self.terrain.end_point[1]))
                        #self.update_ui(final_cell, self.terrain)
                        self.text_entry_line_6.redraw()
                        self.text_entry_line_6.disable()

    

                
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
                if self.initial == False: 
                    self.agent.draw_human(self.screen, self.offset_x, self.offset_y)
                    self.terrain.draw_i(self.screen, self.offset_x, self.offset_y)
                    self.terrain.draw_f(self.screen, self.offset_x, self.offset_y)
                    self.terrain.draw_v(self.screen, self.offset_x, self.offset_y)
                    self.terrain.draw_o(self.screen, self.offset_x, self.offset_y)

                self.terrain.draw_grid(self.screen, self.offset_x, self.offset_y)
                
                if self.initial == True:
                    self.initial_screen()
                
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