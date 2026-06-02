# lista=[1,2,3,4,5,6]

# print (lista)
# print (lista[0])
# print ("-"*30)

# for i in lista:
#     print (i*2)
# lista.append(64)

# print ("--"*20)

# for i in lista:
#     print (lista)

# fruta=["manzana","naranja","uvas","sandia"]

# print ("--"*10)
# print (fruta[0])
# print ("--"*10)
# print (fruta[1])
# print ("--"*10)
# print (fruta[2])
# print ("--"*10)
# print (fruta[3])
# print("--"*10)

# for f in fruta:
#     print (f)

pokemons=["Swampert","Sceptile"]

while True:
    try:
        print("1-. Agregar Pokemon ")
        print("2-. Eliminar Pokemon ")
        print("3-. Actualizar Pokemon ")
        print("4-. Mostrar Pokemon ")
        print("5-. Salir ")
        op=int(input("eliga una opcion"))
        match op:
            case 1:
                  print ("Ingrese el pokemon")
                  pkmn=input(" Nombre del pokemon")
                  pokemons.append (pkmn)
            case 2:
                print("Ingrese el pokemon a liberar")
                pkm=input ("   ")
                pokemons.remove(pkm)
            case 3:
                
                print ("estos son los pokemon actualizados :")
                print (pkmn)
            case 4:
                for p in pokemons:
                    c=1
                    print (c,".-",p)
                    c+=1          
    except ValueError as e:
        print (e)