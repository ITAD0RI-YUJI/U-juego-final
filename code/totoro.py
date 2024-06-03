# from pantalla import *
import pygame
pygame.init()
from objetoAbstracto import *
from pantalla import screen
 
class Enemy(Dad):
    def __init__(self , vida , animation , animation_time , pet , array_vidas):
        super().__init__(animation, animation_time, pet)

        self.vidas = vida

        self.rect.y = 150
        self.rect.x = 510   

        self.array_vidas = array_vidas
        self.vida_image = pygame.image.load("../multimedia/img/totoro_img/totoro_live.png").convert_alpha()
        self.rect_vida_image = self.vida_image.get_rect()
        
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

    def vidas_array_add(self):
        for x in range(self.vidas):
            self.array_vidas.append(self.vida_image)

    def dibujar_vidas(self):
        for i in range(len(self.array_vidas)):
            pos_x = 10 + i * (self.rect_vida_image.width)  # Posición X con un espaciado de 10 píxeles entre las vidas
            pos_y = 50 
            screen.blit(self.array_vidas[i], (pos_x, pos_y))
