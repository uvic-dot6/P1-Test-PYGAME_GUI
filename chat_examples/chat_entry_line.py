import pygame
import pygame_gui
import string

# Inicialización de Pygame y Pygame GUI
pygame.init()
pygame.display.set_caption("Sistema de Coordenadas con Entrada de Texto")
window_size = (600, 600)
window = pygame.display.set_mode(window_size)

# Crear un administrador de GUI
manager = pygame_gui.UIManager(window_size)

# Crear una entrada de texto (solo un carácter permitido)
input_line = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((200, 550), (200, 30)), manager=manager)
input_line.set_text_length_limit(1)  # Limitar a un solo carácter

# Configuración de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Parámetros de la matriz
num_rows = 26  # De A a Z
num_cols = 10  # Puedes ajustar esto
cell_width = window_size[0] // (num_cols + 1)
cell_height = window_size[1] // (num_rows + 1)

# Función para dibujar la matriz
def draw_grid(surface):
    for row in range(num_rows + 1):
        pygame.draw.line(surface, BLACK, (0, row * cell_height), (window_size[0], row * cell_height))
    for col in range(num_cols + 1):
        pygame.draw.line(surface, BLACK, (col * cell_width, 0), (col * cell_width, window_size[1]))

    # Etiquetar las filas
    for row in range(num_rows):
        label = chr(65 + row)  # A es 65 en ASCII
        font = pygame.font.Font(None, 36)
        text_surface = font.render(label, True, BLACK)
        surface.blit(text_surface, (5, row * cell_height + 5))

    # Etiquetar las columnas
    for col in range(num_cols):
        label = str(col + 1)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(label, True, BLACK)
        surface.blit(text_surface, (col * cell_width + cell_width // 2 - text_surface.get_width() // 2, 5))

# Función para manejar clic en la celda y mostrar coordenadas
def handle_click(mouse_pos):
    col = mouse_pos[0] // cell_width
    row = mouse_pos[1] // cell_height
    if 0 <= col < num_cols and 0 <= row < num_rows:
        print(f"Celda seleccionada: ({chr(65 + row)}, {col + 1})")

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Verificar si se hizo clic en una celda
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            handle_click(mouse_pos)

        # Procesar eventos de pygame_gui
        manager.process_events(event)

        # Procesar la entrada de texto cuando se presiona Enter
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == input_line:
                user_input = event.text
                if user_input.isalpha():  # Verificar si es una letra
                    print(f"Entrada de texto: {user_input.upper()}")
                else:
                    print("Entrada no válida, solo se permiten letras.")

    # Dibujar la ventana
    window.fill(WHITE)
    draw_grid(window)
    manager.update(time_delta)
    manager.draw_ui(window)

    pygame.display.update()

pygame.quit()
