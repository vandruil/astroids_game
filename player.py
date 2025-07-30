import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    """A player-controlled spaceship that can move and rotate."""

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

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
        Rotate the Player on the screen

        Args:
            dt (float?): Delta Time

        """
        self.rotation += +(PLAYER_TURN_SPEED * dt)
        self.rotation = (self.rotation % 360 + 360) % 360

    def update(self, dt):
        """
        Reads the User Inputs to create movements or shoot

        Args:
            dt (float?): Delta Time

        """
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt
        self.shot_cooldown = max(self.shot_cooldown, 0)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown > 0:
                return
            self.shoot()
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(
        self,
    ):
        x, y = self.position
        new_shot = Shot(x, y)
        new_shot.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        )
