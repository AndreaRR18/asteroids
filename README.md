# Asteroids Game

A classic Asteroids clone built with Pygame.

## Features

- Player Control: Rotate and thrust your spaceship
- Shooting Mechanics: Fire bullets to destroy asteroids
- Asteroid Physics: Realistic movement and splitting
- Collision Detection: Circle-based collision system
- Game Logging: State and event logging

## Game Controls

- W: Thrust forward
- A: Rotate counter-clockwise
- D: Rotate clockwise
- S: Reverse thrust
- SPACE: Fire bullet
- ESC/Close Window: Quit game

## Installation

### Prerequisites
- Python 3.8+
- Pygame library

### Setup



## Project Structure

- main.py: Main game entry point
- player.py: Player spaceship logic
- asteroid.py: Asteroid behavior
- asteroidfield.py: Asteroid spawning
- shot.py: Bullet behavior
- circleshape.py: Base class
- constants.py: Game configuration
- logger.py: Game logging

## Architecture

The game uses an object-oriented approach with CircleShape as the base class for all game objects. The main game loop handles input, updates, collisions, and rendering.

## Development

To add new features, extend CircleShape and add objects to the appropriate sprite groups.
