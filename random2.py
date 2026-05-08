from random import randint

num1 = int(input("ingrese la base "))
num2 = int(input("ingrese el techo "))
while num1 > num2:
    print("los valores ingresados no son validos ")
    num1 = int(input("ingrese la base"))
    num2 = int(input("ingrese el techo "))

secret = randint(num1, num2)

print("intente adivinar el numero")
intentos = 3
while intentos > 0:
    adi = int(input(""))
    if adi > secret:
        intentos -= 1
        print(f"el numero a adivinar es menor, intente con un digito mas pequeño, te restan {intentos}")
    elif adi < secret:
        intentos -= 1
        print(f"el numero a adivinar es mayor, intente con un digito mas grande, te restan {intentos}")
    else:
        print("has logrado adivinar el numero !!!")
        break

if intentos == 0 and adi != secret:
    print(f"has perdido el numero a adivinar es {secret}")
