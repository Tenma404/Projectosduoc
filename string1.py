# Name="  Vergil  "
# print (Name.strip() )
# print(Name.lower())
# print (Name.upper())
# print (Name.replace("Vergil", "Dante"))
# print (Name.find("Vergil"))

# Usuario=input (" cree su nombre de usuario")
# clave="SHAZAM"

# print ("ingrese su usuario y clave ")

# if clave.upper()==clave:
#     print( " inicio de sesion exitoso  Bienvenido  ", Usuario)
# else:
#     print ("clave o usuario incorrecto, intente mas tarde")
     
# usuario=input ("cree su nombre de usuario:")
# if 4<=len(usuario)<=10:
#     print ( " el nombre de usuario debe tener entre 4 a 10 caracteres,intente de nuevo")
# else:
#     print ( " el usuario introducido cumple con los requisitos, Bienvenido ", usuario)

print (" Cree su Pin de 4 digitos ")
pin=int (input ("Ingrese su pin de 4 dígitos: "))
if 1000<=pin<=9999:
    print ("Pin correcto, creacion exitosa")
else:
    print ( "pin invalido, ingrese uno con 4 digitos ")