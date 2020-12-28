import pygame as pg


class Sheep:
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('media/sheep.png')
        self.width = (int)(self.image.get_width() * 0.1)
        self.height = (int)(self.image.get_height() * 0.1)
        self.image = pg.transform.scale(
            self.image, (self.width, self.height)).convert_alpha()
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
        move_delta_x = 0
        move_delta_y = 0

        if self.isMoving == True:

            if self._target_pos_x > self.x:
                move_delta_x = max(min(self.maxSpeed,
                                       (self._target_pos_x - self.x) / 30), -self.maxSpeed)

            if self._target_pos_x < self.x:
                move_delta_x = -max(min(self.maxSpeed, (self.x -
                                                        self._target_pos_x) / 30), -self.maxSpeed)

            if self._target_pos_y > self.y:
                move_delta_y = max(min(self.maxSpeed,
                                       (self._target_pos_y - self.y) / 30), -self.maxSpeed)

            if self._target_pos_y < self.y:
                move_delta_y = -max(min(self.maxSpeed, (self.y -
                                                        self._target_pos_y) / 30), -self.maxSpeed)

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
