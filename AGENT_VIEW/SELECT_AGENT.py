import pygame
import pygame_gui
from pygame_gui.core import ObjectID
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
TITLE_HEIGHT = 132
IMAGE_WIDTH = SCREEN_WIDTH // 4
IMAGE_HEIGHT = IMAGE_WIDTH
PADDING_IMG = 1
BUTTON_WIDTH = 150
BUTTON_HEIGHT = TITLE_HEIGHT // 2
pygame.init()
pygame.display.set_caption('Agent Menu')

clock = pygame.time.Clock()



class View:
    def __init__(self, window_surface, manager):
        self.window_surface = window_surface
        self.manager = manager

    def process_events(self, event):
        pass

    def update(self, time_delta):
        pass

    def draw(self):
        pass
class SeleccionarAgente(View):  # Hereda de la clase View
    def __init__(self, window_surface, manager):
        print("Nueva vista de selección de agente")
        self.running = True
        self.window_surface = window_surface
        background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background.fill(pygame.Color('#000000'))
        super().__init__(window_surface, manager)
        self.agent=None
        self.setup_ui()
    def setup_ui(self):
        self.panel_header_rect = pygame.Rect(0, 0, SCREEN_WIDTH, TITLE_HEIGHT)
        self.panel_header = pygame_gui.elements.UIPanel(relative_rect=self.panel_header_rect,
                                                manager=self.manager,
                                                object_id=ObjectID(class_id='@panel_header'))
        # button_back_rect = pygame.Rect(20, TITLE_HEIGHT // 4, BUTTON_WIDTH, BUTTON_HEIGHT)
        # button_advance_rect = pygame.Rect(SCREEN_WIDTH - BUTTON_WIDTH - 20, TITLE_HEIGHT // 4, BUTTON_WIDTH, BUTTON_HEIGHT)
        # self.button_back = pygame_gui.elements.UIButton(relative_rect=button_back_rect,
        #                                         text="Regresar",
        #                                         manager=self.manager,
        #                                         container=panel_header,
        #                                         object_id=ObjectID(class_id='@buttons_navegation'))
        # self.button_advance = pygame_gui.elements.UIButton(relative_rect=button_advance_rect,
        #                                             text="Avanzar",
        #                                             manager=self.manager,
        #                                             container=panel_header,
        #                                             object_id=ObjectID(class_id='@buttons_navegation'))
        label_title_rect = pygame.Rect(SCREEN_WIDTH // 4, TITLE_HEIGHT // 4, SCREEN_WIDTH // 2, TITLE_HEIGHT // 2)
        self.label_title_map = pygame_gui.elements.UILabel(relative_rect=label_title_rect,
                                                    text='SELECCIONAR AGENTE',
                                                    manager=self.manager,
                                                    container=self.panel_header,
                                                    object_id=ObjectID(class_id='@title', object_id='#title_map_modified'))
        self.menu_container_img = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(100, TITLE_HEIGHT, SCREEN_WIDTH - PADDING_IMG, SCREEN_HEIGHT - TITLE_HEIGHT),
            manager=self.manager,
            object_id=ObjectID(class_id='@menu_container_img'))
        self.human_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(PADDING_IMG, PADDING_IMG, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#human_button')
        )
        self.human_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(PADDING_IMG, IMAGE_HEIGHT, IMAGE_WIDTH - PADDING_IMG, BUTTON_HEIGHT // 2),
            text='Humano',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@agent_label')
        )
        self.monkey_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SCREEN_WIDTH // 2, PADDING_IMG, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#monkey_button')
        )
        self.monkey_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(SCREEN_WIDTH // 2, IMAGE_HEIGHT, IMAGE_WIDTH - PADDING_IMG, BUTTON_HEIGHT // 2),
            text='Mono',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@agent_label')
        )
        self.octopus_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(PADDING_IMG, (SCREEN_HEIGHT - TITLE_HEIGHT) // 2,
                                    IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#octopus_button')
        )
        self.octopus_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(PADDING_IMG, (SCREEN_HEIGHT - TITLE_HEIGHT) // 2 + IMAGE_HEIGHT,
                                    IMAGE_WIDTH - PADDING_IMG, BUTTON_HEIGHT // 2),
            text='Pulpo',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@agent_label')
        )
        self.sasquatch_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SCREEN_WIDTH // 2, (SCREEN_HEIGHT - TITLE_HEIGHT) // 2,
                                    IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#sasquatch_button')
        )
        self.sasquatch_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(SCREEN_WIDTH // 2, (SCREEN_HEIGHT - TITLE_HEIGHT) // 2 + IMAGE_HEIGHT,
                                    IMAGE_WIDTH - PADDING_IMG, BUTTON_HEIGHT // 2),
            text='Sasquatch',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@agent_label')
        )
    def process_events(self, event):
        advance=False
        back=False
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            # if event.ui_element ==self.button_advance:
            #     print('Avanzar')
            # elif event.ui_element ==self.button_back:
            #     print('Retroceder')
            #     back=True
            if event.ui_element == self.human_button:
                print('Humano seleccionado')
                self.agent="Human"
                advance=True
            elif event.ui_element == self.monkey_button:
                print('Mono seleccionado')
                self.agent="Monkey"
                advance=True
            elif event.ui_element == self.octopus_button:
                print('Pulpo seleccionado')
                self.agent="Octopus"
                advance=True
            elif event.ui_element == self.sasquatch_button:
                print('Sasquatch seleccionado')
                self.agent="Sasquatch"
                advance=True
        if advance==True:
            return self.agent
     
    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self):
        self.window_surface.fill(pygame.Color('#000000'))
        self.manager.draw_ui(self.window_surface)
        pygame.display.update()
    def get_agent(self):
        if self.agent is not None:
            self.clear_ui()
            return self.agent
    def clear_ui(self):

        
    # Opción 1: Resetear el texto de los botones y labels
        # self.human_button.set_text('')
        # self.monkey_button.set_text('')
        # self.octopus_button.set_text('')
        # self.sasquatch_button.set_text('')


        # Opción 2: Eliminar completamente los botones y labels
        self.human_button.kill()
        self.monkey_button.kill()
        self.octopus_button.kill()
        self.sasquatch_button.kill()
        # self.button_back.kill()
        # self.button_advance.kill()

        self.human_label.kill()
        self.monkey_label.kill()
        self.octopus_label.kill()
        self.sasquatch_label.kill()
        self.label_title_map.kill()

        self.menu_container_img.kill()
        self.panel_header.kill()