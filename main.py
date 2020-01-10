# Consola para aprender Python practico :P
import os
# import subprocess
import functions.funciones_ as fun

# MENU PERSISTENTE EL BUCLE WHILE


# MENU PERSISTENTE INTERACTUABLE
while True: 
    # LLAMADO AL MENU
    fun.menusit()
    opcion = int(input("Ingrese en que desea entrar: "))

    if opcion == 1: 
        os.system("cls") # Para limpiar en linux "clear"
        # llamada al contenido de variables
        fun.varia()
        input("> Presiona ENTER para continuar...")
    elif opcion == 2:
        os.system("cls") # Limpia pantalla
        # LLAMADO AL TIPO DE DATOS
        fun.tipo()
        input("> Presione ENTER para continuar...")
    elif opcion == 3:
        # AÚN NO DEFINIDO
        pass 
    elif opcion == 4: 
        # Limpiar consola
        os.system("cls")
        input("Elegiste SALIR, presiona ENTER para salir.")
        #.terminate()
        break 