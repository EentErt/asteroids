# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()


    clock = pygame.time.Clock()
    dt = 0  # delta time
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create and assign groups for the player and asteroids 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # create the player
    player = Player( 
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT / 2,
        PLAYER_RADIUS,
    )

    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        # create the screen
        screen.fill((0, 0, 0))

        # update and draw objects
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)  

        # check for collisions
        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print("Game over!")
                return


        # enable closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000.0  # convert milliseconds to seconds
        
        
        pygame.display.flip()



if __name__ == "__main__":
    main()