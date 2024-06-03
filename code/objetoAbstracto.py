import pygame
pygame.init()

from pygame.sprite import Sprite
from abc import ABC, abstractmethod


#CLase abstracta para los pets
class Dad(ABC , Sprite):
    def __init__(self , animation , animation_time , pet):
        self.vida = 0

        self.images_animation = animation
        self.current_image = 0
        self.personaje_imagen = self.images_animation[self.current_image]
        self.rect = self.personaje_imagen.get_rect()
    
        self.animation_time = animation_time  # Tiempo en milisegundos para cambiar la imagen
        self.last_update = pygame.time.get_ticks()
        
        self.contador = 0
        self.bats_array = pet

    @abstractmethod
    def animacion(self):
        pass

    @abstractmethod
    def draw(self):
        pass
