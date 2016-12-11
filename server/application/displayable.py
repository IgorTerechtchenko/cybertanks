class Displayable(object):
    """
    Base class for any object to be displayed on game field.
    object_name

    get_name(self)
    display(self, another_displayable)
    get_shape(self)
    get_coordinates(self)
    """

    def __init__(self, object_name):
        self.object_name = object_name

    def get_name(self):
        return self.object_name

    # TODO: choose some particular display object type
    def display(self, display_object):
        """
        Draws this object on display object (e.g. some
        drawing panel passed.)
        """
        return

    def get_shape(self):
        """Returns fully described shape of this object."""
        return

    def get_coordinates(self):
        """
        Returns tuple (x, y) containing coordinates of point
        considered to be center of this object.
        """
        return
