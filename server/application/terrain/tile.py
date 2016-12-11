import pygame

from displayable import Displayable


class Tile(Displayable):
    """
    Base class for terrain tiles.
    rect is rectangle containing coordinates of tile.
    color is color with which the tile will be drawn.
    """

    def __init__(self, rect, color, name):
        Displayable.__init__(self, name)
        self.rect = rect
        self.color = color

    def display(self, display_object):
        """
        Method displays this water tile.
        :param display_object: is pygame.Surface object representing display to
        draw on.
        """
        pygame.draw.rect(display_object, self.color, self.rect)

    def get_shape(self):
        """
        :return: pygame.Rect object with coordinates of this water tile.
        """
        return self.rect

