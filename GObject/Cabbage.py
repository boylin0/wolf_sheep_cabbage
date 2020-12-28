import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp

class Cabbage(BaseGObject):
    def __init__(self, x, y):
        animated = [
            {
                'path': 'media/cabbage.png',
                'duration': 1000
            },
        ]

        super(Cabbage, self).__init__(animated, 0.18, x, y)
