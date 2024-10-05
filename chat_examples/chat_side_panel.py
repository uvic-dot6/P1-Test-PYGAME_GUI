import pygame as pg
import pygame_gui as pgui

pg.init()

# Dimensiones de la ventana
window_size = (800, 600)
screen = pg.display.set_mode(window_size)
pg.display.set_caption('Ejemplo de UIPanel')

# Crear el UI Manager
ui_manager = pgui.UIManager(window_size)

# Crear un panel lateral
side_panel = pgui.elements.UIPanel(
    relative_rect=pg.Rect((600, 0), (200, 600)),  # Panel lateral en el lado derecho
    starting_height=1,
    manager=ui_manager
)

# Crear botones dentro del panel
button_1 = pgui.elements.UIButton(
    relative_rect=pg.Rect((10, 10), (180, 40)),  # Posición relativa dentro del panel
    text='Botón 1',
    manager=ui_manager,
    container=side_panel  # Asignar el botón al panel
)

button_2 = pgui.elements.UIButton(
    relative_rect=pg.Rect((10, 60), (180, 40)),
    text='Botón 2',
    manager=ui_manager,
    container=side_panel  # Asignar el botón al panel
)

# Bucle principal
running = True
clock = pg.time.Clock()

while running:
    time_delta = clock.tick(60) / 1000.0  # Control de tiempo
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        ui_manager.process_events(event)

    # Actualizar la UI
    ui_manager.update(time_delta)

    # Dibujar la pantalla
    screen.fill((0, 0, 0))  # Limpiar pantalla
    ui_manager.draw_ui(screen)  # Dibujar los elementos UI

    pg.display.update()

pg.quit()
