import pygame

from typing import Dict, Callable, List, Optional
from classes.button_style import ButtonStyle


class Button:
    def __init__(self, position: pygame.Vector2, size: pygame.Vector2, default_style: ButtonStyle, hovered_style: Optional[ButtonStyle] = None, clicked_style: Optional[ButtonStyle] = None):
        self.rect: pygame.Rect = pygame.Rect(
            position.x, position.y, size.x, size.y)

        self.event_callbacks: List[Callable] = []

        self.default_style: ButtonStyle = default_style
        self.hovered_style: ButtonStyle = hovered_style or default_style
        self.clicked_style: ButtonStyle = clicked_style or default_style

        self.is_clicked: bool = False
        self.is_hovered: bool = False

    def handle_events(self, event: pygame.event.Event):
        # Check if the button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.is_clicked = True

                    print("Calling callbacks")

                    for callback in self.event_callbacks:
                        callback()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_clicked = False

        # Check if the button is hovered
        self.is_hovered = self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface: pygame.Surface):
        current_style: ButtonStyle = None

        # Adjust button style based on its state
        if self.is_clicked:
            current_style = self.clicked_style
        elif self.is_hovered:
            current_style = self.hovered_style
        else:
            current_style = self.default_style

        print("Clicked: " + str(self.is_clicked) + " Hovered: " +
              str(self.is_hovered) + " | " + str(current_style.text))
        pygame.draw.rect(surface, current_style.background_color, self.rect)

        font = pygame.font.SysFont("Corbel", 32)
        text_surface = font.render(
            current_style.text, True, (current_style.text_color.r, current_style.text_color.g, current_style.text_color.b))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def add_callback(self, callback: Callable):
        self.event_callbacks.append(callback)
