from pantalla import *
from personaje import *
from config import *

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        else:
            propiedades_pantalla()

            character = main_character()
            character.dibujar()

            enemy = Enemy(totoro_movimiento)
            enemy.animacion()
            enemy.dibujar()
            
            pygame.display.flip()


if __name__ == "__main__":
    main()