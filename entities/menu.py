from collections import OrderedDict

import pygame

from config import HEIGHT, WIDTH, GAME_WIDTH
from engine.ga_nn_flappy_engine import GaNnFlappyEngine
from engine.manual_flappy_engine import ManualFlappyEngine
from entities.option_menu import OptionMenu
from entities.scorepanel import ScorePanel
from repository.image_loader import ImageLoader
from scenes.play_scene import PlayScene
from utils import root_path


class Menu(pygame.Surface):
    orange = (219, 200, 54)
    white = (255, 255, 255)
    selected = None

    def __init__(self, game, width):
        pygame.Surface.__init__(self, (width, HEIGHT), pygame.SRCALPHA, 32)
        self.game = game
        self.image_loader = ImageLoader()

        self.menu_options = OrderedDict()
        self.arrow_alpha_increment = 1
        self.y = 0
        self.arrow = self.image_loader.get_image("arrow.png").convert_alpha()

        self.add_menu_option("Manual", lambda: self.game.change_scene(
            PlayScene(self.game, ManualFlappyEngine(), None)))

        ga_nn_flappy_engine = GaNnFlappyEngine()
        self.add_menu_option("Bot", lambda: self.game.change_scene(
            PlayScene(self.game, GaNnFlappyEngine(),
                      ScorePanel(self.game.screen, GAME_WIDTH,
                                 WIDTH - GAME_WIDTH,
                                 ga_nn_flappy_engine.get_birds()))))

        self.set_header((width / 2))

        self.selected = "Manual"

    def render_header(self):
        self.blit(self.header, self.header_rect)

    def render_arrow(self):
        selected_option = self.menu_options[self.selected][0]
        y = (selected_option.y + (self.arrow.get_height() / 2))
        x = (selected_option.x - self.arrow.get_width() - 15)
        self.blit(self.arrow, (x, y),
                  (0, 0, self.arrow.get_width(), self.arrow.get_height()))

    def render_menu_options(self):
        for text, tuple_value in self.menu_options.items():
            option_menu = tuple_value[0]
            self.blit(option_menu, (option_menu.x, option_menu.y))

    def get_next_menu_option_y(self):
        if len(self.menu_options):
            last_item = next(reversed(self.menu_options.values()))[0]
            return last_item.y + last_item.get_height()
        else:
            return HEIGHT / 3

    def add_menu_option(self, text, callback):
        option_menu = OptionMenu(text, x=(WIDTH / 2),
                                 y=self.get_next_menu_option_y())
        self.menu_options[text] = (option_menu, callback)

    def set_header(self, center_x):
        font = pygame.font.Font(root_path + '/assets/flappy_bird_font.ttf', 90)
        self.header, self.header_rect = self.text_objects("Flappy Bird 0 ML",
                                                          font,
                                                          self.orange)
        self.header_rect.center = (center_x, (HEIGHT / 5))

    @staticmethod
    def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def refresh(self):
        self.fill(pygame.Color(0, 0, 0, 0))
        self.render_header()
        self.render_menu_options()
        self.render_arrow()

    def on_press_return(self):
        self.menu_options[self.selected][1]()

    def on_press_up(self):
        keys = list(self.menu_options.keys())

        selected_index = keys.index(self.selected)
        if selected_index > 0:
            self.selected = keys[selected_index - 1]

    def on_press_down(self):
        keys = list(self.menu_options.keys())

        selected_index = keys.index(self.selected)
        if selected_index < len(keys) - 1:
            self.selected = keys[selected_index + 1]
