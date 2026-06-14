def ivacalc(neto,tasa=0.19):
    iva= neto*tasa
    total=neto+iva
    return iva,total


print ("ingrese el valor neto de su prodcuto para agregarle el IVA")

valor=int(input("ingrese el valor"))


resultado=ivacalc(valor)


print (resultado)    