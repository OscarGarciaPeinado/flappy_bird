import pygame

from config import HEIGHT


class Score(object):
    bg_color = (102, 153, 153)
    bird_slot_height = HEIGHT / 10.0

    def __init__(self, x, width, birds):
        self.bg_x = x
        self.bg_width = width
        self.birds = birds
        self.score_text_font = pygame.font.SysFont("monospace", 15)

    def update_bird_score(self, screen, bird, y):
        text_y = y + self.bird_slot_height / 2
        pipes_x = self.bg_x + 0.7 * self.bg_width
        name_x = self.bg_x + 0.2 * self.bg_width
        distance_x = self.bg_x + 0.6 * self.bg_width
        distance = self.score_text_font.render(str(bird.distance), 1, (255, 255, 0))
        pipes = self.score_text_font.render(str(bird.score), 1, (255, 255, 0))
        name = self.score_text_font.render(bird.name, 1, (255, 255, 0))
        screen.blit(name, (name_x, text_y))
        screen.blit(pipes, (pipes_x, text_y))
        screen.blit(distance, (distance_x, text_y))

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, (self.bg_x, 0, self.bg_width, HEIGHT))
        for index, bird in enumerate(self.birds):
            self.update_bird_score(screen, bird, float(index * self.bird_slot_height))
