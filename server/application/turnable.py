import abc

from displayable import Displayable

class Turnable(Displayable):
    """Base class for any object that can change it's rotation on gaming
    field.

    Fields:

    angle is turn angle for this object.

    angular_speed is speed of rotation of object at this moment.

    max_angular_speed is maximum of absolute value of turning speed. Clockwise
    rotation speed equals to counterclockwise rotation speed."""

    def __init__(self, init_angle, init_angular_speed, max_angular_speed):
        self._angle = init_angle
        self._angular_speed = init_angular_speed
        self._max_angular_speed = max_angular_speed

    def turn_on_angle(self):
        """Turns this object on given angle, if direction "forward" can be
        defined."""
        self._angle += self._angular_speed

    def set_angular_speed(self, angular_speed):
        """Sets angular speed with check."""
        if angular_speed > self._max_angular_speed:
            self._angular_speed = self._max_angular_speed
        elif angular_speed < -self._max_angular_speed:
            self._angular_speed = -self._max_angular_speed
        else:
            self._angular_speed = angular_speed

    #   TODO: implement when we define strictly how angle is measured
    def turn_to_face(self, x, y):
        """Turns this object to be positioned to point (x,y)"""
        raise NotImplementedError("Not implemented yet")
