# Crear un gestor de pacientes 

pacientes=[

  {"Nombre": " Aquiles Baeza", "Preevision":  "Fonasa", "Temperatura": 35.6,
   "Grave":False } 
   


]


# Crear al gestor de pacientes en un centro medico donde
#para poner el nombre se debe validar que no este vacio 
#y aqdemas tenga 8 caracteres 
#para la preevision solo existen 3 posibles valores Fonasa Isapre o Fodesa
#al ingresar el paciente se debe ingresar la temperatura y crear funcion que determine si esta grave o no 
# si el valor de la fiebre es superior o igual a 39 grados celcius







def agregarpaciente ():
    paciente=input("Ingrese el nombre del paciente")
    temp=float(input("Ingrese la temperatura corporal del paciente "))
    
