from pygame import Vector2
from enum import Enum


class FontsEnum():
    DEFAULT: str = "fonts/Ubuntu-R.ttf"
    VT323: str = "fonts/VT323-Regular.ttf"
    ROBOTO: str = "fonts/Roboto-Regular.ttf"
    LINERAMA: str = "fonts/Linerama-Regular.ttf"


global default_display_resolution, display_resolution, scaling_factor
default_display_resolution: Vector2 = Vector2(480, 640)
display_resolution: Vector2 = default_display_resolution
scaling_factor: float = 1.0


def recalculate_display_globals(new_resolution: Vector2):
    global display_resolution, scaling_factor
    display_resolution = new_resolution
    scaling_factor = min(display_resolution.x / default_display_resolution.x,
                         display_resolution.y / default_display_resolution.y)