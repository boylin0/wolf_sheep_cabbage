import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp


class Sheep(BaseGObject):
    def __init__(self, x, y):
        animated = [
            {
                'path': 'media/sheep/sheep_0.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_1.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_2.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_3.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_4.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_5.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_6.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_7.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_8.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_9.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_8.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_7.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_6.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_5.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_4.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_3.png',
                'duration': 100
            },
            {
                'path': 'media/sheep/sheep_2.png',
                'duration': 100
            },
        ]

        super(Sheep, self).__init__(animated, 0.125, x, y)
        self.setMaxSpeed(10)
        self.setFlip(True, False)

        self.AddAnimation(
            'eat_cabbage',
            [
                {'path': 'media/sheep/sheep_eat_0.png', 'duration': 500},
                {'path': 'media/sheep/sheep_eat_1.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_2.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_3.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_4.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_5.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_6.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_7.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_8.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_9.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_7.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_6.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_5.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_4.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_3.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_2.png', 'duration': 100},
                {'path': 'media/sheep/sheep_eat_1.png', 'duration': 100},
            ])