 #generar un rpg simple con sistema de pelea con turnos,mana y vida

import time 
import random 
vida=100
mana=100
ataque_magico=random.randint(1,25)
ataque_normal=random.randint(5,15)
ataque_goblin=random.randint(5,15)
ataque_m2=random.randint(10,35)
vida2=100
print (input("ingrese el nombre de su personaje "))

while vida and vida2 !=0:
    print ("te has encontrado con un enemigo")
    op=int(input("""ingrese la accion que desea hacer 
                 1-. Bola de fuego

                 2- Corte recto 

                 3.- Rayo magico
                 """) )
    if op==1:
        vida2-=ataque_magico
        mana-=5
        print (f"has usado la bola de fuego,el enemigo pierde {ataque_magico} HP,le quedan{vida2} HP " )    
        time.sleep(1)
    vida-=ataque_goblin
    print (f"has recibido {ataque_goblin} puntos de daño, te restan {vida} HP" ) 
if op==2:
    vida2-=ataque_normal
    print (f"has usado el corte recto, el enemigo pierde {ataque_normal} hp,le restan {vida2} HP " ) 
    time.sleep(1)
    vida-=ataque_goblin
    print (f"has recibido {ataque_goblin} puntos de daño, te restan {vida} HP " ) 
if op==3:
    mana-=25
    print (f"has usado el rayo magico, el enemigo recibe {ataque_m2} puntos de daño, le restan {vida2} HP " ) 
    time.sleep(1) 
    vida-=ataque_goblin
    print (f"has recibido {ataque_goblin} puntos de daño,te restan {vida} HP " )    
    if vida>0:
        print (f"has ganado, te restan {vida} HP y {mana} MP " )
    if vida2>0:
        print ("has muerto... Deseas reinciar desde el checkpoint?")