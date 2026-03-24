import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """Base class for all circular game objects.
    
    CircleShape provides common functionality for game objects including:
    - Position and velocity management
    - Basic sprite functionality
    - Circle-based collision detection
    - Container management for sprite groups
    """
    containers: tuple = ()

    def __init__(self, x, y, radius):
        """Initialize a circular game object.
        
        Args:
            x: Initial x position
            y: Initial y position
            radius: Size of the circular object
        """
        super().__init__(*self.containers)

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen):
        """Draw the object on the screen.
        
        Args:
            screen: Pygame surface to draw on
        
        Note:
            This method must be overridden by subclasses.
        """
        # must override
        pass

    def update(self, dt):
        """Update the object state.
        
        Args:
            dt: Delta time for frame-rate independent updates
        
        Note:
            This method must be overridden by subclasses.
        """
        # must override
        pass

    def collides(self, other):
        """Check collision with another CircleShape instance.
        
        Args:
            other: Another CircleShape object to check collision with
        
        Returns:
            bool: True if objects are colliding, False otherwise
        """
        # Check collision with a single CircleShape instance
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
