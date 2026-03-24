from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """Player bullet that moves in a straight line and can destroy asteroids.
    
    Shots are created when the player fires and move at high speed in the direction
    the player is facing. They are destroyed when they hit asteroids or go off-screen.
    """
    def __init__(self, x, y):
        """Initialize a shot at the given position.
        
        Args:
            x: Initial x position
            y: Initial y position
        """
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        """Draw the shot as a small circle on the screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """Update the shot position based on velocity.
        
        Args:
            dt: Delta time for frame-rate independent movement
        """
        self.position += self.velocity * dt
