import pygame
import random
from pantalla import screen
import sys

pygame.init()

#Arreglos para controlar la cantidad de los objetos en la pantalla
bats_array = []
gusanos_array = []
vidas_array_luffy = []

#Colisiones entre objetos
def colision(objeto_chocado , objeto_chocando_arreglo , array_vidas):
    for objeto_chocando in objeto_chocando_arreglo:
        
        if objeto_chocado.rect.colliderect(objeto_chocando.rect):
            objeto_chocado.vida -= 1
            objeto_chocando_arreglo.remove(objeto_chocando)
            array_vidas.pop()
            print(objeto_chocado.vida)

            if objeto_chocado.vida <= 0:
                sys.exit()