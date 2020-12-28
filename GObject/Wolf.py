import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp

class Wolf(BaseGObject):
    def __init__(self, x, y):
        animated = [
            {
                'path': 'media/wolf/wolf_0.png',
                'duration': 200
            },
            {
                'path': 'media/wolf/wolf_1.png',
                'duration': 200
            },
            {
                'path': 'media/wolf/wolf_2.png',
                'duration': 200
            },
            {
                'path': 'media/wolf/wolf_3.png',
                'duration': 200
            },
            {
                'path': 'media/wolf/wolf_4.png',
                'duration': 200
            },
            {
                'path': 'media/wolf/wolf_5.png',
                'duration': 200
            },
            {
                'path': 'media/wolf/wolf_6.png',
                'duration': 200
            },
            {
                'path': 'media/wolf/wolf_7.png',
                'duration': 200
            }
        ]

        super(Wolf, self).__init__(animated, 0.2, x, y)
        self.setMaxSpeed(10)