from constants import LAVA_COLOR
from tile import Tile


class LavaTile(Tile):
    """
    Class represents lava tile. Tanks that move on it are destroyed.
    """

    def __init__(self, rect):
        Tile.__init__(self, rect, LAVA_COLOR)
