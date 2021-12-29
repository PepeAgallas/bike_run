from pygame.sprite import Group, GroupSingle

from src.entities.bike.bike import Bike
from src.entities.obstacle.obstacle import Obstacle


class EntityManager(object):
    player: GroupSingle
    obstacles: Group
    all_entities: Group

    def __init__(self):
        player = Bike()

        self.player = GroupSingle(player)
        self.obstacles = Group()
        self.all_entities = Group(player)

    def update(self, delta_time, **kwargs):
        self.all_entities.draw(kwargs["surface"])
        self.all_entities.update(delta_time, **kwargs)

    def add_obstacle(self):
        obstacle = Obstacle()

        self.obstacles.add(obstacle)
        self.all_entities.add(obstacle)
