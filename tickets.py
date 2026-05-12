print ("Bienvenido al terminal de buses !")
while True:
    try:
        pasajes=int(input("cuantos pasajes desea comprar ") )
    except ValueError :
     print ("el error es ",ValueError )
    print ("Solo ingresar numeros enteros " )
    break

total=0 
while True:
    try:
        for i in range (pasajes):
            print ("ingrese el precio a pagar de los pasajes")
            pasaje1=float(input("Valor del pasaje"))
    except: 
     print ("el valor del pasaje del solo puede sere decimal ")
    
    total+=pasaje1
    print (f"el valor total es {total} " ) 
    break