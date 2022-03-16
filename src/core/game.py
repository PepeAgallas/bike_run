import sys

import pygame

from src.entities.entity_manager import EntityManager
from src.core.road import Road
from src.core.window import Window

FPS = 60


class Game(object):
    is_running: bool = False
    window: Window
    entity_manager: EntityManager
    road: Road
    last_obstacle_time: float = 0

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

        self.road.loop(delta_time, self.window.screen)
        self.entity_manager.process_input(delta_time)
        self.entity_manager.update(delta_time)
        self.entity_manager.render()

        self.add_obstacle()
        self.check_player_collision()

    def quit(self) -> None:
        self.is_running = False
        pygame.quit()
        sys.exit(0)

    def add_obstacle(self):
        last_time = pygame.time.get_ticks()
        if last_time - self.last_obstacle_time >= 1000:
            self.last_obstacle_time = last_time
            self.entity_manager.add_obstacle()

    def check_player_collision(self):
        [player] = self.entity_manager.player
        obstacles = self.entity_manager.obstacles
        
        collition_group = pygame.sprite.spritecollide(
            player,
            obstacles,
            True
        )

        for collided in collition_group:
            collided.kill()

        has_collided = len(collition_group) > 0
        if has_collided and player.alive():
            player.crash()

        if player.alive() is not True:
            print("Game over!")
            self.quit()
