print ("""
Bienvenido a Steam Dev. Ingrese su nombre de usuario y la cantidad de juegos que desea registrar .
       """)

indie=0
TRIPLE=0
E=0
T=0
M=0
while True:
    try:
        usuario=input("ingrese su nombre de usuario ")
        len(usuario)
        if len(usuario)<=4 and  " " not in usuario and usuario.upper():
            print ("ingrese un nombre de usuario valido ")
    except ValueError: 
        print ("ingrese valores alfabeticos, no de tipo entero ni decimal, intente nuevamente ")
    print ("ingrese la cantidad de juegos que desea registrar ")
    try:
        juegosn=int(input())
        if juegosn<=0:
            print ("ingrese una cantidad de juegos valida")
    except ValueError:
             print ("solo se aceptan digitos enteros y positivos")
    print ("Ingrese el precio ")
    try:
         precio=float (input("Ingrese el precio: "))
    
         if 20.000>precio<40.000:
              indie+=1
              print ("has registrado un indie")
    except ValueError:
         print ("ingrese solo numeros positivos y decimales")
    try:
         if precio>=40.000:
              TRIPLE+=1
              print ("has registrado un juego triple A")
    except ValueError:
         print ("ingrese digitos decimales y positivos, intente nuevamente ")
    print ("ingrese la edad para clasificar los juegos")
    try:
        
         edad=int (input(""))
         if edad<=0:
              print ("ingrese una edad valida")
         elif edad<=12:
              print ("has registrado un juego clasificacion E ")
              E+=1
         elif edad<=17:
              print ("has registrado un juego clasificacion T ")
              T+=1
         elif edad>=18:
              print ("has registrado un juego clasificacion M")
              M+=1
    except ValueError:
         print ("solo ingrese edades enteras o positivas. no datos tipo alfabeticos")
    print (f"has registrado {indie} juegos indie, {TRIPLE} juegos de estudio, {E} de clasificacion E, {T} de clasificacion T y {M} de clasificacion M")
    break 
