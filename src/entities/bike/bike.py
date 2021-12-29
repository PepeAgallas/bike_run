import os.path

import pygame.image
from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface


class Bike(Sprite):
    rect: Rect
    image: Surface
    speed: int = 100
    life: int = 0

    def __init__(self):
        super().__init__()
        self._load_image()
        self.rect = self.image.get_rect()
        self.life = 3

    def _load_image(self):
        sprite = os.path.join(os.path.dirname(__file__), 'sprite.png')
        image = pygame.image.load(sprite).convert_alpha()
        width, height = image.get_size()

        self.image = pygame.transform.scale(image, (width//6, height//6))

    def update(self, dt, **kwargs) -> None:
        self.move(dt)

    def move(self, dt) -> None:
        keys = pygame.key.get_pressed()

        movement_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        movement_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]

        self.rect.x += round(self.speed * dt * movement_x)
        self.rect.y += round(self.speed * dt * movement_y)

    def die(self) -> None:
        self.life = 0
