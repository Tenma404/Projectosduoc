deuda=100.000
total=0
print (""" 
bienvenido al  menu del banco Estandar seleccione la opcion que desea realizar
       1-. Pago de Deuda
       2-. Compras
       3-. Salir
       """)
op=int(input("ingrese la opcion que desea realizar "))
if op==1:
    while deuda>0:
        try:
            pago=float(input("ingrese el monto a pagar"))
            if pago<0:
                print ("ingrese un valor positivo")
            elif pago>deuda:
                print ("no se puede pagar un valor superior a la deuda")
            elif pago>=0:
                deuda-=pago
                print (f"la deuda actual es de {deuda}")
            if deuda==0:
                print ("has pagado la totalidad de tu deuda, la tarjeta cuenta con saldo nuevamente")
                break
        except ValueError:
            print ("ingrese solo valores decimales y positivos, intente nuevamnete")
elif op==2:
    try:
        print ("""
1.- Pc Gamer ("valor variable segun requerimientos del cliente)
2.- Play Station 5 ("250.000)
3-. Batidora  ("45.000)
4-. Secadora("30.000)""")
        producto=int(input("ingrese el numero del producto que desea comprar "))
        if producto==1:
            print ("el valor de la pc gamer es variable segun los requerimientos del cliente, por lo que se le asignara un valor de 150.000")
            total+=150.000
        elif producto==2:
            total+=250.000
        elif producto==3:
            total+=45.000
        elif producto==4:
            total+=30.000
        else:
            print ("ingrese solo un producto listado")
    except:
        print("ingrese solo valores numericos positivos")

elif op==3:
    print ("has seleccionado salir. gracias por usar el banco estandar para tus compras")