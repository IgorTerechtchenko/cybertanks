from constants import DESTROYABLE_OBSTACLE_COLOR
from constants import DESTROYABLE_OBSTACLE_HP

from tile import Tile


class ObstacleTile(Tile):
    """
    Class represents destroyable obstacle tile. Tanks and bullets can't move
    through it, but this tile can be destroyed.
    """

    def __init__(self, rect):
        Tile.__init__(self, rect, DESTROYABLE_OBSTACLE_COLOR)
        self.hp = DESTROYABLE_OBSTACLE_HP

    def broken(self):
        return self.hp <= 0
