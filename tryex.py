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
                print ("ingrese el la clave secreta de su tarjeta para realizar la compra")
                codigot=int(input("ingrese la clave de su tarjeta"))
                if codigot==clavetarjeta:
                    print ("se ha realizado con exito la compra")
                    break
                else:
                    print ("has ingresado una clave incorrecta, intente de nuevo")
            except:
                print ("solo se pueden ingresar numeros enteros, no decinmales ni alfabeticos, intente de nuevo")

        if op==3:
            print ("has seleccionado salir,ten un buen dia y vuelva pronto ")
            