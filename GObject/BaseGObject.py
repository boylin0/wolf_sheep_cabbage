import pygame as pg

from Utils.Utils import clamp


class BaseGObject(object):
    def __init__(self, animatedList, resizeRate, x, y):
        #pg.sprite.Sprite.__init__(self)

        # Set image size
        self._set_image(pg.image.load(animatedList[0]['path']))
        self.width = (int)(self.image.get_width() * resizeRate)
        self.height = (int)(self.image.get_height() * resizeRate)
        self._original_x = x
        self._original_y = y
        self._original_width = self.width
        self._original_height = self.height

        # Load images for animating
        self._animation_all = {}
        self._animation_default_name = 'Idle'

        self._animation_all['Idle'] = []
        for frame_info in animatedList:
            frame = {
                'image': pg.transform.scale(pg.image.load(frame_info['path']), (self.width, self.height)).convert_alpha(),
                'duration': frame_info['duration']
            }
            self._animation_all['Idle'].append(frame)

        # Load Named Animation
        self._set_image(self._animation_all['Idle'][0]['image'])
        self._animation_name = self._animation_default_name
        self._animated_index = 0
        self._lastAnimationChanged = pg.time.get_ticks()
        

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
        self._animation_all[animationName] = []
        for f in animation:
            self._animation_all[animationName].append(
                {
                    'image': pg.transform.scale(pg.image.load(f['path']), (self.width, self.height)).convert_alpha(),
                    'duration': f['duration']
                }
            )

    def SetDefaultAnimation(self, animationName):
        self._animation_default_name = animationName

    def PlayAnimation(self, animationName):
        if self._animation_name == animationName:
            return
        self._animated_index = 0
        self._lastAnimationChanged = pg.time.get_ticks()
        self._animation_name = animationName

    def SetMaxSpeed(self, val):
        self.maxSpeed = val

    def SetFlip(self, xbool, ybool):
        pass

    def SetPos(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self._target_pos_x = self.x
        self._target_pos_y = self.y
        self.rect = pg.Rect(self.x, self.y, self.image.get_width(),
                            self.image.get_height())

    def Move(self, move):
        self.isMoving = True
        self._target_pos_x = move[0]
        self._target_pos_y = move[1]

    def Update(self):

        # Animation Images
        frameIndex = self._animated_index % len(
            self._animation_all[self._animation_name])
        frameDuration = self._animation_all[self._animation_name][frameIndex]['duration']

        if pg.time.get_ticks() - self._lastAnimationChanged > frameDuration:
            # Img
            frameImage = self._animation_all[self._animation_name][frameIndex]['image']
            self._set_image(frameImage)

            if frameIndex == len(self._animation_all[self._animation_name]) - 1:
                self._animation_name = self._animation_default_name

            self._animated_index += 1
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
    
    def Draw(self, surface):
        surface.blit(self.image, self.rect)

    def Clicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        else:
            return False

    def _set_image(self, img):
        self.image = img
        self._original_image = self.image
    