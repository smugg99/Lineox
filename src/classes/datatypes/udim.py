from typing import Optional

from pygame import Vector2

import config


# ================# Classes #================ #


class UDim:
    def __init__(self, scale: Vector2, offset: Optional[Vector2] = Vector2(0, 0)):
        self._scale: Vector2 = scale
        self._offset: Vector2 = offset
        self._calc: Vector2 = None

    @property
    def scale(self) -> Vector2:
        return self._scale

    @scale.setter
    def scale(self, new_scale: Vector2):
        self._scale = new_scale
        self._calc = None

    @property
    def offset(self) -> Vector2:
        return self._offset

    @offset.setter
    def offset(self, new_offset: Vector2):
        self._offset = new_offset
        self._calc = None

    @property
    def calc(self) -> Vector2:
        return (Vector2(config.display_resolution.x * self._scale.x,
                        config.display_resolution.y * self._scale.y)) + self._offset

    def __repr__(self):
        return f"UDim(scale=Vector2({self._scale.x}, {self._scale.y}), offset=Vector2({self._offset.x}, {self._offset.y})), Vector2({self.calc.x}, {self.calc.y})"

    @classmethod
    def from_scale(cls, x: float, y: float):
        return cls(Vector2(x, y))

    @classmethod
    def from_offset(cls, x: float, y: float):
        return cls(Vector2(0, 0), Vector2(x, y))


# ================# Classes #================ #
