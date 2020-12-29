import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp


class Cabbage(BaseGObject):
    def __init__(self, x, y):
        animated = [
            {'path': 'media/cabbage/cabbage_0.png', 'duration': 200},
            {'path': 'media/cabbage/cabbage_1.png', 'duration': 200},
            {'path': 'media/cabbage/cabbage_2.png', 'duration': 200},
            {'path': 'media/cabbage/cabbage_3.png', 'duration': 200},
            {'path': 'media/cabbage/cabbage_2.png', 'duration': 200},
            {'path': 'media/cabbage/cabbage_1.png', 'duration': 200},
        ]

        super(Cabbage, self).__init__(animated, 0.18, x, y)
        self.setMaxSpeed(10)
        self.AddAnimation(
            'eat_cabbage',
            [
                {'path': 'media/cabbage/cabbage_eat_0.png', 'duration': 500},
                {'path': 'media/cabbage/cabbage_eat_1.png', 'duration': 300},
                {'path': 'media/cabbage/cabbage_eat_2.png', 'duration': 300},
                {'path': 'media/cabbage/cabbage_eat_3.png', 'duration': 300},
                {'path': 'media/cabbage/cabbage_eat_4.png', 'duration': 300},
                {'path': 'media/cabbage/cabbage_eat_5.png', 'duration': 300},
                {'path': 'media/cabbage/cabbage_eat_6.png', 'duration': 300},
            ])

        self.AddAnimation(
            'eaten',
            [
                {'path': 'media/cabbage/cabbage_eat_6.png', 'duration': 1000},
            ])
