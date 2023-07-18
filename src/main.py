#!/usr/bin/env python3

import pygame
import asyncio

from classes.button import Button
from classes.button_style import ButtonStyle

pygame.init()

global WIDTH, HEIGHT, SCREEN, SCREEN_FLAGS, CLOCK

WIDTH, HEIGHT = 480, 640

SCREEN_FLAGS = 0
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), SCREEN_FLAGS)
CLOCK = pygame.time.Clock()

pygame.display.set_caption("Lineox")


async def main():
    button: Button = Button(pygame.Vector2(150, 150), pygame.Vector2(128, 64),
                            default_style=ButtonStyle(text="sex", text_color=pygame.Color(
                                255, 255, 255), background_color=pygame.Color(0, 0, 255)),
                            hovered_style=ButtonStyle(text="sex?", text_color=pygame.Color(255, 0, 0),
                                                      background_color=pygame.Color(0, 255, 255)),
                            clicked_style=ButtonStyle(text="sex!", text_color=pygame.Color(0, 255, 255), background_color=pygame.Color(255, 255, 255)))

    def sex_button():
        print("sex button clicked")

    button.add_callback(sex_button)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        SCREEN.fill((0, 0, 0))

        # Draw all UI elements here

        button.handle_events(event)
        button.draw(SCREEN)
        pygame.display.flip()

        # Make it depend on FPS
        CLOCK.tick(60)


if __name__ == "__main__":
    asyncio.run(main())

pygame.quit()
