"""Game configuration constants.

This module contains all the configurable parameters for the Asteroids game,
including screen dimensions, object sizes, speeds, and game mechanics settings.
"""

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Player configuration
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300  # degrees per second
PLAYER_SPEED = 200  # pixels per second
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
PLAYER_SHOT_SPEED = 500  # pixels per second

# Asteroid configuration
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3  # number of different asteroid sizes
ASTEROID_SPAWN_RATE_SECONDS = 0.8  # time between asteroid spawns
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# Shot configuration
SHOT_RADIUS = 5

# Visual configuration
LINE_WIDTH = 2
