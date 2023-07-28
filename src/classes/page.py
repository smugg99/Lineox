from typing import Dict, List

from classes.widgets.base_widget import BaseWidget


# ================# Classes #================ #


class Page:
    def __init__(self):
        self.widgets: List[BaseWidget] = []
        self.pages: Dict[str, Page] = []
        self.is_visible: bool = False

    def show(self):
        if self.is_visible:
            return

        print("Showing page")
        self.is_visible = True

    def hide(self):
        if not self.is_visible:
            return

        # Hide all pages inside this page as well?
        print("Hiding page")
        self.is_visible = False

    def add_widget(self, widget: BaseWidget):
        if widget in self.widgets:
            return

        widget.update()

        self.widgets.append(widget)

    def remove_widget(self, widget: BaseWidget):
        if widget not in self.widgets:
            return

        self.widgets.remove(widget)

    def add_page(self, page: "Page", key: str):
        if key in self.pages:
            return

        self.pages[key] = page

        for widget in page.widgets:
            widget.update()

    def remove_page(self, key: str):
        if key in self.pages:
            del (self.pages[key])


# ================# Classes #================ #
