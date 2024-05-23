from pantalla import *
from luffy import *
from totoro import *
from deidara_masa import *
from config import *

def main():
    enemy = Enemy(totoro_movimiento, pos_totoro , 500)  # 500 milisegundos para cambiar la imagen
    character = Main_character()
    bat = Bat(bat_movimiento , pos_bat , 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        else:
            propiedades_pantalla()

            character.movimiento()
            character.dibujar()

            enemy.animacion()
            enemy.draw(screen)
            
            bat.animacion()
            bat.draw(screen)

            pygame.display.flip()


if __name__ == "__main__":
    main()