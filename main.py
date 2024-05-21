# import modules
import pygame as pg
import random
# import classes
from classes.player import Player
from classes.coin import Coin
from classes.resources import Resources

WIDTH = 1920
HEIGHT = 1080

def main():
    # initialize everything
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.SCALED)
    pg.display.set_caption("Game Project 1")
    pg.mouse.set_visible(False)

    # create the background
    background = pg.Surface(screen.get_size())
    background = pg.image.load("data/backgrounds/ground.png").convert()

    #background = pg.Surface(screen.get_size())
    #background = background.convert()
    #background.fill((170, 238, 187))

    # put text on background
    #if pg.font:
        #font = pg.font.Font(None, 64)
        #text = font.render("Game", True, (10, 10, 10))
        # Look for code to make text disappear after amount of time
        #textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        #background.blit(text, textpos)

    # display background
    #screen.blit(background, (0, 0))
    #pg.display.flip()

    # Load background music
    music = Resources()
    #music.load_music('MyBrothersWife.mp3')

    #define colours
    BG = (50, 50, 50)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    class Camera(pg.sprite.Group):
        def __init__(self):
            super().__init__()
            self.offset = pg.math.Vector2()
            self.floor_rect = background.get_rect(topleft=(0, 0))

        def custom_draw(self):
            self.offset.x = pl_sprite.rect.centerx - WIDTH // 2
            self.offset.y = pl_sprite.rect.centery - HEIGHT // 2

            # draw the floor
            floor_offset_pos = self.floor_rect.topleft - self.offset
            screen.blit(background, floor_offset_pos)

            for sprite in all_sprites:
                offset_pos = sprite.rect.topleft - self.offset
                screen.blit(sprite.image, offset_pos)

    # Prepare Game Objects
    camera = Camera()
    all_sprites = pg.sprite.Group()

    # player object
    pl_sprite = Player()
    player_mask = pg.mask.from_surface(pl_sprite.image)

    # coin object
    coin_sprite = Coin()
    coin_mask = pg.mask.from_surface(coin_sprite.image)

    all_sprites.add(pl_sprite)
    all_sprites.add(coin_sprite)

    # coin count text
    coin_count = 0
    counter_incremented = False
    font = pg.font.Font(None, 64)

    clock = pg.time.Clock()

    # Main Loop
    going = True


    while going:
        clock.tick(60)

        #check mask overlap
        if player_mask.overlap(coin_mask, (coin_sprite.rect.x - pl_sprite.rect.x, coin_sprite.rect.y - pl_sprite.rect.y)):
            all_sprites.remove(coin_sprite)
            if not counter_incremented:
                coin_count += 1
                counter_incremented = True 

         # Convert the counter to a string
        text_to_display = str(coin_count)
        text = font.render(text_to_display, True, (255, 215, 0))

        background.fill((0, 0, 0), (100, 50, text.get_width(), text.get_height())) 
        background.blit(text, (100, 50))
        pg.display.flip()

        
        #draw rectangle
        #coin_rect.fill(col)
        #background.blit(bullet, coin_sprite.rect)

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
        # pl_sprite.input()

        # Draw Everything
        #screen.blit(background, (0, 0))
        camera.custom_draw()
        all_sprites.update()
        #all_sprites.draw(screen)
        pg.display.update()

    pg.quit()


if __name__ == "__main__":
    main()



