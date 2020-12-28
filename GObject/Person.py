import pygame as pg

class Person:
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('media/Person.png')
        self.width = (int)(self.image.get_width() * 0.2)
        self.height = (int)(self.image.get_height() * 0.2)
        self.image = pg.transform.scale(
            self.image, (self.width, self.height)).convert_alpha()
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, self.image.get_width(),
                            self.image.get_height())

    def setPos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(),
                            self.image.get_height())

    def move(self, move):
        self.x += move[0]
        self.y += move[1]
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(),
                            self.image.get_height())

    def wasClicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        else:
            return False