from enum import Enum

import pygame
from pygame import Rect, Vector2
from pygame.event import Event

from classes.datatypes.udim import UDim


# ================# Enums #================ #

class FontsEnum(Enum):
    DEFAULT: str = "fonts/Ubuntu-R.ttf"
    VT323: str = "fonts/VT323-Regular.ttf"
    ROBOTO: str = "fonts/Roboto-Regular.ttf"
    LINERAMA: str = "fonts/Linerama-Regular.ttf"

# ================# Enums #================ #


# ================# Classes #================ #


class BaseWidget:
    def __init__(
        self,
        position: UDim,
        size: UDim,
        anchor: Vector2 = Vector2(0, 0)
    ):

        self.position: UDim = position

        self.size: UDim = size
        self.anchor: Vector2 = anchor
        self.rect: Rect = None

        self._updated: bool = False

        # Can't use the unique update method here because it has not been initialized yet
        self.update_rect()

    @property
    def raw_position(self) -> Vector2:
        return self.position.calc - Vector2(self.size.calc.x *
                                            self.anchor.x, self.size.calc.y * self.anchor.y)

    def update_rect(self):
        calc: Vector2 = self.position.calc - Vector2(self.size.calc.x *
                                                     self.anchor.x, self.size.calc.y * self.anchor.y)

        if self.rect is None:
            self.rect: Rect = Rect(
                calc.x, calc.y, self.size.calc.x, self.size.calc.y)
        else:
            self.rect.x = calc.x
            self.rect.y = calc.y

            self.rect.width = self.size.calc.x
            self.rect.height = self.size.calc.y

    def handle_events(self, event: Event):
        if event.type == pygame.VIDEORESIZE:
            self.update()

    # Unique update function for each subclass
    def update(self):
        self.update_rect()
        self._updated = True

    def draw(self):
        raise NotImplementedError(
            "Subclasses must implement the draw() method")


# ================# Classes #================ #
