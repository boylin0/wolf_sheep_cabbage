import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp

class Person(BaseGObject):
    def __init__(self, x, y):
        animated = [
            {
                'path': 'media/person.png',
                'duration': 1000
            },
        ]

        super(Person, self).__init__(animated, 0.2, x, y)
