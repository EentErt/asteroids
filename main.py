# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()


    clock = pygame.time.Clock()
    dt = 0  # delta time
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player_character = Player( 
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT / 2,
        PLAYER_RADIUS,
    )

    while True:
        screen.fill((0, 0, 0))
        player_character.update(dt)
        player_character.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000.0  # convert milliseconds to seconds
        pygame.display.flip()



if __name__ == "__main__":
    main()