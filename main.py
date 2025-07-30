import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)  # pyright: ignore[reportAttributeAccessIssue]
    AsteroidField.containers = (updatable,)  # pyright: ignore[reportAttributeAccessIssue]

    asteroid_field = AsteroidField()  # noqa: F841
    Shot.containers = (shots, updatable, drawable)  # pyright: ignore[reportAttributeAccessIssue]
    Player.containers = (updatable, drawable)  # pyright: ignore[reportAttributeAccessIssue]

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)  # noqa: F841

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        screen.fill("black")

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collision(player):
                sys.exit("GAME OVER")
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # print(clock.get_fps())


if __name__ == "__main__":
    main()
