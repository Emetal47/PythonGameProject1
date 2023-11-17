import pygame as pg
from classes.resources import Resources

# class Player:
class Player(pg.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self):
        res = Resources()

        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = res.load_image("Sprite Template Front.png", -1)
        self.speed = 5  # Speed of movement

        self.rect.x = 590
        self.rect.y = 200

   # def update(self):
   #     """move the fist based on the mouse position"""
   #     pos = pg.mouse.get_pos()
   #     self.rect.topleft = pos
   #     self.rect.move_ip(self.fist_offset)
   #     if self.punching:
   #         self.rect.move_ip(15, 25)
#
   # def punch(self, target):
   #     """returns true if the fist collides with the target"""
   #     if not self.punching:
   #         self.punching = True
   #         hitbox = self.rect.inflate(-5, -5)
   #         return hitbox.colliderect(target.rect)
#
   # def unpunch(self):
   #     """called to pull the fist back"""
   #     self.punching = False