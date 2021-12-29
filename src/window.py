import pygame.display
from pygame import Surface
from pygame.time import Clock

WIDTH, HEIGHT = 480, 720
CENTER_WIDTH, CENTER_HEIGHT = WIDTH/2, HEIGHT/2


class Window(object):
    screen: Surface
    clock: Clock

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = Clock()

    def update(self, fps) -> float:
        ticks = self.clock.tick(fps)
        pygame.display.flip()
        self.screen.fill(pygame.Color('black'))

        return ticks * 0.001
