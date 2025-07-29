import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    window = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
        
        pygame.Surface.fill(window,(0,0,0))
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
