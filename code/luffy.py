from pantalla import *
from config import *
import pygame
pygame.init()
from pygame.sprite import Sprite


class Main_character(Sprite):
    def __init__(self):
        super().__init__()
        self.vidas = 3
        self.velocidad = 3         
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
            screen.blit(quieto , (int(self.px), int(self.py)))



