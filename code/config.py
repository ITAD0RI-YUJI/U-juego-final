import pygame
pygame.init()

# Posición Totoro
pos = [510, 150]

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
