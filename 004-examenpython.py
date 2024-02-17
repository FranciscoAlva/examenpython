import mysql.connector

conexion = mysql.connector.connect (
    host="localhost",
    user="examenpython",
    password="examenpython",
    database="examenpython",
    )

cursor = conexion.cursor()

def menu():
    print("Programa de clientes")
    print("Selecciona una opcion")
    print("1.-Insertar nuevo cliente")
    print("2.-Listado de clientes")
    print("3.-Actualizar un cliente")
    print("4.-Eliminar un cliente")
    print("5.-Buscar un cliente")
    print("6.-Salir")
    opcion = input("Opcion: ")
    if opcion == "1":
        print("Insertar cliente")
    elif opcion == "2":
        print("Lista de clientes")
    elif opcion == "3":
        print("Actualiza un cliente")
    elif opcion == "4":
        print("Elimina un clientes")
    elif opcion == "5":
        print("Buscar cliente")
    elif opcion == "6":
        print("Salir")
    menu()
             
menu()
