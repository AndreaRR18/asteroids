import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
import constants
from logger import log_event, log_state
from player import Player
from shot import Shot

def initialize_game():
    """Initialize pygame and create the game window."""
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    return screen

def setup_sprite_groups():
    """Create and configure sprite groups for game objects."""
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set up container relationships
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    
    return updatable, drawable, asteroids, shots

def create_game_objects(updatable):
    """Create initial game objects (player and asteroid field)."""
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    AsteroidField(updatable)
    return player

def handle_input():
    """Process pygame events and user input."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update_game_state(updatable, dt):
    """Update all game objects based on delta time."""
    updatable.update(dt)

def handle_collisions(player, asteroids, shots):
    """Detect and handle collisions between game objects."""
    for asteroid in asteroids:
        # Check player-asteroid collisions
        if player.collides(asteroid):
            log_event("player_hit")
            print("Game over!")
            sys.exit()

        # Check shot-asteroid collisions
        for shot in shots:
            if shot.collides(asteroid):
                log_event("asteroid_split")
                asteroid.split()
                shot.kill()

def render_game(screen, drawable, fill):
    """Render all game objects to the screen."""
    screen.fill(fill)
    for drawable_obj in drawable:
        drawable_obj.draw(screen)
    pygame.display.flip()

def main():
    """Main game function - initializes and runs the game loop."""
    # Initialize game systems
    screen = initialize_game()
    fill = (0, 0, 0)
    
    # Set up sprite groups
    updatable, drawable, asteroids, shots = setup_sprite_groups()
    
    # Create game objects
    player = create_game_objects(updatable)
    
    # Initialize clock
    clock = pygame.time.Clock()
    
    # Main game loop
    running = True
    while running:
        # Calculate delta time for frame-rate independent movement
        dt = clock.tick(60) / 1000.0
        
        # Process input
        running = handle_input()
        
        # Log game state
        log_state()
        
        # Update game objects
        update_game_state(updatable, dt)
        
        # Handle collisions
        handle_collisions(player, asteroids, shots)
        
        # Render the game
        render_game(screen, drawable, fill)

if __name__ == "__main__":
    main()
