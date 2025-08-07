import pygame
from constants import *
from player import *
from asteroids import *
from  asteroidfield import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,drawable,updatable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2, PLAYER_RADIUS)
    my_astrofield = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        #player.draw(screen)
        for something in drawable:
            something.draw(screen)
        pygame.display.flip()
        delta_time_inmilli = clock.tick(60)
        dt = delta_time_inmilli / 1000
        #player.update(dt)
        for something in updatable:
            something.update(dt)
        for astro in asteroids:
            if player.check_collision(astro):
                print("game over")
                return
        




if __name__ == "__main__":
    main()
