pacientes=[
    {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
     "temperatura":34.6, "grave": False}
]

'''crear al gestor de pacientes en un centro medico
Para poner el nombre se debe validar que no este vacio 
y ademas tenga mas de 8 caracteres
Para la prevision de salud solo exiten 3 posibles valores
Fonasa, Isapre, o Fodesa
Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°
Cada atencion vale $25.000
Los despcuentos corresponden a 
FOnasa 54%
Isapre 27%
Fodesa 12,5%

'''

def prev ():
    prev=int(input("Eliga su prevision 1 . Fonasa, 2 . Isapre, 3  Fodesa"))
    if prev==1:
        descuennto=25.000*54/100
        print (f"su total a pagar es  :  {descuennto}")
    elif prev==2:
        descuennto=25.000*27/100
        print (f"su total a pagar es  :  {descuennto}")
    elif prev==3:
        descuennto=25.000*12.5/100
        print (f"su total a pagar es  :  {descuennto}")
    else:
        print ("Ingrese un valor valido y intentelo nuevamente ")
        
    

       
def agregarpaciente():
   nombre=input ("Ingrese el nombre del paciente ")
   while len(nombre) <8  or nombre.isspace():
       print ("ERROR EL SISTEMA NO ADMITE NOMBRES EN BLANCO O CON MENOS DE 8 CARACTERES INTENTE NUEVAMENTE")
       nombre=input("ingrese el nombre del paciente nuevamente ")
       prevision=input ("ingrese su prevision (Fonasa,Isapre,Fodesa)")
       while prevision not in ["Fonasa","Isapre","Fodesa"]:
           print ("La prevision debe ser una de las mostradas en pantalla, intente nuvamente")
           prevision=input ("Ingrese su prevision (Isapre,Fonasa,Fodesa)")
       temperatura=float(input("Ingrese la temperatura del paciente "))
       grave=validarEstado(temperatura)
       paciente={"nombre":nombre,"prevision":prevision,"temperatura":temperatura,"grave":grave}
       pacientes.append(paciente)
       print ("Paciente Agregado al Sistema Correctamente ")
        
       


def validarEstado(tempe):
   if tempe>39:
       return True 
   else:
       return False
def mostrarPacientes():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        c=1
        for p in pacientes:
            print(f"{c} .- {p}")
            c+=1
while True:
    try:
        print("1.- Ingresar paciente")
        print("2.- Quitar paciente")
        print("3.- Tomar Temperatura")
        print("4.- Cobra atencion")
        print("5.- Mostrar Pacientes")
        print("9.- Salir")
        op=int(input("Ingrese una opcion: "))
        match op:
            case 1:
                agregarpaciente()
            case 2:
                mostrarPacientes()
                paci=int(input("Que paciente se vá?: "))
                pacientes.pop(paci-1)
                print("Paciente eliminado.")
            case 3:
                mostrarPacientes()
                
            case 4:
                prev()
                
            case 5:
                mostrarPacientes()
            case 9:
                print("Saliendo")
                break
            case _:
                print("Opción inválida")
    except Exception as e:
        print("Error:" , e)