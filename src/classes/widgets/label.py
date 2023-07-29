import copy
from typing import Callable, Dict, List, Optional, Tuple, Union

import pygame
from pygame import Color, Rect, Surface, Vector2
from pygame.event import Event
from pygame.font import Font

import config
from classes.datatypes.number_range import NumberRange
from classes.datatypes.udim import UDim
from classes.widgets.base_widget import BaseWidget
from config import FontsEnum

from enum import Enum

pygame.font.init()


# ================# Enums #================ #

class TextAlign(Enum):
    LEFT_TOP: Vector2 = Vector2(0, 0)
    LEFT: Vector2 = Vector2(0, 0.5)
    LEFT_BOTTOM: Vector2 = Vector2(0, 1)

    CENTER_TOP: Vector2 = Vector2(0.5, 0)
    CENTER: Vector2 = Vector2(0.5, 0.5)
    CENTER_BOTTOM: Vector2 = Vector2(0.5, 1)

    RIGHT_TOP: Vector2 = Vector2(1, 0)
    RIGHT: Vector2 = Vector2(1, 0.5)
    RIGHT_BOTTOM: Vector2 = Vector2(1, 1)

# ================# Enums #================ #


# ================# Classes #================ #


class LabelStyle:
    def __init__(
        self,
        text: str,
        text_color: Color,
        text_font: Optional[FontsEnum] = FontsEnum.DEFAULT,
        text_size: Optional[Union[int, NumberRange]
                            ] = config.default_text_size,
        text_scaled: Optional[bool] = False,
        text_wrapped: Optional[bool] = False,
        text_align: Optional[TextAlign] = TextAlign.CENTER,
        background_color: Optional[Color] = Color(0, 0, 0, 255)
    ):

        self.text: str = text
        self.text_color: Color = text_color
        self.text_font: FontsEnum = text_font
        self.text_size: Union[int, NumberRange] = text_size
        self.text_scaled: Optional[bool] = text_scaled
        self.text_wrapped: Optional[bool] = text_wrapped
        self.text_align: Optional[TextAlign] = text_align
        self.background_color: Color = background_color


class Label(BaseWidget):
    def __init__(self, position: UDim, size: UDim, default_style: LabelStyle, anchor: Optional[Vector2] = Vector2(0, 0)):
        super().__init__(position, size, anchor)

        # Default style is constant
        self.default_style: LabelStyle = default_style

        # Current style contains values which are often computed in the update methods (fe. text size)
        self.current_style: LabelStyle = copy.deepcopy(self.default_style)

        self._text_lines: List[str] = []

        self.update()

    def handle_events(self, event: Event):
        super().handle_events(event)

    def update(self):
        super().update()

        relative_font_size: int = config.default_text_size

        if self.default_style.text_wrapped:

            # ================# Local Functions #================ #

            def split_text(font_size: int) -> Tuple[List[str], int]:
                lines: List[str] = []
                temp_font: Font = Font(self.default_style.text_font, font_size)

                words: List[str] = self.default_style.text.split()

                current_line_width: int = 0
                current_lines_height: int = 0

                current_line: List[str] = []
                line_size: int = temp_font.get_linesize()

                for word in words:
                    text_width, _ = temp_font.size(word + " ")

                    if current_line_width + text_width <= self.rect.width:
                        current_line.append(word)

                        current_line_width += text_width
                    else:
                        lines.append(" ".join(current_line))

                        current_line_width = 0
                        current_line = [word]

                        current_line_width = text_width
                        current_lines_height += line_size

                    if word == words[len(words) - 1] and current_line:
                        lines.append(" ".join(current_line))

                # Add artificial line into the calculation to compensate for the algorithm innacuracies
                safe_total_lines_height = (len(lines) + 0.5) * \
                    (temp_font.get_linesize())

                return lines, safe_total_lines_height

            def get_optimised_font_size_and_lines() -> Tuple[int, List[str]]:
                font_size: int = config.min_text_size

                if isinstance(self.default_style.text_size, NumberRange):
                    font_size = self.default_style.text_size.min_value

                while True:
                    lines, total_lines_height = split_text(font_size)

                    # Constraining text size has to be implemented here since
                    # the algorithm has to slice text with such size range
                    if isinstance(self.default_style.text_size, NumberRange):
                        if not self.default_style.text_size.is_in_range(font_size) or total_lines_height > self.rect.height:
                            return font_size - 1 if font_size > 1 else 1, lines

                    else:
                        if total_lines_height > self.rect.height:
                            return font_size - 1 if font_size > 1 else 1, lines

                    font_size += 1

            # ================# Local Functions #================ #

            if not isinstance(self.default_style.text_size, NumberRange):
                if not self.default_style.text_scaled:
                    # Constant font size
                    text_lines, _ = split_text(self.default_style.text_size)

                    self._text_lines = text_lines
                    relative_font_size = self.default_style.text_size
                else:
                    font_size, text_lines = get_optimised_font_size_and_lines()

                    self._text_lines = text_lines
                    relative_font_size = font_size
            else:
                # Make the font size be constrained to the number range
                font_size, text_lines = get_optimised_font_size_and_lines()
                relative_font_size = font_size

                self._text_lines = text_lines
        else:

            # ================# Local Functions #================ #

            def get_optimized_font_size() -> int:
                font_size: int = config.min_text_size

                while True:
                    temp_font: Font = Font(
                        self.default_style.text_font, font_size)
                    font_width, font_height = temp_font.size(
                        self.default_style.text)

                    if font_width > self.rect.width or font_height > self.rect.height:
                        break
                    font_size += 1

                # The last font_size was the one that exceeded the rectangle
                return font_size - 1 if font_size > 1 else 1

            # ================# Local Functions #================ #

            # Adjust font size
            if not isinstance(self.default_style.text_size, NumberRange):
                if not self.default_style.text_scaled:
                    # Constant font size
                    relative_font_size = self.default_style.text_size
                else:
                    # Make the font size be constrained to the rect size
                    relative_font_size = get_optimized_font_size()
            else:
                # Make the font size be constrained to the number range
                fit_value: int = get_optimized_font_size()
                relative_font_size = int(self.default_style.text_size.constrain(
                    fit_value * config.scaling_factor))

        self.current_style.text_size = relative_font_size

    def draw(self, surface: Surface):
        pygame.draw.rect(
            surface, self.current_style.background_color, self.rect)

        font: Font = Font(self.current_style.text_font,
                          self.current_style.text_size)

        initial_position: Vector2 = self.raw_position

        if self.current_style.text_wrapped:
            for i, text_line in enumerate(self._text_lines):
                text_surface: Surface = font.render(
                    text_line, True, self.current_style.text_color)

                rect_position: Vector2 = initial_position + \
                    Vector2(0, i * self.current_style.text_size)

                surface.blit(text_surface, rect_position)
        else:
            text_surface: Surface = font.render(
                self.current_style.text, True, self.current_style.text_color)

            text_rect: Rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)


# ================# Classes #================ #
