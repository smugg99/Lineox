from typing import Dict, List

from pygame import Color, Vector2

from classes.page import Page

# ================# Classes #================ #


class Interface:
    def __init__(self):
        self.pages: Dict[str, Page] = {}

    def add_page(self, page: Page, key: str):
        if key in self.pages:
            return

        self.pages[key] = page
        
        for widget in page.widgets:
            widget.update()

    def remove_page(self, key: str):
        if key in self.pages:
            del (self.pages[key])


# ================# Classes #================ #
