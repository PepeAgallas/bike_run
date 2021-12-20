import sys

import pygame

from entities.entity_manager import EntityManager
from window import Window

FPS = 60


class Game(object):
    is_running: bool = False
    window: Window
    entity_manager: EntityManager
    player = None

    def __init__(self):
        pygame.init()

        self.is_running = True
        self.window = Window()
        self.entity_manager = EntityManager()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

        delta_time = self.window.update(FPS)
        self.entity_manager.update(delta_time, surface=self.window.screen)

    def quit(self):
        self.is_running = False
        pygame.quit()
        sys.exit(0)
