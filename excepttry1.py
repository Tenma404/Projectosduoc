while True:
    try:
        print ("""
1-.  Suma
2.- Resta
3-. Multiplicacion 
4.- Division""")
        op=int(input("ingrese la opcion que desea realizar"))
        if op==1:
            print ("ingrese los digitos a sumar")
            num1=int(input(""))
            num2=int(input(""))
            suma=num1+num2
            print (f"la suma de los digitos es {suma}")
        elif op==2:
            print ("ingrese los dos digitos a restar")
            num3=int(input(""))
            num4=int(input(""))
            res=num3-num4
            print (f"el resultado de la resta es {res}")
        elif op==3:
            print ("ingrese los digitos a multiplicar")
            num5=int(input(""))
            num6=int(input(""))
            multi=num5*num6
            print (f"el resultado de la multiplicacion es {multi}")
        elif op==4:
            print ("ingrese los dos digitos a dividir ")
            num7=int(input(""))
            num8=int(input(""))
            div=num7/num8
            print (f"el resultado de la division es {div}")
            break
        else:
            print("Opcion no valida")
    except Exception:
        print ("solo se pueden ingresar numeros,intente nuevamente ")


