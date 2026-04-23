# def saludo():
#     print ("Hola")

# saludo()
# n="Nano"
# def chao ():
#     print (f"Nos vemos {n}")

# chao()

# def suma ():
#     n1=int (input (" ingrese el primer numero "))
#     n2=int (input (" ingrese el segundo numero "))
#     print (f" El resultado de la suma es : {n1 + n2}")

# suma()

# def suma ():
#     n1=int (input (" ingrese el primer numero "))
#     n2=int (input (" ingrese el segundo numero "))
#     print (f" El resultado de la suma es : {n1 + n2}")

# def resta ():
#     n1=int (input (" ingrese el primer numero "))
#     n2=int (input (" ingrese el segundo numero "))
#     print (f" El resultado de la resta es : {n1 - n2}")

# def multiplicacion ():
#     n1=int (input (" ingrese el primer numero "))
#     n2=int (input (" ingrese el segundo numero "))
#     print (f" El resultado de la multiplicacion es : {n1 * n2}")

# def division ():
#     n1=int (input (" ingrese el primer numero "))
#     n2=int (input (" ingrese el segundo numero "))
#     if n2 != 0:
#         print (f" El resultado de la division es : {n1 / n2}")
#     else:
#         print (" Error: No se puede dividir por cero.")

  

# op=0
# while op!= 5:
#     print ("1. Suma ")
#     print ("2. Resta ")
#     print ("3. Multiplicacion ")
#     print ("4. Division ")
#     print (" 5.- Salir ")
#     op=int (input ("ingrese la opcion deseada "))
#     match op:
#         case 1:
#             suma()
#         case 2:
#             resta()
#         case 3:
#             multiplicacion()
#         case 4:
#             division()
#         case 5:
#             print (" has seleccionado salir")
#         case _:
#             print (" Opcion no valida, intente de nuevo.")
 
def pin ():
    print (" Cree su Pin de 4 digitos ")
pin=int (input ("Ingrese su pin de 4 dígitos: "))
if 1000<=pin<=9999:
    print ("Pin correcto, creacion exitosa")
else:
    print ( "pin invalido, ingrese uno con 4 digitos ")

def Prom ():
    print ("ingrese 3 digitos a promediar ")
    n1=int (input (" ingrese el primer numero "))
    n2=int (input (" ingrese el segundo numero "))
    n3=int (input (" ingrese el tercer numero "))
    print (f" El resultado del promedio es : {(n1 + n2 + n3) / 3}")

def vocales ():
    print (" ingrese una letra para determinar si es vocal o consonante ")
    letra=input (" ingrese una letra :")
    if letra.lower() in "aeiou":
        print (f" La letra {letra} es una vocal ")
    else:
        print (f" La letra {letra} es una consonante ")

    
    op=0
while op!= 4:
    print ("1. Promedio ")
    print ("2. Vocal o Consonante ")
    print ("3. Pin de 4 digitos ")
    print (" 4.- Salir ")
    op=int (input ("ingrese la opcion deseada "))
    match op:
        case 1:
            Prom()
        case 2:
            vocales()
        case 3:
            pin()
        case 4:
            print (" has seleccionado salir")
        case _:
            print (" Opcion no valida, intente de nuevo.") 