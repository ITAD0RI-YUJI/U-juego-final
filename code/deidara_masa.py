import pygame
import random
from pantalla import ancho_pantalla , alto_pantalla
from objetoAbstracto import *

pygame.init()


#Clases de los pets
class Bat(Dad):
    def __init__(self , vida , animation , animation_time , pet):
        super().__init__(animation, animation_time, pet)
        self.vida = vida

        self.rect.y = random.randrange(alto_pantalla - self.rect.height)
        self.rect.x = 680
        
        self.audio = pygame.mixer.Sound("../multimedia/audio/pet_sound.mp3")

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

    def add_array(self , array , pet):
        if random.randint(0 , 100) % 10 == 0 and len(array) < 2:
            array.append(pet)

    def appear(self , screen , array):
        for x in array:
            x.animacion()
            x.draw(screen)
            x.mover()
            x.delete(x)
            
    def delete(self , delete_bat):
        if self.rect.left <= 0:
            self.bats_array.remove(delete_bat)


class Gusano(Dad):
    def __init__(self, vida , animation, animation_time, pet):
        super().__init__(animation, animation_time, pet)
        self.vida = vida
        self.mitad = ancho_pantalla//2
        self.rect.y = 290
        
        self.mitad_pantalla = ancho_pantalla // 2
        self.rect.x = random.randrange(self.mitad_pantalla, ancho_pantalla - self.rect.height)

        self.audio = pygame.mixer.Sound("../multimedia/audio/pet_sound.mp3")

        self.velocidad_x = 2

    def animacion(self):
            now = pygame.time.get_ticks()

            if now - self.last_update > self.animation_time:
                self.last_update = now
                                            
                self.contador = (self.contador + 1) % len(self.images_animation)
                self.personaje_imagen = self.images_animation[self.contador]
                self.rect = self.personaje_imagen.get_rect(topleft=self.rect.topleft)

                if self.contador == 12:
                    self.contador = 6
                    
    def draw(self, screen):
        screen.blit(self.personaje_imagen, self.rect)

    def mover(self):
        self.rect.x -= self.velocidad_x
        # self.audio.play()

    def add_array(self , array , pet):
        if random.randint(0 , 100) % 10 == 0 and len(array) < 1:
            array.append(pet)

    def appear(self , screen , array):
        for x in array:
            x.animacion()
            x.draw(screen)
            x.mover()
            x.delete(x)

    def delete(self , delete_bat):
        if self.rect.left <= 0:
            self.bats_array.remove(delete_bat) 
