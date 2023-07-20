import pygame

from pygame import Vector2, Color, Surface, Rect
from pygame.event import Event
from pygame.font import Font
from typing import Dict, Callable, List, Optional
from classes.udim import UDim
from classes.widget import Widget


class LabelStyle:
    def __init__(self, text: str, text_color: Color, background_color: Optional[Color] = Color(0, 0, 0, 0)):
        self.text = text
        self.text_color = text_color
        self.background_color = background_color


class Label(Widget):
    def __init__(self, position: UDim, size: UDim, default_style: LabelStyle, anchor: Optional[Vector2] = Vector2(0, 0)):
        super().__init__(position, size, anchor)

        self.default_style: LabelStyle = default_style

    def handle_events(self, event: Event):
        super().handle_events(event)

    def draw(self, surface: Surface):
        pygame.draw.rect(
            surface, self.default_style.background_color, self.rect)

        font: Font = pygame.font.SysFont("Corbel", 32)
        text_surface: Surface = font.render(
            self.default_style.text, True, self.default_style.text_color)
        text_rect: Rect = text_surface.get_rect(center=self.rect.center)

        surface.blit(text_surface, text_rect)
