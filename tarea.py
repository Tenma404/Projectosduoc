Datos={
    "Nombre ": "  ",
    
    "Edad ":  0,
    
    "Correo ": 0,
    
    " Numero Telefonico ": "   ",
    
    
    " Nacionalidad " :  "  "
    
}


print ("ingrese los datos que desea agregar " )


print ("""
       1-. Nombre
       2-. Edad 
       3.- Correo Electronico
       4.- Nacionalidad
       5.- Numero Telefonico
       6.- Mostrar Datos Actualizados
       7.-Salir
       """)


while True:
    op=int(input)("ingrese una opcion")
    if op==1:
     print ("ingrese el nombre a guardar " )
     name=input("")
     Datos["Nombre "]=name
     print ("el nombre se ha guardado correctamente " )
    
    if op==2:
     print ("ingrese la edad a guardar en la base de datos " ) 
     age=int(input(" " ) ) 
     Datos["Edad "]=age
    
     print ("la edad se ha ingresado correctamente " )
    
    if op==3:
      print ("ingrese el correo a registrar " )
      email=input(" " )
      Datos["Correo "]=email
      print ("se han ingresado los datos exitosamente " )
    

    if op==4:
     print ("ingrese la nacionalidad a guardar en la base de datos " )
    nacion=input("" )
    
    Datos[" Nacionalidad "]=nacion
    
    print ("se ha ingresado correctamente la nacionalidad " )

    if op==5:
     print ("ingrese el numero telefonico a guardar en la base de datos " )
    
    telefono=int(input("") )
    
    Datos[" Numero Telefonico "]=telefono
    

    if op==6:
     print ("Estos son los datos guardados en nuestra base de datos " )
    
    print ("---"*10)
    
    print (Datos)
    

    if op==7:
    
     print ("has seleccionado salir, vuelva pronto a usar nuestro servicio " )
     break