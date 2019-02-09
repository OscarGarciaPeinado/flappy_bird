import pygame

from config import HEIGHT, GAME_WIDTH
from repository.image_loader import ImageLoader


class Bird(pygame.sprite.Sprite):
    sprite_index = 0

    GRAVITY_ACC = 1

    y_vel = -6
    max_y_vel = 10
    jump_acc = -10

    jumping = False
    dead = False
    sprite_rate_index = 0

    score = 0
    distance = 0

    def __init__(self, name=None, y=HEIGHT / 2):
        pygame.sprite.Sprite.__init__(self)

        mid_flap = ImageLoader().get_image("redbird-midflap.png")
        up_flap = ImageLoader().get_image("redbird-upflap.png")
        down_flap = ImageLoader().get_image("redbird-downflap.png")

        self.flap_sprites = [mid_flap, down_flap, mid_flap, up_flap]

        self.image = mid_flap

        self.rect = self.image.get_rect()
        self.rect.center = (GAME_WIDTH / 2, y)
        self.name = name

    def change_flap_sprite(self):
        self.sprite_rate_index += 1
        if self.sprite_rate_index % 5 == 0:
            self.sprite_index += 1
            self.image = self.flap_sprites[self.sprite_index % len(self.flap_sprites)]

    def refresh(self):
        self.change_flap_sprite()

        if self.y_vel < self.max_y_vel and not self.jumping:
            self.y_vel += self.GRAVITY_ACC
        if self.jumping:
            self.jumping = False

        self.rect.y += self.y_vel

    def jump(self):
        self.jumping = True
        self.y_vel = self.jump_acc
