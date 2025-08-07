import pygame
from constants import *
from player import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2, PLAYER_RADIUS)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #updatable = pygame.sprite.Group()
    #drawable = pygame.sprite.Group()
    #Player.containers = (updatable, drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        player.draw(screen)
        #drawable.draw(screen)
        pygame.display.flip()
        delta_time_inmilli = clock.tick(60)
        dt = delta_time_inmilli / 1000
        player.update(dt)
        #updatable.update(dt)




if __name__ == "__main__":
    main()
