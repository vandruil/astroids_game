import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        pygame.Surface.fill(screen, (0, 0, 0))
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()

        # print(clock.get_fps())


if __name__ == "__main__":
    main()
