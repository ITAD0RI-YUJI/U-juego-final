import pygame
from pantalla import *
from pygame.sprite import Sprite
pygame.init()

class Menu(Sprite):
    def __init__(self):
        super().__init__()
        #Cargando la imagen del menu
        self.fondo_menu = pygame.image.load("../multimedia/img/fondo_img/inicio2.png")
        self.image = self.fondo_menu
        self.rect = self.image.get_rect()
        self.running = True

    def iniciar_juego(self):
        #Ciclo para la pantalla del menu
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            screen.blit(self.image, self.rect)
            pygame.display.update()

            tecla = pygame.key.get_pressed()
            #Presionar enter para jugar
            if tecla [pygame.K_RETURN]: 
                return True

