import pygame
from pygame.surface import Surface

from src.window import WIDTH, HEIGHT

LANES = 3
STRIPE_WIDTH = 10
BORDER_WIDTH = 20
STRIPE_COLOR = (200, 200, 0, 0.7)
BORDER_COLOR = (255, 255, 255, 1)


class Road(object):
    borders: int

    def __init__(self):
        self.borders = 2

    def loop(self, surface: Surface):
        self.draw_boundaries(surface)

    def draw_boundaries(self, surface: Surface):
        def get_positionx(num):
            # distance from borders is not equal or regular
            return abs(BORDER_WIDTH - (WIDTH * num))

        for border_number in range(0, self.borders):
            pygame.draw.line(
                surface,
                BORDER_COLOR,
                (get_positionx(border_number), 0),
                (get_positionx(border_number), HEIGHT),
                BORDER_WIDTH,
            )
