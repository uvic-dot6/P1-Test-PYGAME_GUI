##################################################### C O N S T A N T S

SIDE_PANEL = 300
TILE_SIZE = 32
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
FPS = 30

##################################################### C O N S T A N T S     C O L O R S

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (19, 67, 99)
BLUE_BORDER = (163, 209, 255)
BROWN = (191, 103, 63)
BLACK_MASK= (50,50,50)

##################################################### C O N S T A N T S     C O L O R S     B I O M E S

#BOSQUE = (39, 237, 90)
BOSQUE = (43, 218, 88)
AGUA = (38, 54, 255)
TIERRA = (218, 123, 40)
MONTANA = (73, 57, 48)
ARENA = (255, 222, 99)
PANTANO = (15, 128, 88)
NIEVE = (220, 220, 220)
BORDER_GRID = (81, 81, 81)

##################################################### S T R U C T S
    
    # Diccionario de colores
COLORES = {
        1: BOSQUE,    # Verde - Bosque
        2: AGUA,    # Azul - Agua
        3: TIERRA,    # Cafe - Tierra
        4: MONTANA,  # Marron Oscuro - Montana
        5: ARENA,  # Amarillo - Arena
        6: PANTANO,   # Verde Agua - Pantano
        7: NIEVE, # Blanco - Nieve
        8: BLACK, #Negro - Wall
        9: WHITE #Blanco - Road
    }
    
    #Diccionario de terreno equivalente a su valor entero
TERRAIN_INT = {
    "Bosque": 1,
    "Agua": 2,
    "Tierra": 3,
    "Montaña": 4,
    "Arena": 5,
    "Pantano": 6,
    "Nieve": 7,
    "Wall": 8,
    "Road": 9
}

    #Diccionario de un valor entero equivalente a su tipo de terreno
INT_TERRAIN = {
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