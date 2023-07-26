import pygame
import config
import copy

from config import FontsEnum
from pygame import Vector2, Color, Surface, Rect
from pygame.event import Event
from pygame.font import Font, SysFont
from typing import Dict, Callable, List, Optional, Union
from classes.number_range import NumberRange
from classes.udim import UDim
from classes.label import Label, LabelStyle


# ================# Classes #================ #


class ButtonStyle(LabelStyle):
    def __init__(self, text: str, text_color: Color, text_font: Optional[FontsEnum] = FontsEnum.DEFAULT, text_size: Optional[Union[int, NumberRange]] = 16, text_scaled: Optional[bool] = False, background_color: Optional[Color] = Color(0, 0, 0, 255)):
        super().__init__(text, text_color, text_font,
                         text_size, text_scaled, background_color)


class Button(Label):
    def __init__(self, position: UDim, size: UDim, default_style: ButtonStyle, hovered_style: Optional[ButtonStyle] = None, clicked_style: Optional[ButtonStyle] = None, anchor: Optional[Vector2] = Vector2(0, 0)):
        super().__init__(position, size, default_style, anchor=anchor)

        self.event_callbacks: List[Callable] = []

        self.default_style: ButtonStyle = default_style
        self.hovered_style: ButtonStyle = hovered_style or default_style
        self.clicked_style: ButtonStyle = clicked_style or default_style

        self.current_style: ButtonStyle = copy.deepcopy(self.default_style)

        self.is_clicked: bool = False
        self.is_hovered: bool = False

        self.update()

    # This is basically additional logic of the label but as a button
    def handle_events(self, event: Event):
        super().handle_events(event)

        # Check if the button is hovered
        self.is_hovered = self.rect.collidepoint(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEMOTION:
            if not self.rect.collidepoint(event.pos):
                self.is_clicked = False

        # Check if the button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if event.button == 1:
                    self.is_clicked = True

                    print("Calling callbacks")

                    for callback in self.event_callbacks:
                        callback()
            else:
                self.is_clicked = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_clicked = False

    def update(self):
        pass

    def draw(self, surface: Surface):
        # Adjust button style based on its state
        if self.is_clicked:
            self.current_style = self.clicked_style
        elif self.is_hovered:
            self.current_style = self.hovered_style
        else:
            self.current_style = self.default_style

        # Draw the label
        super().draw(surface)

    def add_callback(self, callback: Callable):
        self.event_callbacks.append(callback)


# ================# Classes #================ #
