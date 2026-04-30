# crear un menu de un zoo mostrando el precio respectivo por el rango de edad niños (1-17) pagan 1000 pesos, adultos (18-64) pagam 3000
# y adultos mayores (mayores a 64 años ) pagan 1500
# usaar un match y un while para el funcionamiento del menu 
# luego mostrar la cantidad de personas que seleccionan la dicha opcion y calcular el precio total y la cantidad total de personas para luego pagar

op=0
personas=0
total=0

while op!=4:
    print("""
  1-. Niños (1-17) $1.000
  2-. Adultos (18-64) $3.000
   3.- Adultos Mayores (64+) $1.500
    4.- Salir """)
    op=int (input ("ingrese la opcion a pagar ") )

    match op:
        
        case 1: 
            print ("Pagando el precio de niño " )
            c=int (input ("cual es la cantidad ? " ) )
            if c>10:
                  print ("has ingresado mas de diez personas, intente nuevamente")
            else:
                print(" has ingresado ", c, " personas")
                total=1000*c
                personas+=c
        case 2:
            print ("Pagando el precio de Adulto ")
            c=int (input ("cual es la cantidad ? " ) )
            if c>10:
                  print ("has ingresado mas de diez personas, intente nuevamente")
            else:
                print(" has ingresado ", c, " personas")
                total=3000*c
                personas+=c
        case 3: 
            print ("Pagando el precio de Adulto Mayor ")
            c=int (input ("cual es la cantidad ? " ) )
            if c>10:
                  print ("has ingresado mas de diez personas, intente nuevamente")
            else:
                print(" has ingresado ", c, " personas")
                total=1500*c
                personas+=c
        case 4: 
          print (" has seleccionado la opcion salir ", " la cantidad total de personas es " , c, " y el total a pagar es ", total )