import pygame
import sys
import random
import time
from character import Character
from circle_enemy import CircleEnemy
from level import Level

# Initialize Pygame
pygame.init()

# Window dimensions
width, height = 1000, 800

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agony Arcade")

# Create a Level instance
level = Level(width, height, 1)
level.generate_level()

# Generate enemies in valid positions
num_enemies = 3
enemies = []

for _ in range(num_enemies):
    valid_position = False
    while not valid_position:
        x = random.randint(0, width)
        y = random.randint(0, height)

        if not level.is_wall_collision(x, y):
            valid_position = True

    enemies.append(CircleEnemy(x, y, 5))

# Create a Character instance
ball = Character(100, 100, 5)

if level.maze_type == 1:
    ball.set_position(100, 100)
elif level.maze_type == 2:
    ball.set_position(100, 100)
elif level.maze_type == 3:
    ball.set_position(100, 100)

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    ball.move(keys, level.maze_walls)

    # Move and check collisions for each enemy
    for enemy in enemies:
        enemy.move(ball, level)

    # Check collisions after all enemies have moved
    collision = any(enemy.check_collision(ball) for enemy in enemies)
    if collision:
        time.sleep(0.3)
        sys.exit()
    else:
        screen.fill((255, 255, 255))  # Fill the screen with white color

    # Draw character
    ball.draw(screen)
    
    # Draw the level
    level.draw(screen)

    # Draw and update all enemies
    for enemy in enemies:
        enemy.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the update speed
    pygame.time.Clock().tick(60)
