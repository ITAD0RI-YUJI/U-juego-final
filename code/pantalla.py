import pygame
pygame.init()
pygame.mixer.init()

ancho_pantalla = 711
alto_pantalla = 400

# Crear la pantalla y el reloj
screen = pygame.display.set_mode([ancho_pantalla, alto_pantalla])
clock = pygame.time.Clock()
pygame.display.set_caption('Luffy vs Totoro')


# Se coloca fuera de "propiedades_pantalla()" ya que esto se ejecutará, se llame o no a la función
pygame.mixer.music.load("../multimedia/audio/mainSound_gear_five.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


def propiedades_pantalla():
    # Cargar imagen en la memoria
    background_img = pygame.image.load("../multimedia/img/fondo_img/background_fusion.jpeg").convert()
    
    # Ubicar la imagen en la pantalla
    screen.blit(background_img, [0, 0])

    #pygame.display.flip()
    clock.tick(60)

    # pygame.quit()