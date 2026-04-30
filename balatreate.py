
import random

codigo=random.randint(7000,21000)
op=0
while op !=4:
	print("""
 1.- Cancha vip $40.000
 2.- Tribuna $40.000
 3.- cancha general $40.000
 4.- Salir
 """)
op=int (input ("seleccione su opcion ") )
print (codigo)
match op:
	case 1 :
		print (" usted selecciono cancha vip el precio a pagar es " , 40.000*1.8 )
		
            