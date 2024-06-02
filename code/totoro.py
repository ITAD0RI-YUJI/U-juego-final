# from pantalla import *
import pygame
pygame.init()
from objetoAbstracto import *
 
class Enemy(Dad):
    def __init__(self , vida , animation , animation_time , pet):
        super().__init__(animation, animation_time, pet)

        self.vidas = vida

        self.rect.y = 150
        self.rect.x = 510   
        
    def animacion(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > self.animation_time:
            self.last_update = now
        
            self.contador = (self.contador + 1) % len(self.images_animation)
            self.personaje_imagen = self.images_animation[self.contador]
            self.rect = self.personaje_imagen.get_rect(topleft=self.rect.topleft)
    
    def draw(self, screen):
        screen.blit(self.personaje_imagen, self.rect)
    
    def colision(self , objeto_chocando):
        if objeto_chocando.rect.colliderect(self.rect):
            self.vida -= 1
            print("Totoro: " , objeto_chocando.vida)