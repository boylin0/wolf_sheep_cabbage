import pygame as pg

from GObject.BaseGObject import BaseGObject
from Utils.Utils import clamp

import random


class Cloud(BaseGObject):
    def __init__(self, width, HeightStart, HeightRange, SizeMin, SizeMax):

        img_paths = [
            'media/cloud/cloud_type0_0.png',
            'media/cloud/cloud_type1_0.png',
            'media/cloud/cloud_type2_0.png',
        ]

        animated = [
            {
                'path': random.choice(img_paths),
                'duration': 1000
            },
        ]

        super(Cloud, self).__init__(animated, 0.2, 0, 0)
        self.setMaxSpeed(random.uniform(0.5, 1.0))
        self.loopWidth = width
        self.HeightStart = HeightStart
        self.HeightRange = HeightRange
        self.SizeMin = SizeMin
        self.SizeMax = SizeMax
        self.setPos((random.randrange(-self.width, self.loopWidth),
                     random.randrange(self.HeightStart, self.HeightStart+self.HeightRange)))
        self._rand_cloud_scale()

    def _rand_cloud_scale(self):
        scale = random.uniform(self.SizeMin,self.SizeMax)
        self.image = pg.transform.scale(self.image, (int(self._original_width * scale), int(self._original_height * scale)))

    def update(self):
        if self.x < -self.width:
            self.setPos((self.loopWidth,
                     random.randrange(self.HeightStart, self.HeightStart+self.HeightRange)))
            self._rand_cloud_scale()
        else:
            self.setPos((self.x-self.maxSpeed, self.y))
