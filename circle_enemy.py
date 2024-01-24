import pygame
import math
from enemy import Enemy

class CircleEnemy(Enemy):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, (255, 255, 0))  # Yellow color for circles
        self.speed = 3

    def move(self, character, level):
        angle = math.atan2(character.y - self.y, character.x - self.x)
        new_x = self.x + self.speed * math.cos(angle)
        new_y = self.y + self.speed * math.sin(angle)

        # Verify collision with wall
        if not level.is_wall_collision(new_x, new_y):
            self.x = new_x
            self.y = new_y
            
    def check_collision(self, character):
        distance = math.sqrt((character.x - self.x)**2 + (character.y - self.y)**2)
        if distance < self.radius + character.radius:
            return True
        return False
