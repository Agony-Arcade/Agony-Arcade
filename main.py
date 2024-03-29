import math

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

# Create a Character instance
ball = Character(100, 100, 5)
ball.set_position(100, 100)

# Camera variables
camera_x = 0
camera_y = 0

def generate_enemy_positions():
    enemy_positions = []
    min_distance = 300
    for _ in range(num_enemies):
        valid_position = False
        while not valid_position:
            x = random.randint(0, width)
            y = random.randint(0, height)

            if not level.is_wall_collision(x, y) and math.sqrt((ball.x - x)**2 + (ball.y - y)**2) > min_distance:
                valid_position = True

        enemy_positions.append((x, y))
    return enemy_positions

# Reset enemy positions with minimum distance
enemy_positions = generate_enemy_positions()

# Update enemy positions if the number of enemies matches
if len(enemies) == num_enemies:
    for i, pos in enumerate(enemy_positions):
        enemies[i].x = pos[0]
        enemies[i].y = pos[1]
else:
    # If the number of enemies has changed, recreate the entire enemies list
    enemies = [CircleEnemy(pos[0], pos[1], 5) for pos in enemy_positions]

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    ball.move(keys, level.maze_walls)

    # Check if the character is on the red zone
    if level.check_character_on_zone(ball.x, ball.y):
        if not level.maze_type == 3:
            level.maze_type += 1
            level.generate_level()

            # Reset enemy positions with minimum distance
            enemy_positions = generate_enemy_positions()
            for i, pos in enumerate(enemy_positions):
                enemies[i].x = pos[0]
                enemies[i].y = pos[1]

        ball.set_position(100, 100)

    # Calculate the camera offset based on the ball's position
    camera_offset_x = width // 2 - ball.x
    camera_offset_y = height // 2 - ball.y

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

    # Draw character with adjusted position based on camera offset
    ball.draw(screen, camera_offset_x, camera_offset_y)

    # Draw the level with adjusted position based on camera offset
    level.draw(screen, camera_offset_x, camera_offset_y)

    # Draw and update all enemies with adjusted position based on camera offset
    for enemy in enemies:
        enemy.draw(screen, camera_offset_x, camera_offset_y)

    # Update the display
    pygame.display.flip()

    # Control the update speed
    clock.tick(60)
