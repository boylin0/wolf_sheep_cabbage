import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp


class UIObject(BaseGObject):
    def __init__(self, image, resizeRate, x, y):
        animated = [
            {
                'path': image,
                'duration': 1000
            },
        ]

        super(UIObject, self).__init__(animated, resizeRate, x, y)
