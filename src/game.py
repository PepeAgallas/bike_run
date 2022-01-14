import sys

import pygame

from src.entities.entity_manager import EntityManager
from src.road import Road
from src.window import Window

FPS = 60


class Game(object):
    is_running: bool = False
    window: Window
    entity_manager: EntityManager
    road: Road

    def __init__(self):
        pygame.init()

        self.is_running = True
        self.window = Window()
        self.entity_manager = EntityManager()
        self.road = Road()

    def loop(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

        delta_time = self.window.update(FPS)

        self.road.loop(self.window.screen)
        self.entity_manager.process_input(delta_time)
        self.entity_manager.update(delta_time)
        self.entity_manager.render(surface=self.window.screen)

    def quit(self) -> None:
        self.is_running = False
        pygame.quit()
        sys.exit(0)
