from pantalla import *
from luffy import *
from totoro import *
from deidara_masa import *
from funcionesComunes import *
from inicio import *
from pets_sprites import *
import sys
import pygame

# Instanciando la clase de menu
inicio = Menu()
iniciar = False
# Guardando el booleano para iniciar el juego
iniciar = inicio.iniciar_juego()

def main():
    if iniciar:
        character = Main_character()
        enemy = Enemy(5, totoro_movimiento, 800, None, vidas_array_totoro)  # 800 milisegundos para cambiar la imagen
        enemy.vidas_array_add()

        vidas = Sombrero(vidas_array_luffy)
        vidas.vidas_array_add()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            
            if character.final:
                propiedades_pantalla()
                
                enemy.dibujar_vidas()

                character.movimiento()
                character.dibujar()

                vidas.dibujar_vidas()

                enemy.animacion()
                enemy.draw(screen)

                bat = Bat(1, bat_movimiento, 200, bats_array)  # Colocar este dentro del while, así creerá nuevas instancias
                bat.add_array(bats_array, bat)
                bat.appear(screen, bats_array)

                gusano = Gusano(1, gusano_movimento, 200, gusanos_array)
                gusano.add_array(gusanos_array, gusano)
                gusano.appear(screen, gusanos_array)
                
                character.colision(bats_array, vidas_array_luffy)
                character.colision(gusanos_array, vidas_array_luffy)

                character.update_disparos(gusanos_array, gusano)
                character.update_disparos(bats_array, bat)
                character.update_especial(gusanos_array, gusano, enemy, vidas_array_totoro)
                character.update_especial(bats_array, bat, enemy, vidas_array_totoro)

            else:
                pygame.mixer.music.pause()

                if character.vida > 0:
                    character.luffy_sound_ganar.play()
                    character.luffy_sound_ganar.set_volume(0.1)
                    pygame.time.wait(int(character.luffy_sound_ganar.get_length() * 1000))  # Esperar a que el sonido termine
                    
                else:
                    character.luffy_sound_perder.play()
                    character.luffy_sound_perder.set_volume(0.1)
                    pygame.time.wait(int(character.luffy_sound_perder.get_length() * 1000))  # Esperar a que el sonido termine
                
                running = False  # Salir del bucle después de reproducir el sonido

            pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()