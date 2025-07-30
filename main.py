import pygame

from Asteroid import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)  # pyright: ignore[reportAttributeAccessIssue]
    Player.containers = (updatable, drawable)  # pyright: ignore[reportAttributeAccessIssue]
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)  # noqa: F841
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        pygame.Surface.fill(screen, (0, 0, 0))
        updatable.update(dt)
        for sprite in updatable:
            sprite.draw(screen)

        pygame.display.flip()

        # print(clock.get_fps())


if __name__ == "__main__":
    main()
