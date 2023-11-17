import os
import pygame as pg

class Resources():

    # Resource handlers
    if not pg.font:
        print("Fonts Disabled")
    if not pg.mixer:
        print("Sound Disabled")

    
    def load_image(self, name, colorkey=None, scale=1):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        main_dir = main_dir.replace("classes", "")
        data_dir = os.path.join(main_dir, "data")
        fullname = os.path.join(data_dir, name)

        image = pg.image.load(fullname)

        size = image.get_size()
        size = (size[0] * scale, size[1] * scale)
        image = pg.transform.scale(image, size)

        image = image.convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        return image, image.get_rect()


    def load_sound(name):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        data_dir = os.path.join(main_dir, "data")

        class NoneSound:
            def play(self):
                pass

        if not pg.mixer or not pg.mixer.get_init():
            return NoneSound()

        fullname = os.path.join(data_dir, name)
        sound = pg.mixer.Sound(fullname)

        return sound