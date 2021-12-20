import random

from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface


class Obstacle(Sprite):
    rect: Rect
    image: Surface
    speed: int = 5
    is_alive: bool = False

    def __init__(self):
        super().__init__()

    def update(self, dt, **kwargs) -> None:
        self.move(dt)

    def move(self, dt):
        self.rect.y += self.speed * dt

    def spawn(self, lane: int = None):
        if self.is_alive:
            return

        self.is_alive = True
        if lane is None:
            lane = random.choice([1, 2, 3])
        self.rect.center = (lane, 0)

    def kill(self):
        if not self.is_alive:
            return

        self.is_alive = False
        super().kill()
