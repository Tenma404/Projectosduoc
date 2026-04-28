#uso y ejemplos de random


# import random
# num=random.randint(1,10)
# print (num)

# for i in range (num):
#     print ("Hola Deny")

#crea un numero random entre 1 y 100
#Pide al usuario que adivine el numero 
#si el usuario pone un numero mayor al generado
# debe decir "te pasaste", en caso contrario 
# "el numero a adivinar es mayor "
# solo hay 5 intentos para adivinar

import random

print (" intente adivinar el numero")
num=random.randint(1,100)
intentos=5
while intentos > 0:
    adivina=int (input("ingrese un numero de 1 a 100:"))
    if adivina > num:
        intentos -= 1
        print (" te pasaste, intentos restantes:", intentos)
    elif adivina < num:
        intentos -= 1
        print (" el numero a adivinar es mayor , intentos restantes:", intentos)
    else:
        print ("felicidades, has adivinado el numero !!, tus intentos restantes son:", intentos)
        break
if intentos == 0:
    print (" lo siento, has agotado tus intentos, el numero era:", num)

    #arreglo en el codigo no se terminaba de ejecutar. se agrega break para detener la secuencia de codigo tras cumplir la condicion numerica 