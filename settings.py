import pygame
import random

# Configuración de pantalla inicial
INITIAL_WIDTH = 800
INITIAL_HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK_HOLE_COLOR = (0, 0, 0)
COLORS = [pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(100)]

# Umbral de velocidad para colisión
COLLISION_SPEED_THRESHOLD = 10

# Radio del agujero negro
BLACK_HOLE_RADIUS = 50
