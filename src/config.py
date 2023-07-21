from pygame import Vector2
from enum import Enum


class FontsEnum():
    DEFAULT: str = "fonts/Ubuntu-R.ttf"
    VT323: str = "fonts/VT323-Regular.ttf"
    ROBOTO: str = "fonts/Roboto-Regular.ttf"
    LINERAMA: str = "fonts/Linerama-Regular.ttf"


global default_display_resolution, display_resolution

default_display_resolution: Vector2 = Vector2(480, 640)
display_resolution: Vector2 = default_display_resolution
