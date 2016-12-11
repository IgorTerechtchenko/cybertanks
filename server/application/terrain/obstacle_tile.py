from constants import OBSTACLE_COLOR
from tile import Tile


class ObstacleTile(Tile):
    """
    Class represents obstacle tile. Tanks and bullets can't move through it.
    """

    def __init__(self, rect):
        Tile.__init__(self, rect, OBSTACLE_COLOR, "Obstacle tile")
