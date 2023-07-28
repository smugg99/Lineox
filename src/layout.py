import copy
from typing import List

from pygame import Color, Vector2
from pygame.font import Font

import config
from classes.app import App
from classes.datatypes.number_range import NumberRange
from classes.datatypes.udim import UDim
from classes.interface import Interface
from classes.page import Page
from classes.widgets.button import Button, ButtonStyle
from classes.widgets.label import Label, LabelStyle
from config import FontsEnum

global interface
interface: Interface = Interface()

global app
app = App()

main_page: Page = Page()

title_label1: Label = Label(UDim.from_scale(0.5, 0.1), UDim.from_scale(
    1, 0.15), anchor=Vector2(0.5, 0.5),
    default_style=LabelStyle("Lineox", Color(255, 0, 0), text_font=FontsEnum.DEFAULT.value, text_scaled=True, background_color=Color(255, 255, 255)))

description_style: LabelStyle = LabelStyle("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt,\nipsum eu posuere pulvinar, tortor ex varius odio,\nvitae varius purus eros a urna.", Color(
    255, 0, 0), text_wrapped=True, text_font=FontsEnum.DEFAULT.value, text_scaled=True, background_color=Color(255, 255, 255))

description_style1: LabelStyle = LabelStyle("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt,\nipsum eu posuere pulvinar, tortor ex varius odio,\nvitae varius purus eros a urna.", Color(
    255, 0, 0), text_wrapped=True, text_font=FontsEnum.DEFAULT.value, text_scaled=False, text_size=8, background_color=Color(255, 255, 255))

description_style2: LabelStyle = LabelStyle("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt, ipsum eu posuere pulvinar, tortor ex varius odio, vitae varius purus eros a urna.", Color(
    255, 0, 0), text_wrapped=True, text_font=FontsEnum.DEFAULT.value, text_scaled=False, text_size=NumberRange(2, 32), background_color=Color(255, 255, 255))


description_label1: Label = Label(UDim.from_scale(0.5, 0.3), UDim.from_scale(
    0.75, 0.15), anchor=Vector2(0.5, 0.5),
    default_style=description_style)

description_label2: Label = Label(UDim.from_scale(0.5, 0.5), UDim.from_scale(
    0.75, 0.15), anchor=Vector2(0.5, 0.5),
    default_style=description_style1)

description_label3: Label = Label(UDim.from_scale(0.5, 0.7), UDim.from_scale(
    0.75, 0.15), anchor=Vector2(0.5, 0.5),
    default_style=description_style2)


play_button: Button = Button(UDim.from_scale(
    0.5, 1), UDim.from_scale(0.4, 0.15), anchor=Vector2(0.5, 1),
    default_style=ButtonStyle("Le default text", Color(255, 255, 255), text_font=FontsEnum.DEFAULT.value, text_scaled=True, background_color=Color(0, 255, 0)))

main_page.add_widget(title_label1)
main_page.add_widget(description_label1)
main_page.add_widget(description_label2)
main_page.add_widget(description_label3)

main_page.add_widget(play_button)

main_page.show()


def button_callback1():
    print("Changing resolution")

    new_res: Vector2 = Vector2(720, 1280) if config.display_resolution == Vector2(
        480, 640) else Vector2(480, 640)

    play_button.current_style.text = "to: " + str(int(config.display_resolution.x)) + \
        "x" + str(int(config.display_resolution.y))
    app.refresh_display(new_res)


play_button.add_callback(button_callback1)

interface.add_page(main_page, "main")
