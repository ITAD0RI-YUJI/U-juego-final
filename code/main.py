from pantalla import *
from luffy import *
from totoro import *
from deidara_masa import *
from config import *
from petActions import *
from inicio import *

#Instanciando la clase de menu
inicio = Menu()
iniciar = False
#Guardando el boleano para iniciar el juego
iniciar = inicio.iniciar_juego()
def main():
    
    if iniciar:
        enemy = Enemy(totoro_movimiento, pos_totoro , 800)  # 800 milisegundos para cambiar la imagen
        character = Main_character()

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
                
                bat = Bat(bat_movimiento , 200 , bats_array) #Colocar este dentro del while, así creerá nuevas instancias
                add_array(bats_array , bat)
                appear(bats_array)

                gusano = Gusano(gusano_movimento , 200 , gusanos_array)
                add_array(gusanos_array , gusano)
                appear(gusanos_array)
                
                
                pygame.display.flip()

if __name__ == "__main__":
    main()