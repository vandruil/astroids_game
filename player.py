import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


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
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  # pyright: ignore[reportArgumentType]

    def rotate(self, dt):
        """
        Rotate the Player on the screen.

        Args:
        dt : Delta Time

        """
        self.rotation += +(PLAYER_TURN_SPEED * dt)
        self.rotation = (self.rotation % 360 + 360) % 360

    def update(self, dt):
        """ """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
