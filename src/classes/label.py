import pygame
import config
import copy

from config import FontsEnum
from pygame import Vector2, Color, Surface, Rect
from pygame.event import Event
from pygame.font import Font, SysFont
from typing import Dict, Callable, List, Union, Optional
from classes.number_range import NumberRange
from classes.udim import UDim
from classes.widget import Widget


class LabelStyle:
    def __init__(self, text: str, text_color: Color, text_font: Optional[FontsEnum] = FontsEnum.DEFAULT, text_size: Optional[Union[int, NumberRange]] = 16, text_scaled: Optional[bool] = False, background_color: Optional[Color] = Color(0, 0, 0, 0)):
        self.text: str = text
        self.text_color: Color = text_color
        self.text_font: FontsEnum = text_font
        self.text_size: Union[int, NumberRange] = text_size
        self.text_scaled: Optional[bool] = text_scaled
        self.background_color: Color = background_color


class Label(Widget):
    def __init__(self, position: UDim, size: UDim, default_style: LabelStyle, anchor: Optional[Vector2] = Vector2(0, 0)):
        super().__init__(position, size, anchor)

        self.default_style: LabelStyle = default_style

        # Used for derivatives of this class
        self.current_style: LabelStyle = copy.deepcopy(self.default_style)

        self.update()

    def handle_events(self, event: Event):
        super().handle_events(event)

    def update(self):
        # Calculate the new font size based on the scaling factor (e.g., 0.02)
        scaling_factor = min(config.display_resolution.x / config.default_display_resolution.x, config.display_resolution.y /
                             config.default_display_resolution.y)

        relative_font_size: int = None

        if not isinstance(self.default_style.text_size, NumberRange):
            if not self.default_style.text_scaled:
                # Constant font size
                relative_font_size = self.default_style.text_size
            else:
                # Make the font size be constrained to the rect size
                relative_font_size = int(
                    self.default_style.text_size * scaling_factor)
        else:
            # Make the font size be constrained to the number range
            fit_value: int = self.default_style.text_size.max_value or self.default_style.text_size.min_value
            relative_font_size = int(self.default_style.text_size.constrain(
                fit_value * scaling_factor))

        print(relative_font_size)
        self.current_style.text_size = relative_font_size

    def draw(self, surface: Surface):
        pygame.draw.rect(
            surface, self.current_style.background_color, self.rect)

        font: Font = Font(
            self.current_style.text_font, self.current_style.text_size)

        text_surface: Surface = font.render(
            self.current_style.text, True, self.current_style.text_color)
        text_rect: Rect = text_surface.get_rect(center=self.rect.center)

        surface.blit(text_surface, text_rect)
