from pantalla import *
import pygame
pygame.init()
from pygame.sprite import Sprite


class main_character(Sprite):
    def __init__(self):
        super().__init__()

        self.vidas = 3
        self.personaje_imagen = pygame.image.load("../multimedia/img/luffy_img/luffy.png").convert()
        self.personaje_imagen.set_colorkey([0 , 0 , 0]) #Quitar el fondo negro que pone pygame         
        self.rect = self.personaje_imagen.get_rect()
        self.rect.move_ip([10, 300])

    def dibujar(self):
        screen.blit(self.personaje_imagen, self.rect)  # Draw the image


class Enemy(Sprite):
    def __init__(self , images_array):
        super().__init__()

        self.vidas = 3
        self.personaje_imagen = pygame.image.load("../multimedia/img/totoro_img/enemy.png").convert()
        self.images_animation = images_array
        self.personaje_imagen.set_colorkey([0 , 0 , 0]) #Quitar el fondo negro que pone pygame         
        self.rect = self.personaje_imagen.get_rect()
        self.rect.move_ip([510, 150])
        self.contador = 0

    def animacion(self):
        self.contador = (self.contador + 1) % len(self.images_animation)
        self.personaje_imagen = self.images_animation[self.contador]

    def dibujar(self):
        screen.blit(self.personaje_imagen, self.rect)  # Draw the image
