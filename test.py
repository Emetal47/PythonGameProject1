# import os
# import pygame as pg

# # Set up directories
# main_dir = os.path.split(os.path.abspath(__file__))[0]
# data_dir = os.path.join(main_dir, "data")

# # Define load_image function
# def load_image(name, colorkey=None, scale=1):
#     fullname = os.path.join(data_dir, name)
#     image = pg.image.load(fullname).convert_alpha()
#     image = pg.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
#     if colorkey is not None:
#         if colorkey == -1:
#             colorkey = image.get_at((0, 0))
#         image.set_colorkey(colorkey, pg.RLEACCEL)
#     return image, image.get_rect()

# class Sprite(pg.sprite.Sprite):
#     def __init__(self):
#         pg.sprite.Sprite.__init__(self)
#         self.image, self.rect = load_image("Sprite Template Front.png", -1)
#         self.speed = 5  # Speed of movement

# def main():
#     pg.init()  # Initialize Pygame
#     screen = pg.display.set_mode((800, 600))  # Create a window
#     pg.display.set_caption("Sprite Movement")  # Set window title

#     all_sprites = pg.sprite.Group()
#     sprite = Sprite()
#     all_sprites.add(sprite)

#     clock = pg.time.Clock()

#     running = True
#     while running:
#         clock.tick(60)

#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 running = False

#         keys = pg.key.get_pressed()
#         if keys[pg.K_LEFT]:
#             sprite.rect.x -= sprite.speed
#         elif keys[pg.K_RIGHT]:
#             sprite.rect.x += sprite.speed
#         elif keys[pg.K_UP]:
#             sprite.rect.y -= sprite.speed
#         elif keys[pg.K_DOWN]:
#             sprite.rect.y += sprite.speed

#         screen.fill((255, 255, 255))  # Clear the screen
#         all_sprites.draw(screen)  # Draw the sprite
#         pg.display.flip()  # Update the display

#     pg.quit()

# if __name__ == "__main__":
#     main()
