import random
from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    """Asteroid that moves through space and can split into smaller asteroids when hit.
    
    Asteroids have circular collision detection and physics-based movement.
    """
    def __init__(self, x, y, radius):
        """Initialize an asteroid.
        
        Args:
            x: Initial x position
            y: Initial y position
            radius: Size of the asteroid
        """
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw the asteroid as a circle on the screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        """Update asteroid position based on velocity.
        
        Args:
            dt: Delta time for frame-rate independent movement
        """
        self.position += self.velocity * dt

    def split(self):
        """Split the asteroid into two smaller asteroids when hit.
        
        If the asteroid is already at minimum size, it is simply destroyed.
        Larger asteroids split into two smaller ones with slightly different trajectories.
        """
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2
