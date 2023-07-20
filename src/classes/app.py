import pygame
import config

from pygame.time import Clock
from pygame.surface import Surface
from pygame import Vector2
from typing import List, Optional
from layout import Interface


class App():
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, interface: Interface):
        self._is_running: bool = True

        self.clock: Clock = Clock()
        self.surface: Surface = None

        self.interface = interface

    def refresh_display(self, resolution: Optional[Vector2] = config.display_resolution):
        self.surface = pygame.display.set_mode(
            (resolution.x, resolution.y), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

        config.display_resolution = resolution

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Lineox")

        self.refresh_display()
        self._is_running = True

    def on_event(self, event: pygame.event):
        if event.type == pygame.QUIT:
            self._is_running = False
        elif event.type == pygame.VIDEORESIZE:
            config.display_resolution = Vector2(event.w, event.h)

        for key, page in self.interface.pages.items():
            if not page.is_visible:
                continue

            for widget in page.widgets:
                widget.handle_events(event)
                widget.update_rect()

    def on_loop(self):
        pass

    def on_render(self):
        self.surface.fill((0, 0, 0))

        for key, page in self.interface.pages.items():
            if not page.is_visible:
                continue

            for widget in page.widgets:
                widget.draw(self.surface)

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._is_running = False

        while (self._is_running):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

            self.clock.tick(60)
        self.on_cleanup()
