cuenta=0
import random 
codigo=1234
clavetarjeta=270506


while True:
    try:
        print ("ingrese su clave de 4 digitos")
        clave=int(input(""))
        if clave==1234:
            print ("clave correcta, has ingresado de manera exitosa")
            break
        else:
            print ("clave incorrecta intentelo nuevamente")
    except:
        print("solo se pueden ingresar valores numeros. intentelo nuevamente ")

    

print ("""bienvenido al app de compras por excelencia que operacion desea realizar
       
       1- Ver Catalogo 

       2- Pagar el carrito y sus añadidos

       3-. Salir """)

op=int(input("ingrese una de las opciones"))

if op==1:
    try:
        print ("""Catalogo de compras de este mes
           1-. Ropa de invierno (25.000)
           2-. Televisor 30 Pulgadas (150.000)
           3-. Producto Sorpresa (valor aleatorio)
           """)
        op2=int(input("seleccione la opcion que desea realizar"))
        if op2==1:
            cuenta+=25.000
        if op==2:
            cuenta+=150.000
        if op==3:
            preciorandom=random.randint(10.000,40.000)
            cuenta+=preciorandom
    except:
        print ("solo se pueden ingresar valores numericos")
    
    if op==2:
        while True:
            try:
                print ("bienvenido al carrito ")
                print (f"la cuenta a pagar es de {cuenta} ")
            except:
                print ("solo se pueden ingresar valores numericos, intente nuevamente")
            clave1=int(input("ingrese la clave de su tarjeta de credito para seguir"))
            if clave1==clavetarjeta:
                cuenta-=cuenta
                print ("has pagado correctamente la cuenta del carrito")
                break
            else:
                print ("clave incorrecta, intente nuevamente")
        if op==3:
            print (" has seleccionado salir,gracias por usar nuestra app ")
