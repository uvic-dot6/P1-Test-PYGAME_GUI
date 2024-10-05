SIDE_PANEL = 300
TILE_SIZE = 32
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
FPS = 30
WHITE = (255, 255, 255)
BLUE = (42, 106, 233)
BROWN = (191, 103, 63)
BROWN_BORDER = (172, 137, 120)
"""def recreate_ui(self, cell_pos):
        
        if self.hello_button is None and self.test_drop_down is None:
            
            self.hello_button = pgui.elements.UIButton(
                relative_rect=pg.Rect((self.screen_width + 20, 20), (100, 50)),
                text='Say Hello',
                manager=self.ui_manager)

            self.test_drop_down = pgui.elements.UIDropDownMenu(
                ['1', '2', '3', '4', '5', '6', '7'],
                str(tablero.current_value(cell_pos[0], cell_pos[1])),
                pg.Rect((self.screen_width + 20, 80), (100, 50)),
                self.ui_manager)

        else:

            self.hello_button = pgui.elements.UIButton(
                relative_rect=pg.Rect((self.screen_width + 50, 20), (100, 50)),
                text='Say Hello',
                manager=self.ui_manager)
            
            self.test_drop_down = pgui.elements.UIDropDownMenu(
                ['1', '2', '3', '4', '5', '6', '7'],
                str(tablero.current_value(cell_pos[0], cell_pos[1])),
                pg.Rect((self.screen_width + 50, 80), (100, 50)),
                self.ui_manager)"""