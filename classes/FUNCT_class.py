import tkinter as tk
from tkinter import filedialog
import constants as c
import pygame as pg
from pygame.locals import *
import pygame_gui as pgui
from .TERRAIN_class import Terrain

class Functions:
    
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