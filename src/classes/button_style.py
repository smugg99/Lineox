from pygame import Color
from typing import Dict, Optional


class ButtonStyle:
    def __init__(self, text: str, text_color: Color, background_color: Color):
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
