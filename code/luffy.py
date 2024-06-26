from pantalla import *
from Sprites_luffy import *
import pygame
pygame.init()
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group


class Main_character(Sprite):
    def __init__(self):
        super().__init__()
        self.final = True
        self.vida = 3
        self.velocidad = 3        
        self.quieto = quieto
        self.quieto.set_colorkey([0 , 0 , 0]) #Quitar el fondo negro que pone pygame         
        self.rect = self.quieto.get_rect()

        #Para cuando luffy pierde
        self.perdedor = perdedor
        self.rectp = self.perdedor.get_rect()

        #Para cuando luffy gana
        self.ganador = ganador_luffy
        self.rectg = self.ganador.get_rect()


        
        #Donde aparecera luffy en la pantalla
        self.rect.move_ip([10, 300])

        #Banderas para controlar el movimiento de luffy
        self.especialx = False
        self.direction_right = False
        self.direction_left = False
        self.ataquez = False
        self.salto = False
        self.parar = False
        self.parar2 = False
    
        #Variales numericas para controlar diferentes acciones de luffy 
        self.cuenta_especial = 0
        self.cuenta_ataques = 0
        self.cuenta_salto = 10
        self.cuenta_pasos = 0
        self.px = 10
        self.py = 300
        self.ancho = 40
        self.cantidad_enemigos_muertos = 0
        
        #Velicudad de pasar de imagen en imagen
        self.anim_speed = 6

        #Sonido de daño
        self.luffy_sound = pygame.mixer.Sound("../multimedia/audio/luffy_ouch.mp3")
        self.luffy_sound_ganar = pygame.mixer.Sound("../multimedia/audio/l_ganando.mp3")
        self.luffy_sound_perder = pygame.mixer.Sound("../multimedia/audio/l_perdiendo.mp3")

        #Sonido de totoro daño
        self.totoro_sound = pygame.mixer.Sound("../multimedia/audio/totoro_daño.mp3")

        # Grupo para manejar los disparos
        self.disparos = Group()
        self.especial = Group()


        # Variables de cooldown para la habilidad de ataque
        self.cooldown_total = 100  #tiempo de cooldown en frames
        self.cooldown_timer = 0

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
                self.cuenta_especial = 0

        #Movimiento a la izquierda
        if keys[pygame.K_LEFT]:
            if self.px - self.velocidad >= 0:  # Verifica el borde izquierdo
                self.px -= self.velocidad
                self.direction_left = True
                self.direction_right = False
                self.quieto = False
                self.parar = False
                self.cuenta_ataques = 0
                self.cuenta_especial = 0

        if keys[pygame.K_z] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and self.cooldown_timer == 0:
            self.ataquez = True
            self.direction_left = False
            self.direction_right = False
            self.quieto = False
            self.parar = True
            self.cooldown_timer = self.cooldown_total  # Reiniciar el temporizador de cooldown
        if self.cantidad_enemigos_muertos >= 10:
            if keys[pygame.K_x] and not keys[pygame.K_z] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self.especialx = True
                self.ataquez = False
                self.direction_left = False
                self.direction_right = False
                self.quieto = False
                self.parar2 = True

        #Si luffy esta saltando, no entra la solicitud de salto
        if not (self.salto):
            if keys[pygame.K_UP]:
                self.salto = True
                self.izquierda = False
                self.derecha = False
                self.parar = False
                self.cuenta_pasos = 0
                self.cuenta_ataques = 0
                self.cuenta_especial = 0

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

    def update_disparos(self, bicho_array , bicho):
        self.disparos.update()
        # Disminuir el temporizador de cooldown
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1

        for disparo in self.disparos:
            if disparo.rect.x > ancho_pantalla:
                disparo.kill()

            for objeto_chocando in bicho_array:
                if disparo.rect.colliderect(objeto_chocando.rect):
                    bicho.vida -= 1
                    bicho.audio.play()
                    self.cantidad_enemigos_muertos +=  1
                    print("Cantidad de enemigos asesinados")
                    print(self.cantidad_enemigos_muertos)
                    bicho_array.remove(objeto_chocando)
                    
                    disparo.kill()

    def update_especial(self, bichos_array, bicho, enemy, array_vidas):
        self.especial.update()

        for especial in self.especial:
            if especial.rect.x > ancho_pantalla:
                especial.kill()

            if especial.rect.colliderect(enemy.rect):
                self.totoro_sound.play()
                enemy.vidas -= 1
                especial.kill()
                array_vidas.pop()
                if enemy.vidas <= 0:
                    self.final = False
                    screen.blit(self.ganador, self.rectg)


            for objeto_chocando in bichos_array:
                if especial.rect.colliderect(objeto_chocando.rect):
                    bicho.vida -= 1
                    bicho.audio.play()
                    self.cantidad_enemigos_muertos = 0
                    bichos_array.remove(objeto_chocando)


    def dibujar(self):
        #Contador de pasos
        if self.cuenta_pasos + 1 >= len(luffy_der) * self.anim_speed:
            self.cuenta_pasos = 0

        if self.cuenta_ataques +1 >= len(ataquez) * self.anim_speed:
            #Se llama el disparo
            nuevo_disparo = Disparo(self.px, self.py)
            self.disparos.add(nuevo_disparo)
            self.parar = False
            self.cuenta_ataques = 0

        if self.cuenta_especial +1 >= len(ataque_especial) * self.anim_speed:
            nueva_especial = Especial(self.px, self.py)
            self.especial.add(nueva_especial)
            self.cuenta_especial = 0
            self.parar2 = False

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
            screen.blit(ataquez[self.cuenta_ataques // self.anim_speed], (int(self.px), int(self.py)))
            self.cuenta_ataques += 1

        elif self.especialx and self.parar2:
            screen.blit(ataque_especial[self.cuenta_especial// self.anim_speed], (int(self.px), int(self.py)))
            self.cuenta_especial += 1
        #Para cuando luffy este quieto 
        else:
            screen.blit(quieto , (int(self.px), int(self.py)) )

        # Dibujar disparos
        self.disparos.draw(screen)
        self.especial.draw(screen)


    def colision(self , objeto_chocando_arreglo , array_vidas):
        for objeto_chocando in objeto_chocando_arreglo:
            
            if self.rect.colliderect(objeto_chocando.rect):
                self.vida -= 1
                objeto_chocando_arreglo.remove(objeto_chocando)
                self.luffy_sound.play()
                array_vidas.pop()

                if self.vida <= 0:
                    self.final = False
                    screen.blit(self.perdedor, self.rectp)

                    


class Sombrero(Main_character):
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


class Disparo(Sprite):
    def __init__(self, px, py):
        super().__init__()

        self.image = disparoz
        self.rect = self.image.get_rect()
        self.rect.x = px + 50
        self.rect.y = py
        self.velocidad = 5

    def update(self):
        self.rect.x += self.velocidad

class Especial(Sprite):
    def __init__(self, px, py):
        super().__init__()

        self.image = especial
        self.rect = self.image.get_rect()
        self.rect.x = px + 50
        self.rect.y = py
        self.velocidad = 7

    def update(self):
        self.rect.x += self.velocidad