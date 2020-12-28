import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp

class Sheep(BaseGObject):
    def __init__(self, x, y):
        animated = [
            {
                'path': 'media/sheep.png',
                'duration': 1000
            },
        ]

        super(Sheep, self).__init__(animated, 0.1, x, y)
