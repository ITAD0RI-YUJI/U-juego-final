from pantalla import *
from luffy import *
from totoro import *
from config import *

def main():
    character = Main_character()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        else:
            propiedades_pantalla()

            character.movimiento()
            character.dibujar()


            enemy = Enemy(totoro_movimiento)
            enemy.animacion()
            enemy.dibujar()
            
            pygame.display.flip()


if __name__ == "__main__":
    main()