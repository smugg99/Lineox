#!/usr/bin/env python3

import layout
from classes.app import App

global app
app = App()


app.interface = layout.interface


# ================# Functions #================ #


def main():
    app.on_execute()


# ================# Functions #================ #

if __name__ == "__main__":
    main()
