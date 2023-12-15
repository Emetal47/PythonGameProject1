import pygame as pg
from classes.resources import Resources

# class Player:
class Player(pg.sprite.Sprite):
   """moves a clenched fist on the screen, following the mouse"""

   def __init__(self):
        res = Resources()
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = res.load_image("player", "Sprite Template Front.png", -1)
        self.speed = 5  # Speed of movement

        self.rect.x = 960
        self.rect.y = 540

   def input(self):
      keys2 = pg.KEYUP
      keys = pg.key.get_pressed()
      if keys[pg.K_a]:
         self.rect.x -= self.speed
         self.leftWalk(self.rect.x, self.rect.y)
      elif keys[pg.K_d]:
         self.rect.x += self.speed
         self.rightWalk(self.rect.x, self.rect.y)
      elif keys[pg.K_w]:
         self.rect.y -= self.speed
         self.upWalk(self.rect.x, self.rect.y)
      elif keys[pg.K_s]:
         self.rect.y += self.speed
         self.downWalk(self.rect.x, self.rect.y)
      elif keys2:
         self.defaultPose(self.rect.x, self.rect.y)

   def leftWalk(self, x, y):
      res = Resources()
      self.image, self.rect = res.load_image("player", "Sprite Template Left Walk.png", -1)

      self.rect.x = x 
      self.rect.y = y

   def defaultPose(self, x, y):
      res = Resources()
      self.image, self.rect = res.load_image("player", "Sprite Template Front.png", -1)

      self.rect.x = x
      self.rect.y = y

   def rightWalk(self, x, y):
      res = Resources()
      self.image, self.rect = res.load_image("player", "Sprite Template Right Walk.png", -1)

      self.rect.x = x
      self.rect.y = y

   def upWalk(self, x, y):
      res = Resources()
      self.image, self.rect = res.load_image("player", "Sprite Template Back.png", -1)

      self.rect.x = x
      self.rect.y = y

   def downWalk(self, x, y):
      res = Resources()
      self.image, self.rect = res.load_image("player", "Sprite Template Front.png", -1)

      self.rect.x = x
      self.rect.y = y

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