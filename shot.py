import pygame
from constants import *
from circleshape import CircleShape
import random

class Shot(CircleShape):
    containers = None
    
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        
        self.velocity = velocity
        
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        # self.wrap_around_screen()      
        