Nombre=input ("Ingrese su nombre ")
cantvocas=0
cons=0
for i in Nombre:
   
    
    
    if i in "aeiou":
        cantvocas+=1
    elif i == " ":
        print ()
    else:
        cons+=1


print (f"La cantidad de vocales son : {cantvocas}")
print (f"La cantidad de consonantes son : {cons}")