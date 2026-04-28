#se piden dos peleadores de killin instint y a eleccion con input se elige un peleador 
# cada jugador empieza con 100 puntos de vida 
# debe ser con turnos 
# cada golpe debe ser de 7 o 18 puntos de daño
# se termina la match cuando uno de los peleadores llega a 0 puntos de vida 
#se debe mostrar el ganador al finalizar la match
#  BONUS: mostrar las barras de energia de cada peleador en cada turno
# usar un time sleep para los turnos 

print (" Ingrese el nombre del primer peleador")
peleador1=input()
print (" Ingrese el nombre del segundo peleador")
peleador2=input()
vida1=100
vida2=100
import random
import time
while vida1 > 0 and vida2 > 0:
    golpe=random.choice([7,18])
    vida2 -= golpe
    print (peleador1, "golpea a", peleador2, "y le quita", golpe, "puntos de vida")
    print (peleador1, "tiene", vida1, "puntos de vida restantes")
    print (peleador2, "tiene", vida2, "puntos de vida restantes")
    time.sleep(1)
    if vida2 <= 0:
        print (peleador1, "es el ganador!")
        break
    golpe=random.choice([7,18])
    vida1 -= golpe
    print (peleador2, "golpea a", peleador1, "y le quita", golpe, "puntos de vida")
    print (peleador1, "tiene", vida1, "puntos de vida restantes")
    print (peleador2, "tiene", vida2, "puntos de vida restantes")
    time.sleep(1)
    if vida1 <= 0:
        print (peleador2, "es el ganador!")
        break

    # se agrega break para detener la secuencia de codigo tras cumplir la condicion numerica, evitando que el programa siga ejecutandose tras la derrota de cualquiera de los dos jugadores 
    # Se implementa comando time para poder ingresar los turnos de cada jugador dependiendo de la variable numerica asignada a dicha funcion
    # se prueba y no muestra errores, de preferencia ingresar personajes reales del dicho Fighting para mayor inmersion.
    # se subeel commit para testeo en casas y integracion del codigo escrito en otros programas para mayor rapidez
    # disclaimer; el uso de cada linea subida a github es de uso libre para cualquiera con acceso a repositorio publico cmo material de estudio o practica, mas no usarlo en evaluaciones ya que no es perfecto y podria causar notas no deseadas o iguales a un 5
    