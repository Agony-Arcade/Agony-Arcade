import pygame
import math
from enemy import Enemy

class CircleEnemy(Enemy):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, (255, 255, 0))  # Yellow color for circles
        self.speed = 3
        
    def draw(self, screen, camera_offset_x=0, camera_offset_y=0):
        pygame.draw.circle(screen, self.color, (int(self.x + camera_offset_x), int(self.y + camera_offset_y)), self.radius)

    def move(self, character, level):
        # Calcular el ángulo hacia el personaje
        angle = math.atan2(character.y - self.y, character.x - self.x)

        # Calcular el movimiento propuesto
        move_x = self.speed * math.cos(angle)
        move_y = self.speed * math.sin(angle)

        # Probar movimiento horizontal y ajustar si hay colisión
        if not level.is_wall_collision(self.x + move_x, self.y):
            self.x += move_x
        else:
            # Intentar moverse verticalmente en lugar de horizontalmente
            if not level.is_wall_collision(self.x, self.y + self.speed):
                self.y += self.speed
            elif not level.is_wall_collision(self.x, self.y - self.speed):
                self.y -= self.speed

        # Probar movimiento vertical y ajustar si hay colisión
        if not level.is_wall_collision(self.x, self.y + move_y):
            self.y += move_y
        else:
            # Intentar moverse horizontalmente en lugar de verticalmente
            if not level.is_wall_collision(self.x + self.speed, self.y):
                self.x += self.speed
            elif not level.is_wall_collision(self.x - self.speed, self.y):
                self.x -= self.speed

    def check_collision(self, character):
        distance = math.sqrt((character.x - self.x)**2 + (character.y - self.y)**2)
        if distance < self.radius + character.radius:
            return True
        return False

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
