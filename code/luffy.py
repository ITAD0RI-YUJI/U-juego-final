from pantalla import *
import pygame
pygame.init()
from pygame.sprite import Sprite

#luffy quieto
quieto = pygame.image.load("../multimedia/img/luffy_img/luffy.png").convert()
quieto.set_colorkey([0 , 0 , 0] ) #Quitar el fondo negro que pone pygame

#imagenes luffy
luffy_der = [pygame.image.load("../multimedia/img/luffy_img/l_der1.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_der2.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_der3.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_der4.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_der5.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_der6.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_der7.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_der8.png")]

luffy_izq = [pygame.image.load("../multimedia/img/luffy_img/l_izq1.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_izq2.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_izq3.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_izq4.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_izq5.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_izq6.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_izq7.png"),
             pygame.image.load("../multimedia/img/luffy_img/l_izq8.png")]


class Main_character(Sprite):
    def __init__(self):
        super().__init__()

        self.vidas = 3
        self.velocidad = 3         

        self.personaje_imagen = pygame.image.load("../multimedia/img/luffy_img/luffy.png").convert()
        self.personaje_imagen.set_colorkey([0 , 0 , 0]) #Quitar el fondo negro que pone pygame         
        self.rect = self.personaje_imagen.get_rect()

        self.rect.move_ip([10, 300])

        self.direction_right = False
        self.direction_left = False
        self.quieto = True
        
        self.cuenta_pasos = 0
        self.px = 10
        self.py = 300
        self.ancho = 40
        
        self.anim_speed = 6

    def movimiento(self):
        #Moviemiento a la derecha
        self.quieto = True
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.px + self.velocidad + self.ancho <= ancho_pantalla:  # Verifica el borde derecho
                self.px += self.velocidad
                self.direction_right = True
                self.direction_left = False
                self.quieto = False

        if keys[pygame.K_LEFT]:
            if self.px - self.velocidad >= 0:  # Verifica el borde izquierdo
                self.px -= self.velocidad
                self.direction_left = True
                self.direction_right = False
                self.quieto = False

    def dibujar(self):
         #Contador de pasos
        if self.cuenta_pasos + 1 >= len(luffy_der) * self.anim_speed:
            self.cuenta_pasos = 0

        if self.direction_right and not self.quieto:
            screen.blit(luffy_der[self.cuenta_pasos // self.anim_speed], (int(self.px), int(self.py)))
            self.cuenta_pasos += 1

        elif self.direction_left and not self.quieto:
            screen.blit(luffy_izq[self.cuenta_pasos // self.anim_speed], (int(self.px), int(self.py)))
            self.cuenta_pasos += 1

        else:
            screen.blit(quieto , (int(self.px), int(self.py)) )
