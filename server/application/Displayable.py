import abc


class Displayable:
    """Base class for any object to be displayed on game field"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, object_name):
        self.object_name = object_name

    def get_name(self):
        return self.object_name

    @abc.abstractmethod
    def intersects(self, another_displayable):
        """Returns true if this object intersects with another_displayable."""
        return

    # TODO: choose some particular display object type
    @abc.abstractmethod
    def display(self, display_object):
        """Draws this object on display object (e.g. some drawing panel)
        passed."""
        return

    @abc.abstractmethod
    def get_shape(self):
        """Returns fully described shape of this object."""
        return

    @abc.abstractmethod
    def get_coordinates(self):
        """Returns pair (x, y) of point considered to be center of this
        object."""
        return
