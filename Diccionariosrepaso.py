goty={
    1:{"Titulo":"Uncharted 4 ","Calificacion": 93},
    2:{"Titulo":"DOOM 2016" , "Calificacion": 85},
    3:{"Titulo":"Zelda BOTW ", "Calificacion": 98},
    4:{"Titulo": "GTA Vice City", "Calificacion": 95}
    
    
    
    
    
    
}

def mostrar ():
    for p,z in goty.items():
        print (f".-{p}{z}")
        print ("---"*10)
       
       

def borrar():
    mostrar()
    borrarjuego=int(input("Eliga un juego a borrar (solo ingrese numeros)"))
    del goty[borrarjuego]
    

def actualizar():
    mostrar()
    newdata=int(input("ingrese el titulo a actualizar "))
    title=input("ingrese el nuevo titulo")
    rating=float(input("ingrese el nuevo rating"))
    goty[actualizar]={"Titulo":title,"Calificacion":rating}
    print ("has actualizado los datos del rating correctamente")
    
def agregar():
    Juego=input("ingrese el Titulo a Agregar")
    Rate=float(input("ingrese el rating a agregar"))
    goty[list(goty.keys())[-1]+1]={"Titulo": Juego , "Calificacion": Rate}

def menugoty():
    while True:
        try:
            print ("1.-Agregar Titulos ")
            print ("2.- Eliminar Titulos")
            print ("3.- Actualizar Titulos")
            print ("4.- Mostrar Titulos")
            print ("5.- Salir")
            
            op=int(input("Ingrese una opcion a seleccionar"))
            match op:
                case 1:
                    agregar()
                    
                case 2:
                    borrar()
                    
                case 3:
                    actualizar()
                
                case 4:
                    mostrar()
                    
                case 5:
                        print ("Has Elegido Salir... saliendo")
                        break
                    
                case _:
                    print ("opcion invalida intente nuevamente")
                    
        except ValueError:
            print (ValueError)
            print ("Error Ingrese solo numeros enteros positivos")
            
            

menugoty()