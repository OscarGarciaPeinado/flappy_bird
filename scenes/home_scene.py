import pygame

from config import WIDTH, MAP_SPEED
from entities.floor import Floor
from entities.menu import Menu
from scenes.scene import Scene


class HomeScene(Scene):

    def __init__(self, game):
        Scene.__init__(self, game)
        self.initialize_bg(game.screen)
        self.initialize_menu()

    def initialize_bg(self, screen):
        self.floor = Floor(MAP_SPEED)
        screen.fill((0, 153, 204))

    def initialize_menu(self):
        self.menu = Menu(self.game, WIDTH)

    def on_update(self, time):
        self.game.screen.fill((0, 153, 204))
        self.floor.refresh()
        self.menu.refresh()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.menu.on_press_return()
            if event.key == pygame.K_UP:
                self.menu.on_press_up()
            if event.key == pygame.K_DOWN:
                self.menu.on_press_down()

    def on_draw(self, screen):
        screen.blit(self.floor.image, self.floor.rect)
        screen.blit(self.menu, self.menu.get_rect())
