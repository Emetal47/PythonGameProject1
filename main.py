# Import Modules
import os
import pygame as pg

if not pg.font:
    print("Fonts Disabled")
if not pg.mixer:
    print("Sound Disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

# Resource handlers

def load_image(name, colorkey=None, scale=1):
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
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound


# classes for our game objects

# class Player:
class Sprite(pg.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("Sprite Template Front.png", -1)
        self.fist_offset = (-235, -80)
        self.punching = False

    def update(self):
        """move the fist based on the mouse position"""
        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        """returns true if the fist collides with the target"""
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """called to pull the fist back"""
        self.punching = False


def main():

    # initialize everything
    pg.init()
    screen = pg.display.set_mode((1280,600), pg.SCALED)
    pg.display.set_caption("Game Project 1")
    pg.mouse.set_visible(False)

    # create the background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    #put text on baclground
    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("Game", True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

    # display background
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Prepare Game Objects
    sprite = Sprite()
    allsprites = pg.sprite.RenderPlain((sprite))
    clock = pg.time.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False

        allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()



































# Example file showing a circle moving on screen
# import pygame

# pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True
# dt = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # for event in pygame.event.get():
        # if event.type == pygame.QUIT:
            # running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("black")

    # pygame.draw.circle(screen, "red", player_pos, 40)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
        # player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
        # player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
        # player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
        # player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    # pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    # dt = clock.tick(60) / 1000

# pygame.quit()
