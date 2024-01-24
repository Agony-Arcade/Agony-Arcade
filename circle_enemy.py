import pygame
import math
from enemy import Enemy

class CircleEnemy(Enemy):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, (255, 255, 0))  # Yellow color for circles
        self.speed = 3

    def move(self, character):
        angle = math.atan2(character.y - self.y, character.x - self.x)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)

    def check_collision(self, character):
        distance = math.sqrt((character.x - self.x)**2 + (character.y - self.y)**2)
        if distance < self.radius + character.radius:
            return True
        return False
