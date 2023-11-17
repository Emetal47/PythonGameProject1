# import modules
import pygame as pg

# import classes
from classes.player import Player

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

    #put text on background
    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("Game", True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

    # display background
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Prepare Game Objects
    all_sprites = pg.sprite.Group()
    sprite = Player()
    all_sprites.add(sprite)

    clock = pg.time.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pg.event.get():
           if event.type == pg.QUIT:
                going = False

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            sprite.rect.x -= sprite.speed
        elif keys[pg.K_d]:
            sprite.rect.x += sprite.speed
        elif keys[pg.K_w]:
            sprite.rect.y -= sprite.speed
        elif keys[pg.K_s]:
            sprite.rect.y += sprite.speed


        # Draw Everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
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
