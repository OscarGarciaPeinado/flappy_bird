import pygame

from config import HEIGHT
from entities.panel import Panel


class ScorePanel(Panel):
    bg_color = (102, 153, 153)
    bird_slot_height = HEIGHT / 10.0
    line_color = (104, 104, 104)
    font_size = 15

    def __init__(self, screen, x, width, birds):
        self.screen = screen
        self.bg_x = x
        self.bg_width = width
        self.birds = birds
        self.score_text_font = pygame.font.SysFont("monospace", self.font_size)

    def draw_bird_score(self, screen, bird, y):
        text_y = y + (self.bird_slot_height / 2) - self.font_size / 2
        pipes_x = self.bg_x + 0.7 * self.bg_width
        name_x = self.bg_x + 0.2 * self.bg_width
        distance_x = self.bg_x + 0.6 * self.bg_width
        distance = self.score_text_font.render(str(bird.distance), 1, (255, 255, 0))
        pipes = self.score_text_font.render(str(bird.score), 1, (255, 255, 0))
        name = self.score_text_font.render(bird.name, 1, (255, 255, 0))

        pygame.draw.rect(
            self.screen, self.line_color, (self.bg_x, y + self.bird_slot_height, self.bg_width, 4))

        screen.blit(name, (name_x, text_y))
        screen.blit(pipes, (pipes_x, text_y))
        screen.blit(distance, (distance_x, text_y))

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, (self.bg_x, 0, self.bg_width, HEIGHT))
        pygame.draw.rect(self.screen, self.line_color, (self.bg_x, 0, 4, HEIGHT))
        for index, bird in enumerate(self.birds):
            self.draw_bird_score(self.screen, bird, float(index * self.bird_slot_height))
