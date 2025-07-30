import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    window = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(window, (0, 0, 0))

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        print(clock.get_fps())


if __name__ == "__main__":
    main()
