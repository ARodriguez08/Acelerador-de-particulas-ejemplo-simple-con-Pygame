import pygame
import random
import math
from particle import Particle, OppositeParticle
from settings import *

def create_tunnels(width, height):
    tunnel_width, tunnel_height = width // 8, height // 8
    return [
        pygame.Rect(width // 4 - tunnel_width // 2, height // 4 - tunnel_height // 2, tunnel_width, tunnel_height),
        pygame.Rect(3 * width // 4 - tunnel_width // 2, height // 4 - tunnel_height // 2, tunnel_width, tunnel_height),
        pygame.Rect(width // 4 - tunnel_width // 2, 3 * height // 4 - tunnel_height // 2, tunnel_width, tunnel_height),
        pygame.Rect(3 * width // 4 - tunnel_width // 2, 3 * height // 4 - tunnel_height // 2, tunnel_width, tunnel_height)
    ]

def check_collision(particle1, particle2):
    dx = particle1.x - particle2.x
    dy = particle1.y - particle2.y
    distance = (dx ** 2 + dy ** 2) ** 0.5
    return distance < particle1.radius + particle2.radius

def main():
    # Inicializar Pygame
    pygame.init()

    # Configurar la pantalla
    width, height = INITIAL_WIDTH, INITIAL_HEIGHT
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption("Acelerador de Partículas 2D")

    # Crear partículas
    particles = [
        Particle(width // 2, height // 2 - 100, 10, RED),
        OppositeParticle(width // 2, height // 2 + 100, 10, BLUE)
    ]
    
    # Crear túneles iniciales
    tunnels = create_tunnels(width, height)

    # Bucle principal
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                tunnels = create_tunnels(width, height)

        screen.fill(BLACK)

        for tunnel in tunnels:
            pygame.draw.rect(screen, WHITE, tunnel)

        # Verificar colisiones y crear agujero negro si es necesario
        create_black_hole = False
        if check_collision(particles[0], particles[1]) and particles[0].speed > COLLISION_SPEED_THRESHOLD and particles[1].speed > COLLISION_SPEED_THRESHOLD:
            create_black_hole = True
            black_hole_x, black_hole_y = (particles[0].x + particles[1].x) / 2, (particles[0].y + particles[1].y) / 2

        if create_black_hole:
            pygame.draw.circle(screen, BLACK_HOLE_COLOR, (int(black_hole_x), int(black_hole_y)), BLACK_HOLE_RADIUS)
            for particle in particles:
                dx = black_hole_x - particle.x
                dy = black_hole_y - particle.y
                distance = (dx ** 2 + dy ** 2) ** 0.5
                if distance < BLACK_HOLE_RADIUS:
                    particles.remove(particle)

            if len(particles) == 0:
                font = pygame.font.Font(None, 74)
                text = font.render("Simulación Terminada", True, WHITE)
                screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

        for particle in particles:
            particle.move(width, height)
            particle.check_tunnel(tunnels)
            particle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
