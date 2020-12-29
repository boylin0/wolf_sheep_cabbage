import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp

class Cabbage(BaseGObject):
    def __init__(self, x, y):
        animated = [
            {
                'path': 'media/cabbage/cabbage_0.png',
                'duration': 200
            },
            {
                'path': 'media/cabbage/cabbage_1.png',
                'duration': 200
            },
            {
                'path': 'media/cabbage/cabbage_2.png',
                'duration': 200
            },
            {
                'path': 'media/cabbage/cabbage_3.png',
                'duration': 200
            },
            {
                'path': 'media/cabbage/cabbage_2.png',
                'duration': 200
            },
            {
                'path': 'media/cabbage/cabbage_1.png',
                'duration': 200
            },
        ]

        super(Cabbage, self).__init__(animated, 0.18, x, y)
        self.setMaxSpeed(10)