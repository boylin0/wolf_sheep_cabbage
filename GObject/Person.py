import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp

class Person(BaseGObject):
    def __init__(self, x, y):
        animated = [
            {
                'path': 'media/person/person_0.png',
                'duration': 200
            },
            {
                'path': 'media/person/person_1.png',
                'duration': 200
            },
            {
                'path': 'media/person/person_2.png',
                'duration': 200
            },
            {
                'path': 'media/person/person_1.png',
                'duration': 200
            },

        ]

        super(Person, self).__init__(animated, 0.2, x, y)
