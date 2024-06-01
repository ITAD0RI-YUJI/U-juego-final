import pygame
import random
from pantalla import screen

pygame.init()

#Arreglos para controlar la cant de pets
bats_array = []
gusanos_array = []

#Colisiones entre objetos
def colision(objeto_chocado, objeto_chocando_arreglo):
    for objeto_chocando in objeto_chocando_arreglo:
        
        if objeto_chocado.rect.colliderect(objeto_chocando.rect):
            objeto_chocado.vida -= 1
            objeto_chocando_arreglo.remove(objeto_chocando)