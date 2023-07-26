import config

from config import FontsEnum
from pygame import Vector2, Color
from pygame.font import Font

from classes.interface import Interface
from classes.page import Page
from classes.udim import UDim
from classes.button import Button, ButtonStyle
from classes.label import Label, LabelStyle
from classes.number_range import NumberRange

from classes.app import App

global interface
interface: Interface = Interface()

app = App(interface)

main_page: Page = Page()

title_label1: Label = Label(UDim.from_scale(0.5, 0.1), UDim.from_scale(
    1, 0.15), anchor=Vector2(0.5, 0.5),
    default_style=LabelStyle("Lineox", Color(255, 0, 0), text_font=FontsEnum.DEFAULT, text_scaled=True, background_color=Color(255, 255, 255)))

description_label1: Label = Label(UDim.from_scale(0.5, 0.5), UDim.from_scale(
    0.75, 0.55), anchor=Vector2(0.5, 0.5),
    default_style=LabelStyle("!START! Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt,\nipsum eu posuere pulvinar, tortor ex varius odio,\nvitae varius purus eros a urna. Sed felis lectus,\nvestibulum quis consectetur sed, hendrerit nec sapien.\nSed ante dolor, suscipit sit amet molestie sed, vulputate sit amet. !STOP!", Color(255, 0, 0), text_wrapped=True, text_font=FontsEnum.DEFAULT, text_scaled=True, background_color=Color(255, 255, 255)))


play_button: Button = Button(UDim.from_scale(
    0.5, 1), UDim.from_scale(0.4, 0.15), anchor=Vector2(0.5, 1),
    default_style=LabelStyle("Play", Color(255, 255, 255), background_color=Color(0, 255, 0)))

main_page.add_widget(title_label1)
main_page.add_widget(description_label1)

main_page.add_widget(play_button)

main_page.show()

interface.add_page(main_page, "main")


def button_callback():
    print("Changing resolution")

    new_res: Vector2 = Vector2(720, 1280) if config.display_resolution == Vector2(
        480, 640) else Vector2(480, 640)

    app.refresh_display(new_res)


play_button.add_callback(button_callback)
