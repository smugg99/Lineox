#!/usr/bin/env python3

import pygame
import asyncio
import threading
import time
import random

import layout

from classes.app import App

global app
app = App(layout.interface)

# ================# Functions #================ #


async def main():
    app.on_execute()


# ================# Functions #================ #

if __name__ == "__main__":
    asyncio.run(main())
