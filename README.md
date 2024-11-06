# Snake Game

## Overview

The Snake Game is a classic arcade game implemented in Python using the Turtle graphics library. Players control a snake that grows in length as it eats food while avoiding collisions with the walls and its own tail.

## Features

- **User Controls**: Navigate the snake using the arrow keys (Up, Down, Left, Right).
- **Food Mechanics**: The snake grows longer each time it eats food, and the food randomly refreshes.
- **Collision Detection**: The game detects collisions with the wall and the snake's tail, resetting the game when a collision occurs.
- **Scoreboard**: Keeps track of the player's score, which increases as the snake eats food.

## Prerequisites

- Python 3.x
- `turtle` module (included with standard Python installation)

## Code Structure
- snake.py: Contains the Snake class, which handles the snake's movement, growth, and collision detection.
- food.py: Contains the Food class, responsible for generating food at random positions on the screen.
- scoreboard.py: Contains the Scoreboard class, which manages the display and updating of the player's score.
- main.py: The main file that sets up the game window, listens for user input, and runs the game loop.

## Controls
- Arrow Up: Move the snake up
- Arrow Down: Move the snake down
- Arrow Left: Move the snake left
- Arrow Right: Move the snake right