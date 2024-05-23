from pantalla import *
from luffy import *
from totoro import *
from config import *

def main():
    enemy = Enemy(totoro_movimiento, pos , 500)  # 500 milisegundos para cambiar la imagen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        else:
            propiedades_pantalla()

            character = main_character()
            character.dibujar()

            enemy.animacion()
            enemy.draw(screen)
            
            pygame.display.flip()


if __name__ == "__main__":
    main()