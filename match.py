op=0

# while op != 4:
#     print ("1. PC $500.000 " )
# print ("2. LGTV 55 Pulgadas $380.000 " )
# print ("3. Microondas Hamsa $100.000     " )
# print ("4-. Salir")
# op=int (input())
# match op:
#     case 1:
#         print (" El Total a Pagar es ", 500000 * 1.19)
#         total=500000 * 1.19
#     case 2:
#         print (" El Total a Pagar es ", 380000 * 1.19)
#         total=380000 * 1.19
#     case 3:
#         print (" El Total a Pagar es ", 100000 * 1.19)
#         total=100000 * 1.19
#     case 4:
#         print (" has seleccionado salir, hasta luego ")
 
#     case _:
#         print (" opcion no valida, intente de nuevo")
op=0
while op != 5:
    print ("1. Suma ")
    print ("2. Resta ")
    print ("3. Multiplicacion ")
    print ("4. Division ")
    print (" 5.- Salir ")
    op=int (input ("ingrese la opcion deseada "))
num1=float (input (" ingrese el primer numero "))
num2=float (input (" ingrese el segundo numero "))
match op:
        case 1:
            print (f" El resultado de la suma es : {num1 + num2}")
        case 2:
            print (f" El resultado de la resta es : {num1 - num2}")
        case 3:
            print (f" El resultado de la multiplicacion es : {num1 * num2}")
        case 4:
            if num2 != 0:
                print (f" El resultado de la division es : {num1 / num2}")
            else:
                print (" Error: No se puede dividir por cero.")
        case 5:
            print (" has seleccionado salir")
        case _:
            print (" Opcion no valida, intente de nuevo.")
