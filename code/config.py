import pygame
pygame.init()

# Posición Totoro
pos = [510, 150]

# Animación de Totoro estando quieto
totoro_movimiento = [
    pygame.image.load("../multimedia/img/totoro_img/enemy.png").convert_alpha(),
    pygame.image.load("../multimedia/img/totoro_img/enemy_peque.png").convert_alpha()
]