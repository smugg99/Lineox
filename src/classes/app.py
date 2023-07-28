from typing import List, Optional

import pygame
from pygame import Vector2
from pygame.surface import Surface
from pygame.time import Clock

import config
from classes.interface import Interface


# ================# Classes #================ #


class App():
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        self._is_running: bool = True

        self.clock: Clock = Clock()
        self.surface: Surface = None
        self.interface: Interface = None

    def refresh_display(self, resolution: Optional[Vector2] = config.display_resolution):
        self.surface = pygame.display.set_mode(
            (resolution.x, resolution.y), pygame.HWSURFACE | pygame.RESIZABLE)

        config.recalculate_display_globals(resolution)

        if self.interface:
            for _, page in self.interface.pages.items():
                if not page.is_visible:
                    continue

                for widget in page.widgets:
                    widget.update()

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Lineox")

        self.refresh_display()
        self._is_running = True

    def on_event(self, event: pygame.event):
        if event.type == pygame.QUIT:
            self._is_running = False
        elif event.type == pygame.VIDEORESIZE:
            config.recalculate_display_globals(Vector2(event.w, event.h))

        if self.interface:
            for _, page in self.interface.pages.items():
                if not page.is_visible:
                    continue

                for widget in page.widgets:
                    widget.handle_events(event)

    def on_loop(self):
        pass

    def on_render(self):
        self.surface.fill((0, 0, 0))

        if self.interface:
            for _, page in self.interface.pages.items():
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

        _updated: bool = False

        while (self._is_running):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

            self.clock.tick(config.max_fps)

            if not _updated:
                if self.interface:
                    for _, page in self.interface.pages.items():
                        if not page.is_visible:
                            continue

                        for widget in page.widgets:
                            widget.update()

                print("First update")
                _updated = True
        self.on_cleanup()


# ================# Classes #================ #
