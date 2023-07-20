import pygame

from pygame import Vector2, Color, Surface, Rect
from pygame.event import Event
from pygame.font import Font
from typing import Dict, Callable, List, Optional
from classes.udim import UDim
from classes.widget import Widget


class ButtonStyle:
    def __init__(self, text: str, text_color: Color, background_color: Optional[Color] = Color(0, 0, 0, 0)):
        self.text = text
        self.text_color = text_color
        self.background_color = background_color


class Button(Widget):
    def __init__(self, position: UDim, size: UDim, default_style: ButtonStyle, hovered_style: Optional[ButtonStyle] = None, clicked_style: Optional[ButtonStyle] = None, anchor: Optional[Vector2] = Vector2(0, 0)):
        super().__init__(position, size, anchor)

        self.event_callbacks: List[Callable] = []

        self.default_style: ButtonStyle = default_style
        self.hovered_style: ButtonStyle = hovered_style or default_style
        self.clicked_style: ButtonStyle = clicked_style or default_style

        self.is_clicked: bool = False
        self.is_hovered: bool = False

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

            print(self.rect.collidepoint(event.pos))
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_clicked = False

    def draw(self, surface: Surface):
        current_style: ButtonStyle = None

        # Adjust button style based on its state
        if self.is_clicked:
            current_style = self.clicked_style
        elif self.is_hovered:
            current_style = self.hovered_style
        else:
            current_style = self.default_style

        # print("Clicked: " + str(self.is_clicked) + " Hovered: " + str(self.is_hovered) + " | " + str(current_style.text))
        pygame.draw.rect(surface, current_style.background_color, self.rect)

        font: Font = pygame.font.SysFont("Corbel", 32)
        text_surface: Surface = font.render(
            current_style.text, True, current_style.text_color)
        text_rect: Rect = text_surface.get_rect(center=self.rect.center)

        surface.blit(text_surface, text_rect)

    def add_callback(self, callback: Callable):
        self.event_callbacks.append(callback)
