import pygame
import random
from pantalla import ancho_pantalla , alto_pantalla
from config import *
from pets_sprites import *
from abc import ABC, abstractmethod

from pygame.sprite import Sprite

pygame.init()

#CLase abstracta para los pets
class Pet(ABC , Sprite):
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

    @abstractmethod
    def mover(self):
       pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def appear(self):
        pass

#Clases de los pets
class Bat(Pet):
    def __init__(self , vida , animation , animation_time , pet):
        super().__init__(animation, animation_time, pet)
        self.vida = vida

        self.rect.y = random.randrange(alto_pantalla - self.rect.height)
        self.rect.x = 680
        
        # self.audio = pygame.mixer.Sound("../multimedia/audio/bat_sound.mp3")

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
        # self.audio.play()

    def delete(self , delete_bat):
        if self.rect.left <= 0:
            self.bats_array.remove(delete_bat)
    
    def appear(self , screen , array):
        for x in array:
            x.animacion()
            x.draw(screen)
            x.mover()
            x.delete(x)
    
    def add_array(self , array , pet):
        if random.randint(0 , 100) % 10 == 0 and len(array) < 2:
            array.append(pet)


class Gusano(Pet):
    def __init__(self, vida , animation, animation_time, pet):
        super().__init__(animation, animation_time, pet)
        self.vida = vida

        self.rect.y = 320
        self.rect.x = random.randrange(ancho_pantalla - self.rect.height)
        
        self.audio = pygame.mixer.Sound("../multimedia/audio/bat_sound.mp3")

        self.velocidad_x = 2

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
        # self.audio.play()

    def delete(self , delete_bat):
        if self.rect.left <= 0:
            self.bats_array.remove(delete_bat)
    
    def appear(self , screen , array):
        for x in array:
            x.animacion()
            x.draw(screen)
            x.mover()
            x.delete(x)
    
    def add_array(self , array , pet):
        if random.randint(0 , 100) % 10 == 0 and len(array) < 1:
            array.append(pet)
