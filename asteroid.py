import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    containers = None
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        
        angle = random.uniform(0, 360)
        self.velocity = pygame.Vector2(1, 0).rotate(angle) * random.randint(100, 600)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        # self.wrap_around_screen()
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_ateroid1_vector = self.velocity.rotate(angle)
        new_asteroid2_vector = self.velocity.rotate(-angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid1.velocity = new_ateroid1_vector * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid2.velocity = new_asteroid2_vector * 1.2
    