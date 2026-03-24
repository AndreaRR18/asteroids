from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame
from shot import Shot

class Player(CircleShape):
    """Player spaceship that can rotate, move, and shoot.

    The player is represented as a triangle and can be controlled with keyboard inputs.
    """
    rotation = 0

    def __init__(self, x, y):
        """Initialize the player spaceship.

        Args:
            x: Initial x position
            y: Initial y position
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.shoot_timer = 0
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    def triangle(self):
        """Calculate the three points of the player's triangle shape.

        Returns:
            List of three pygame.Vector2 objects representing the triangle vertices
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5)
        forward_scaled = pygame.Vector2(forward * self.radius)
        a = self.position + forward_scaled
        b = self.position - forward_scaled - right
        c = self.position - forward_scaled + right
        return [a, b, c]

    def draw(self, screen):
        """Draw the player's triangle on the screen.

        Args:
            screen: Pygame surface to draw on
        """
        pygame.draw.polygon(screen, "white", self.triangle(), int(LINE_WIDTH))

    def rotate(self, dt):
        """Rotate the player by the given amount.

        Args:
            dt: Delta time for frame-rate independent rotation
        """
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        """Update player state based on keyboard input.

        Args:
            dt: Delta time for frame-rate independent movement
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shoot_timer += dt

    def move(self, dt):
        """Move the player in the current facing direction.

        Args:
            dt: Delta time for frame-rate independent movement
        """
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        "Fire a bullet from the player's current position and direction."
        if self.shoot_timer >= self.shoot_cooldown:
            self.shoot_timer = 0
            bullet = Shot(*self.position)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
