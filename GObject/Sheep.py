import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp

class Sheep(BaseGObject):
    def __init__(self, x, y):
        animated = [
            {
                'path': 'media/sheep/sheep_0.png',
                'duration': 200
            },
            {
                'path': 'media/sheep/sheep_1.png',
                'duration': 200
            },
            {
                'path': 'media/sheep/sheep_2.png',
                'duration': 200
            },
            {
                'path': 'media/sheep/sheep_3.png',
                'duration': 200
            },
            {
                'path': 'media/sheep/sheep_4.png',
                'duration': 200
            },
            {
                'path': 'media/sheep/sheep_5.png',
                'duration': 200
            },
            {
                'path': 'media/sheep/sheep_6.png',
                'duration': 200
            },
            {
                'path': 'media/sheep/sheep_5.png',
                'duration': 200
            },
            {
                'path': 'media/sheep/sheep_4.png',
                'duration': 200
            },
            {
                'path': 'media/sheep/sheep_3.png',
                'duration': 200
            }
        ]


        super(Sheep, self).__init__(animated, 0.125, x, y)
        self.setMaxSpeed(10)