import pygame

from pygame import Rect, Vector2
from pygame.event import Event
from classes.udim import UDim


class Widget:
    def __init__(self, position: UDim, size: UDim, anchor: Vector2 = Vector2(0, 0)):
        self.position: UDim = position
        self.size: UDim = size
        self.anchor: Vector2 = anchor
        self.rect: Rect = None

        # This shit below has to be recreated after changing resolution because it operates on the calculated values of UDim
        self.update_rect()

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
            self.update_rect()

    def draw(self):
        raise NotImplementedError(
            "Subclasses must implement the draw() method")
