from displayable import Displayable


class Movable(Displayable):
    """
    Base class for any object that can move on the gaming field.

    speed - linear speed of this object at this moment.
    max_speed - maximal possible speed for this object.
    min_speed - minimal possible speed for this object.
    angle - angle of rotation for speed vector of this object.
    angular_speed - speed of rotation of object at this moment.
    max_angular_speed - maximum of absolute value of turning speed. Clockwise
    rotation speed - equals to counterclockwise rotation speed.


    set_speed(self, speed)
    move_forward(self)
    turn_on_angle(self)
    set_angular_speed(self, angular_speed)
    turn_to_face(self, x, y)
    """

    def __init__(self, init_speed, max_speed, min_speed,
                 init_angle, init_angular_speed, max_angular_speed):
        self._speed = init_speed
        self._max_speed = max_speed
        self._min_speed = min_speed
        self._angle = init_angle
        self._angular_speed = init_angular_speed
        self._max_angular_speed = max_angular_speed

    def set_speed(self, speed):
        """Sets speed of this object with check on speed limits."""
        if speed > self._max_speed:
            self._speed = self._max_speed
        elif speed < self.min_speed:
            self._speed = self._min_speed
        else:
            self._speed = speed

    # TODO: implement when we define strictly how angle is measured
    def move_forward(self):
        """Moves this object "forward" on length determined by speed"""
        raise NotImplementedError("Not implemented yet")

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
