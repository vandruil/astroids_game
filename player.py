import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    """A player-controlled spaceship that can move and rotate."""

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        """
        Initialize a new player at the given position.

        Args:
            x (int): Starting x coordinate
            y (int): Starting y coordinate
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(
        self,
        screen: pygame.Surface,
    ):
        """
        Draw the player as a white triangle on the screen.

        Args:
        screen (pygame.Surface): The surface to draw the player on
        """
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)
