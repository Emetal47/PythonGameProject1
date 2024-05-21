import pygame as pg
from classes.resources import Resources

# class Coin:
class Coin(pg.sprite.Sprite):
    def __init__(self):
        res = Resources()
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = res.load_image("coin", "coin_png.png",-1,0.2)

        self.rect.x = 1200
        self.rect.y = 500