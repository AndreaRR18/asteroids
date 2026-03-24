import pygame
import random
from asteroid import Asteroid
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE_SECONDS,
    ASTEROID_MAX_RADIUS,
)


class AsteroidField(pygame.sprite.Sprite):
    """Manages the spawning of asteroids at the edges of the screen.
    
    The AsteroidField is responsible for creating new asteroids that enter the game
    from random screen edges with random velocities and sizes.
    """
    containers: pygame.sprite.Group
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self, groups: pygame.sprite.Group):
        """Initialize the asteroid field.
        
        Args:
            groups: Pygame sprite group to add this field to
        """
        pygame.sprite.Sprite.__init__(self, groups)
        self.containers = groups
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """Create a new asteroid at the specified position with given velocity.
        
        Args:
            radius: Size of the asteroid to spawn
            position: Initial position of the asteroid
            velocity: Initial velocity vector of the asteroid
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        # Add the asteroid to its containers
        for container in Asteroid.containers:
            container.add(asteroid)

    def update(self, dt):
        """Update the asteroid field, spawning new asteroids when needed.
        
        Args:
            dt: Delta time for frame-rate independent timing
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE_SECONDS:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
