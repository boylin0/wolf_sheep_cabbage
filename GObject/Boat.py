import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp

class Boat(BaseGObject):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        animated = [
            {
                'path': 'media/boat/boat_0.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_r_1.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_r_2.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_r_3.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_r_2.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_r_1.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_0.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_l_1.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_l_2.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_l_3.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_l_2.png',
                'duration': 300
            },
            {
                'path': 'media/boat/boat_swing_l_1.png',
                'duration': 300
            },
        ]

        super(Boat, self).__init__(animated, 0.5, x, y)

        self.isMoving = False
        self.Carrying = None
        self.Crossed = False

    def update(self):
        super().update()
        if not self.Carrying == None and self.isMoving:
            self.Carrying.setPos(
                (self.x + self.width - self.Carrying.width - 10,
                 self.rect.bottom - self.Carrying.height - 30))