import pygame
import pygame_gui

# Inicialización de Pygame y Pygame GUI
pygame.init()
pygame.display.set_caption("Sistema de Coordenadas")
window_size = (600, 600)
window = pygame.display.set_mode(window_size)

# Crear un administrador de GUI
manager = pygame_gui.UIManager(window_size)

# Configuración de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Parámetros de la matriz
num_rows = 26  # De A a Z
num_cols = 10  # Puedes ajustar esto

# Tamaño de cada celda
cell_width = window_size[0] // (num_cols + 1)
cell_height = window_size[1] // (num_rows + 1)

# Función para dibujar la matriz
def draw_grid(surface):
    # Dibujar las filas y columnas
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

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

    window.fill(WHITE)
    draw_grid(window)
    manager.update(time_delta)
    manager.draw_ui(window)

    pygame.display.update()

pygame.quit()
