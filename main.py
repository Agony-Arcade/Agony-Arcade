import pygame
import sys
import random
import time
import threading

import circle_enemy
from character import Character
from circle_enemy import CircleEnemy
from level import Level

def enemy_logic(enemy, character, level, update_interval):
    while True:
        start_time = time.time()

        # Lógica de a_star
        enemy.a_star((character.x, character.y), level)

        # Lógica de move_ai
        enemy.move_ai(character, level)

        # Esperar el intervalo de actualización
        time.sleep(max(0, update_interval - (time.time() - start_time)))
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
num_enemies = 1
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

# Camera variables
camera_x = 0
camera_y = 0

# Main loop
clock = pygame.time.Clock()
character_moved = False

update_interval = 1    # Actualizar el camino cada 0.5 segundos
last_update_time = 0
prev_x, prev_y = 0,0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    int_ball_x = int(ball.x)
    int_ball_y = int(ball.y)
    prev_x = int_ball_x
    prev_y = int_ball_y

    ball.move(keys, level.maze_walls)


    # Calculate the camera offset based on the ball's position
    camera_offset_x = width // 2 - ball.x
    camera_offset_y = height // 2 - ball.y
    character_moved = int_ball_x != prev_x or int_ball_y != prev_y
    # Move and check collisions for each enemy
    current_time = time.time()
    if current_time - last_update_time > update_interval:
        for enemy in enemies:
            enemy.a_star((ball.x, ball.y), level)
            print("AAAAAAAAAAAAAAA")
        last_update_time = current_time
    """
    for enemy in enemies:
        enemy.move_ai(ball, level)

    """
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
    pygame.time.Clock().tick(60)


