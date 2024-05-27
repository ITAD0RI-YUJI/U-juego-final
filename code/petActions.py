import pygame
import random
from pantalla import screen

pygame.init()

#Arreglos para controlar la cant de pets
bats_array = []
gusanos_array = []


#Funciones
def add_array(array , pet):
    if random.randint(0 , 100) % 10 == 0 and len(array) < 2:
        array.append(pet)

def appear(array): #Controlar la cant de pets visibles al tiempo
    for x in array:
        x.animacion()
        x.draw(screen)
        x.mover()
        x.delete(x)
                