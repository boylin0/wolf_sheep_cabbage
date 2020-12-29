import pygame as pg

from Utils.Utils import clamp


class BaseGObject:
    def __init__(self, animatedList, resizeRate, x, y):
        pg.sprite.Sprite.__init__(self)

        # load base image size
        self.image = pg.image.load(animatedList[0]['path'])
        self.width = (int)(self.image.get_width() * resizeRate)
        self.height = (int)(self.image.get_height() * resizeRate)
        self._original_width = self.width
        self._original_height = self.height
        self._original_x = x
        self._original_y = y

        # load images for animating
        self._named_animations = {}

        self._named_animations['Idle'] = []

        for frame in animatedList:
            self._named_animations['Idle'].append({
                'image': pg.transform.scale(pg.image.load(frame['path']), (self.width, self.height)).convert_alpha(),
                'duration': frame['duration']
            })

        self._animationIdleName = 'Idle'

        # Load Named Animation
        self._animatedIndex = 0
        self._lastAnimationChanged = pg.time.get_ticks()
        self.image = self._named_animations['Idle'][0]['image']
        self._onceAnimation = False
        self._animationName = self._animationIdleName

        # define object position & status
        self.x = x
        self.y = y
        self._target_pos_x = x
        self._target_pos_y = y
        self.rect = pg.Rect(x, y, self.image.get_width(),
                            self.image.get_height())
        self.maxSpeed = 3
        self.isMoving = False

    def AddAnimation(self, animationName, animation):
        '''
        animation = [
            {'path': 'media/cabbage/cabbage_eat_0.png', 'duration': 100},
            {'path': 'media/cabbage/cabbage_eat_1.png', 'duration': 100},
            {'path': 'media/cabbage/cabbage_eat_2.png', 'duration': 100},
            {'path': 'media/cabbage/cabbage_eat_3.png', 'duration': 100},
            {'path': 'media/cabbage/cabbage_eat_4.png', 'duration': 100},
            {'path': 'media/cabbage/cabbage_eat_5.png', 'duration': 100},
            {'path': 'media/cabbage/cabbage_eat_6.png', 'duration': 100},
        ]
        '''
        self._named_animations[animationName] = []
        for f in animation:
            self._named_animations[animationName].append(
                {
                    'image': pg.transform.scale(pg.image.load(f['path']), (self.width, self.height)).convert_alpha(),
                    'duration': f['duration']
                }
            )

    def PlayAnimationOnce(self, animationName):
        if self._animationName == animationName:
            return
        self._animatedIndex = 0
        self._lastAnimationChanged = pg.time.get_ticks()
        self._animationName = animationName

    def setMaxSpeed(self, val):
        self.maxSpeed = val

    def setFlip(self, xbool, ybool):
        pass
        #for animationName in enumerate(self._named_animations):
        #    for Frame in enumerate(animationName):
        #        print(Frame)
        #Frame['image'] = pg.transform.flip(Frame['image'], xbool, ybool)
        #for x in animationName:
        #x['image'] = pg.transform.flip(x['image'], xbool, ybool)

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

    def setAnimationIdle(self, animationName):
        self._animationIdleName = animationName

    def update(self):

        # Animation Images

        frameIndex = self._animatedIndex % len(self._named_animations[self._animationName])
        frameDuration = self._named_animations[self._animationName][frameIndex]['duration']
        if pg.time.get_ticks() - self._lastAnimationChanged > frameDuration:

            frameImage = self._named_animations[self._animationName][frameIndex]['image']
            self.image = frameImage

            if frameIndex == len(self._named_animations[self._animationName]) - 1:
                self._animationName = self._animationIdleName

            self._animatedIndex += 1
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
