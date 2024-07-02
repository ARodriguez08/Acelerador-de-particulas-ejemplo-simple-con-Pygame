import pygame
import random
import math
from settings import *

class Particle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(2, 5)
    
    def move(self, width, height):
        # Movimiento circular
        center_x, center_y = width // 2, height // 2
        radius = min(width, height) // 3
        self.angle += self.speed / radius
        self.x = center_x + radius * math.cos(self.angle)
        self.y = center_y + radius * math.sin(self.angle)

        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.angle = math.pi - self.angle
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.angle = -self.angle

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def check_tunnel(self, tunnels):
        for tunnel in tunnels:
            if tunnel.collidepoint(self.x, self.y):
                self.speed *= 1.1

class OppositeParticle(Particle):
    def move(self, width, height):
        # Movimiento circular en dirección opuesta
        center_x, center_y = width // 2, height // 2
        radius = min(width, height) // 3
        self.angle -= self.speed / radius
        self.x = center_x + radius * math.cos(self.angle)
        self.y = center_y + radius * math.sin(self.angle)

        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.angle = math.pi - self.angle
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.angle = -self.angle
