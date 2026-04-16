notas=int (input (" Ingrese la cantidad de notas a promediar "))
suma=0
for i in range (notas):
    n=float (input (f"Ingrese la nota  ({i+1}) "))
    suma=suma+n
prom=suma/notas
print ( "el promedio de las notas es : ",round (prom,1) )
if prom>4:
    print ("el alumno ha aprobado ")
else:
    print ("el alumno ha reprobado")
