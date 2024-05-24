import pygame
import random
from pantalla import ancho_pantalla , alto_pantalla
from config import *

from pygame.sprite import Sprite

pygame.init()

#Arreglos para controlar la cant de pets
bats_array = []

#Animaciones de pets
bat_movimiento = [
    pygame.image.load("../multimedia/img/pets/bat/bat_uno.png").convert_alpha(),
    pygame.image.load("../multimedia/img/pets/bat/bat_dos.png").convert_alpha(),
    pygame.image.load("../multimedia/img/pets/bat/bat_tres.png").convert_alpha()
]

#Clases de los pets
class Bat(Sprite):
    def __init__(self , bat_animation , animation_time , bats):
        self.vida = 1

        self.images_animation = bat_animation
        self.current_image = 0
        self.personaje_imagen = self.images_animation[self.current_image]
        self.rect = self.personaje_imagen.get_rect()
        self.rect.y = random.randrange(alto_pantalla - self.rect.height)
        self.rect.x = 680
        
        self.animation_time = animation_time  # Tiempo en milisegundos para cambiar la imagen
        self.last_update = pygame.time.get_ticks()
        
        self.contador = 0
        self.bats_array = bats

        self.velocidad_x = 3

    def animacion(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > self.animation_time:
            self.last_update = now
        
            self.contador = (self.contador + 1) % len(self.images_animation)
            self.personaje_imagen = self.images_animation[self.contador]
            self.rect = self.personaje_imagen.get_rect(topleft=self.rect.topleft)
    
    def draw(self, screen):
        screen.blit(self.personaje_imagen, self.rect)

    def mover(self):
        self.rect.x -= self.velocidad_x

    def delete(self , delete_bat):
        if self.rect.left <= 0:
            self.bats_array.remove(delete_bat)


#Funciones
def add_array(array , pet):
    if random.randint(0 , 100) % 10 == 0 and len(array) < 2:
        array.append(pet)