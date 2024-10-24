import pygame

# Inicialización de Pygame
pygame.init()
window_size = (600, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Máscara con pygame.Mask")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Crear una superficie con un círculo
#surface = pygame.Surface(window_size)
#surface.fill(WHITE)
pygame.draw.circle(window, BLUE, (300, 200), 150)

# Crear una máscara del mismo tamaño que la superficie
mask = pygame.Mask(window_size)

# Definir qué píxeles de la máscara son visibles (valor 1 en la máscara)
for y in range(100, 300):  # Esto crea un cuadrado de 200x200 visible
    for x in range(100, 300):
        mask.set_at((x, y), 1)  # Hacer visible esta área en la máscara

# Crear una superficie en blanco para aplicar la máscara
masked_surface = pygame.Surface(window_size, pygame.SRCALPHA)

# Copiar los píxeles visibles de la superficie original a la máscara
for y in range(window_size[1]):
    for x in range(window_size[0]):
        if mask.get_at((x, y)):  # Si el píxel está visible en la máscara
            masked_surface.set_at((x, y), window.get_at((x, y)))

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    window.fill(BLACK)

    # Dibujar solo la parte visible de la superficie usando la máscara
    window.blit(masked_surface, (0, 0))

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
