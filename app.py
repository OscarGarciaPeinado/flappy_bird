import pygame
from scenes.game import Game
from scenes.home_scene import HomeScene

if __name__ == "__main__":
    pygame.init()
    game = Game()
    home_scene = HomeScene(game)
    game.change_scene(home_scene)
    game.loop()
