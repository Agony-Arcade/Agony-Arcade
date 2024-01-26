import heapq

import pygame
import math
from enemy import Enemy
from pathfinding.finder.a_star import AStarFinder

class CircleEnemy(Enemy):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, (255, 255, 0))  # Yellow color for circles
        self.speed = 3
        self.path = []
        
    def draw(self, screen, camera_offset_x=0, camera_offset_y=0):
        pygame.draw.circle(screen, self.color, (int(self.x + camera_offset_x), int(self.y + camera_offset_y)), self.radius)

    def move(self, character, level):
        # Calcular el ángulo hacia el personaje
        angle = math.atan2(character.y - self.y, character.x - self.x)
        move_x = self.speed * math.cos(angle)
        move_y = self.speed * math.sin(angle)

        # Crear un rectángulo para el nuevo potencial lugar del enemigo
        new_rect = self.get_rect().move(move_x, move_y)

        # Si no hay colisión con la pared, mover directamente hacia el objetivo
        if not level.is_wall_collision_rect(new_rect):
            self.x += move_x
            self.y += move_y
        else:
            # Emitir rayos en diferentes direcciones para encontrar un camino libre
            for ray_angle in [math.pi / 4, -math.pi / 4, 3 * math.pi / 4,
                              -3 * math.pi / 4]:  # Rayos en 45°, 135°, 225° y 315°
                ray_x = self.speed * math.cos(angle + ray_angle)
                ray_y = self.speed * math.sin(angle + ray_angle)
                ray_rect = self.get_rect().move(ray_x, ray_y)

                # Si un rayo no colisiona con una pared, moverse en esa dirección
                if not level.is_wall_collision_rect(ray_rect):
                    self.x += ray_x
                    self.y += ray_y
                    break

    def check_collision(self, character):
        distance = math.sqrt((character.x - self.x)**2 + (character.y - self.y)**2)
        if distance < self.radius + character.radius:
            return True
        return False

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

    def heuristic(self, a, b):
        """ Calculate the Manhattan distance between two points """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(self, current, level):
        """ Return the accessible neighboring nodes for a given node """
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
        neighbors = []
        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if not level.is_wall_collision(nx, ny):  # Assuming a method 'is_wall' in Level class
                neighbors.append((nx, ny))
        return neighbors

    def a_star(self, goal, level):
        """ A* Pathfinding Algorithm """
        start = self.x, self.y
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}
        frontera = []
        heapq.heappush(frontera,
                       (self.heuristic(start, goal), start, []))

        while frontera:
            _, current, camino_actual = heapq.heappop(frontera)

            if current == goal:
                """"
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                """
                self.path = camino_actual[::-1] # Return reversed path
                print(self.path)
                return

            for neighbor in self.neighbors(current, level):
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    nuevo_camino = camino_actual + [neighbor]
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    if neighbor not in [item[1] for item in frontera]:
                        heapq.heappush(frontera, (f_score[neighbor], neighbor, nuevo_camino))

        self.path = None
        return

    def move_ai(self, character, level):
        # Moverse hacia el próximo punto en el camino si hay uno disponible
        if self.path:
            next_point = self.path[0]  # Obtener el primer punto del camino
            angle = math.atan2(next_point[1] - self.y, next_point[0] - self.x)

            move_x = self.speed * math.cos(angle)
            move_y = self.speed * math.sin(angle)

            new_rect = self.get_rect().move(move_x, move_y)

            # Si no hay colisión con la pared, moverse hacia el próximo punto
            if not level.is_wall_collision_rect(new_rect):
                self.x += move_x
                self.y += move_y
                self.path.pop(0)  # Eliminar el punto alcanzado del camino

            # Si no hay más puntos en el camino o si hay una colisión, puedes decidir si detenerte o hacer otra acción
            if not self.path or level.is_wall_collision_rect(new_rect):
                # Aquí puedes añadir lógica adicional si es necesario
                pass
        else:
            # Aquí puedes añadir lógica adicional si no hay un camino disponible
            pass

