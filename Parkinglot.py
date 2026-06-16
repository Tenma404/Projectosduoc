# Estacionamiento: 4 pisos, 10 espacios por piso

parking = {
    1: [2000, 3500, 2000, 2000, 3500, 2000, 2000, 3500, 2000],
    2: [],
    3: [],
    4: []
}


# def inicializar_estacionamiento():
#     for piso in parking:
#         while len(parking[piso]) < 10:
#             parking[piso].append(0)


# def ingresar_vehiculo():
#     print("\nTIPOS DE VEHÍCULO")
#     print("1. Ligero ($2000)")
#     print("2. Mediano ($3000)")
#     print("3. Pesado ($3500)")

#     opcion = input("Seleccione tipo: ")

#     if opcion == "1":
#         valor = 2000
#     elif opcion == "2":
#         valor = 3000
#     elif opcion == "3":
#         valor = 3500
#     else:
#         print("Tipo inválido.")
#         return

#     for piso in parking:
#         for espacio in range(10):
#             if parking[piso][espacio] == 0:
#                 parking[piso][espacio] = valor
#                 print(f"Vehículo estacionado en piso {piso}, espacio {espacio + 1}")
#                 return

#     print("No hay espacios disponibles.")


# def contar_ganancias():
#     total = 0

#     for piso in parking:
#         total += sum(parking[piso])

#     print(f"\nGanancias acumuladas: ${total}")


# def contar_vehiculos():
#     cantidad = 0

#     for piso in parking:
#         for espacio in parking[piso]:
#             if espacio != 0:
#                 cantidad += 1

#     print(f"\nVehículos estacionados: {cantidad}")


# def mostrar_estacionamiento():
#     print("\nESTADO DEL ESTACIONAMIENTO")
#     for piso in parking:
#         print(f"Piso {piso}: {parking[piso]}")


# def menu():
#     print("\n=== MENÚ ESTACIONAMIENTO ===")
#     print("1.- Ingresar vehículo")
#     print("2.- Contar ganancias")
#     print("3.- Contar vehículos")
#     print("4.- Mostrar estacionamiento")
#     print("5.- Salir")

#     opcion = input("Seleccione una opción: ")

#     if opcion == "1":
#         ingresar_vehiculo()
#         menu()  

#     elif opcion == "2":
#         contar_ganancias()
#         menu()

#     elif opcion == "3":
#         contar_vehiculos()
#         menu()

#     elif opcion == "4":
#         mostrar_estacionamiento()
#         menu()

#     elif opcion == "5":
#         print("Programa finalizado.")

#     else:
#         print("Opción inválida.")
#         menu()


# # Programa principal
# inicializar_estacionamiento()
# menu()