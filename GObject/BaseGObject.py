import pygame as pg

from Utils.Utils import clamp


class BaseGObject:
    def __init__(self, animatedList, resizeRate, x, y):
        pg.sprite.Sprite.__init__(self)

        # load base image size
        self.image = pg.image.load(animatedList[0]['path'])
        self.width = (int)(self.image.get_width() * resizeRate)
        self.height = (int)(self.image.get_height() * resizeRate)

        # load images for animating
        self._animatedList = []

        for frame in animatedList:
            self._animatedList.append({
                    'image': pg.transform.scale(pg.image.load(frame['path']), (self.width, self.height)).convert_alpha(),
                    'duration': frame['duration']
            })
        
        self._animatedIndex = 0
        self._lastAnimationChanged = pg.time.get_ticks()
        self.image = self._animatedList[self._animatedIndex]['image']

        # define object position & status
        self.x = x
        self.y = y
        self._target_pos_x = x
        self._target_pos_y = y
        self.rect = pg.Rect(x, y, self.image.get_width(),
                            self.image.get_height())
        self.maxSpeed = 3
        self.isMoving = False

    def setPos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self._target_pos_x = self.x
        self._target_pos_y = self.y
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(),
                            self.image.get_height())

    def move(self, move):
        self.isMoving = True
        self._target_pos_x = (self.x + move[0])
        self._target_pos_y = (self.y + move[1])

    def absMove(self, move):
        self.isMoving = True
        self._target_pos_x = move[0]
        self._target_pos_y = move[1]

    def update(self):


        # Animation Images
        if pg.time.get_ticks() - self._lastAnimationChanged > self._animatedList[self._animatedIndex % len(
                self._animatedList)]['duration']:
            self._animatedIndex += 1
            self.image = self._animatedList[self._animatedIndex % len(
                self._animatedList)]['image']
            self._lastAnimationChanged = pg.time.get_ticks()

        # Animation Moving
        move_delta_x = 0
        move_delta_y = 0
        if self.isMoving == True:

            if self._target_pos_x > self.x:
                move_delta_x = clamp(
                    (self._target_pos_x - self.x) * 0.1, -self.maxSpeed, self.maxSpeed)

            if self._target_pos_x < self.x:
                move_delta_x = - \
                    clamp((self.x - self._target_pos_x) *
                          0.1, -self.maxSpeed, self.maxSpeed)

            if self._target_pos_y > self.y:
                move_delta_y = clamp(
                    (self._target_pos_y - self.y) * 0.1, -self.maxSpeed, self.maxSpeed)

            if self._target_pos_y < self.y:
                move_delta_y = - \
                    clamp((self.y - self._target_pos_y) *
                          0.1, -self.maxSpeed, self.maxSpeed)

        # Moving Done
        if abs(move_delta_x) < 0.08 and abs(move_delta_y) < 0.08:
            self.isMoving = False
            self.x = self._target_pos_x
            self.y = self._target_pos_y
        else:
            self.x += move_delta_x
            self.y += move_delta_y

        self.rect = pg.Rect(self.x, self.y, self.image.get_width(),
                            self.image.get_height())

    def wasClicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        else:
            return False
