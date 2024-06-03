from pantalla import *
from luffy import *
from totoro import *
from deidara_masa import *
from funcionesComunes import *
from inicio import *
from pets_sprites import *

#Instanciando la clase de menu
inicio = Menu()
iniciar = False
#Guardando el boleano para iniciar el juego
iniciar = inicio.iniciar_juego()
def main():
    
    if iniciar:
        enemy = Enemy(5 , totoro_movimiento , 800 , None)  # 800 milisegundos para cambiar la imagen
        character = Main_character()

        vidas = Sombrero(vidas_array_luffy)
        vidas.vidas_array_add()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            else:
                propiedades_pantalla()

                character.movimiento()
                character.dibujar()

                vidas.dibujar_vidas()

                enemy.animacion()
                enemy.draw(screen)
                enemy.colision(character)
                
                bat = Bat(1 , bat_movimiento , 200 , bats_array) #Colocar este dentro del while, así creerá nuevas instancias
                bat.add_array(bats_array , bat)
                bat.appear(screen , bats_array)

                gusano = Gusano(1, gusano_movimento , 200 , gusanos_array)
                gusano.add_array(gusanos_array , gusano)
                gusano.appear(screen , gusanos_array)
                
                character.colision(bats_array , vidas_array_luffy)
                #character.colision(gusanos_array , vidas_array_luffy)

                character.update_disparos(gusanos_array , gusano)
                character.update_disparos(bats_array , bat)


                
                pygame.display.flip()

if __name__ == "__main__":
    main()      