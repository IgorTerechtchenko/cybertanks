from displayable import Displayable


class Movable(Displayable):
    """
    Base class for any object that can move on the gaming field.
    
    speed - linear speed of this object at this moment.
    max_speed - maximal possible speed for this object.
    min_speed - minimal possible speed for this object.
    angle - angle of rotation for speed vector of this object.
    
    set_speed(self, speed)
    move_forward(self)
    """

    def __init__(self, init_speed, max_speed, min_speed, angle):
        self._speed = init_speed
        self._max_speed = max_speed
        self._min_speed = min_speed
        self._angle = angle

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
