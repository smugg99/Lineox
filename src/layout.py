import config

from pygame import Vector2, Color

from classes.interface import Interface
from classes.page import Page
from classes.udim import UDim
from classes.button import Button, ButtonStyle
from classes.label import Label, LabelStyle

from classes.app import App

global interface
interface: Interface = Interface()

app = App(interface)

main_page: Page = Page()

title_label: Label = Label(UDim.from_scale(0.5, 0.1), UDim.from_scale(
    1, 0.15), anchor=Vector2(0.5, 0.5),
    default_style=LabelStyle("Lineox", Color(255, 0, 0), Color(255, 255, 255)))

play_button: Button = Button(UDim.from_scale(
    0.5, 0.5), UDim.from_scale(0.4, 0.15), anchor=Vector2(0.5, 0.5),
    default_style=ButtonStyle("Nuthin", Color(
        0, 255, 0), Color(128, 128, 128)),
    hovered_style=ButtonStyle("Hovered", Color(
        64, 255, 64), Color(96, 96, 96)),
    clicked_style=ButtonStyle("Clicked", Color(255, 255, 0), Color(32, 32, 32)))

test_button: Button = Button(UDim.from_scale(
    0.5, 0.75), UDim.from_scale(0.4, 0.15), anchor=Vector2(0.5, 0.5),
    default_style=ButtonStyle("Nuthin", Color(
        0, 255, 0), Color(128, 128, 128)),
    hovered_style=ButtonStyle("Hovered", Color(
        64, 255, 64), Color(96, 96, 96)),
    clicked_style=ButtonStyle("Clicked", Color(255, 255, 0), Color(32, 32, 32)))

main_page.add_widget(title_label)
main_page.add_widget(play_button)
main_page.add_widget(test_button)
main_page.show()

interface.add_page(main_page, "main")


def button_callback():
    print("Changing resolution")

    new_res: Vector2 = Vector2(720, 1280) if config.display_resolution == Vector2(
        480, 640) else Vector2(480, 640)
    
    app.refresh_display(new_res)


play_button.add_callback(button_callback)
