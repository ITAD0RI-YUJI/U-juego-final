from pantalla import *
from Sprites_luffy import *
import pygame
pygame.init()
from pygame.sprite import Sprite



class Main_character(Sprite):
    def __init__(self):
        super().__init__()

        self.vida = 3
        self.velocidad = 3        
        self.quieto = quieto
        self.quieto.set_colorkey([0 , 0 , 0]) #Quitar el fondo negro que pone pygame         
        self.rect = self.quieto.get_rect()

        #Donde aparecera luffy en la pantalla
        self.rect.move_ip([10, 300])

        #Banderas para controlar el movimiento de luffy
        self.direction_right = False
        self.direction_left = False
        self.ataquez = False
        self.salto = False
        self.parar = False

        #Variales numericas para controlar diferentes acciones de luffy 
        self.cuenta_ataques = 0
        self.cuenta_salto = 10
        self.cuenta_pasos = 0
        self.px = 10
        self.py = 300
        self.ancho = 40

        
        #Velicudad de pasar de imagen en imagen
        self.anim_speed = 6
        self.anim_speed_atack = 4

    def movimiento(self):
        #Bandera para controlar si luffy esta quieto
        self.quieto = True
        
        keys = pygame.key.get_pressed()
        #Moviemiento a la derecha
        if keys[pygame.K_RIGHT]:
            if self.px + self.velocidad + self.ancho <= ancho_pantalla:  # Verifica el borde derecho
                self.px += self.velocidad
                self.direction_right = True
                self.direction_left = False
                self.quieto = False
                self.parar = False
                self.cuenta_ataques = 0

        #Movimiento a la izquierda
        if keys[pygame.K_LEFT]:
            if self.px - self.velocidad >= 0:  # Verifica el borde izquierdo
                self.px -= self.velocidad
                self.direction_left = True
                self.direction_right = False
                self.quieto = False
                self.parar = False
                self.cuenta_ataques = 0

        if keys[pygame.K_z]:
            self.ataquez = True
            self.direction_left = False
            self.direction_right = False
            self.quieto = False
            self.parar = True

        #Si luffy esta saltando, no entra la solicitud de salto
        if not (self.salto):
            if keys[pygame.K_UP]:
                self.salto = True
                self.izquierda = False
                self.derecha = False
                self.parar = False
                self.cuenta_pasos = 0
                self.cuenta_ataques = 0

        #Si luffy no esta saltando, se hace la subida y bajada del sprite de luffy
        else:
            if self.cuenta_salto >= -10:
                self.py -= (self.cuenta_salto * abs(self.cuenta_salto)) * 0.3
                self.cuenta_salto -= 1
            else:
                self.cuenta_salto = 10
                self.salto = False

        # Actualizar la posición del rectángulo de Luffy
        self.rect.topleft = (self.px, self.py) 

    def dibujar(self):
        #Contador de pasos
        if self.cuenta_pasos + 1 >= len(luffy_der) * self.anim_speed:
            self.cuenta_pasos = 0

        if self.cuenta_ataques +1 >= len(ataquez) * self.anim_speed_atack:
            self.parar = False
            self.cuenta_ataques = 0

        #Condicinales para movimientos de luffy 
        if self.direction_right and not self.quieto:
            screen.blit(luffy_der[self.cuenta_pasos // self.anim_speed], (int(self.px), int(self.py)))
            self.cuenta_pasos += 1

        elif self.direction_left and not self.quieto:
            screen.blit(luffy_izq[self.cuenta_pasos // self.anim_speed], (int(self.px), int(self.py)))
            self.cuenta_pasos += 1

        elif self.salto:
            screen.blit(salto[self.cuenta_pasos // self.anim_speed], (int(self.px), int(self.py)))
            self.cuenta_pasos += 1

        elif self.ataquez and self.parar:
            screen.blit(ataquez[self.cuenta_ataques // self.anim_speed_atack], (int(self.px), int(self.py)))
            self.cuenta_ataques += 1

        #Para cuando luffy este quieto 
        else:
            screen.blit(quieto , (int(self.px), int(self.py)) )


class sombrero(Main_character):
    def __init__(self , array):
        super().__init__()
    
        #Imagen de la vida de Luffy
        self.vida_image = pygame.image.load("../multimedia/img/luffy_img/luffy_live.png").convert_alpha()
        
        self.rect = self.vida_image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.hat_array = array

    def vidas_array_add(self):
        for x in range(self.vida):
            self.hat_array.append(self.vida_image)

    def dibujar_vidas(self):
        for i in range(len(self.hat_array)):
            pos_x = 10 + i * (self.rect.width + 10)  # Posición X con un espaciado de 10 píxeles entre las vidas
            pos_y = 10 
            screen.blit(self.hat_array[i], (pos_x, pos_y))
