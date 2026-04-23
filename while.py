# cont=1
# while cont <=3:
#     print (f" el contador es  {cont}")
#     cont=cont+1
# pin=5656
# num=int (input (" ingrese su pin "))
# while num != pin:
#     print (" pin incorrecto, intente de nuevo ")
#     num=int (input (" ingrese su pin "))
# print (" pin correcto, acceso concedido ")

## pedir un numero al usuario y mostrar su tabla de multiplicar del 1 al 10

print (" ingrese un numero para mostrar su tabla de multiplicar ")
num=int (input ("ingrese un numero :"))
cant=1
while cant <=10:
    print (f"{num} x {cant} = {num*cant}")
    cant=cant+1