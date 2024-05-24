# from pantalla import *
import pygame
pygame.init()
from pygame.sprite import Sprite

# Animación de Totoro estando quieto
totoro_movimiento = [
    pygame.image.load("../multimedia/img/totoro_img/enemy.png").convert_alpha(),
    pygame.image.load("../multimedia/img/totoro_img/enemy_peque.png").convert_alpha()
]

class Enemy(Sprite):
    def __init__(self, image_list, pos , animation_time):
        self.vidas = 10

        self.images_animation = image_list
        self.current_image = 0
        self.personaje_imagen = self.images_animation[self.current_image]
        self.rect = self.personaje_imagen.get_rect()

        self.rect.move_ip(pos)
        
        self.animation_time = animation_time  # Tiempo en milisegundos para cambiar la imagen
        self.last_update = pygame.time.get_ticks()
        
        self.contador = 0
        
    def animacion(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > self.animation_time:
            self.last_update = now
        
            self.contador = (self.contador + 1) % len(self.images_animation)
            self.personaje_imagen = self.images_animation[self.contador]
            self.rect = self.personaje_imagen.get_rect(topleft=self.rect.topleft)
    
    def draw(self, screen):
        screen.blit(self.personaje_imagen, self.rect)