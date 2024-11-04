
from package_input.Array_Generales import *
from package_input.Especificas import *

def menu_opciones(listas_numeros:int ) -> None:
    while True:
        opcion = int(input("\n--- Menu de opciones ---\n-Elija una opcion\n--1) Mostrar la cantidad de numeros positivos y negativos\n--2) Mostrar la sumatoria de los numeros pares.\n--3) Informar el mayor de los numeros impares.\n--4) Listar todos los numeros ingresados.\n--5) Listar todos los numeros pares.\n--6) Listar los numeros de las posiciones impares.\n--7) Salir\n"))
        match opcion:
            case 1:
                cantidad_positivos_y_negativos(listas_numeros)
            case 2:
                sumatoria_pares(listas_numeros)
            case 3:
                mayor_numeros_impares(listas_numeros)
            case 4:
                listar_numeros(listas_numeros)
            case 5:
                listar_numeros_pares(listas_numeros)
            case 6:
                listar_numeros_posicion_impar(listas_numeros)
            case 7:
                print("Usted eligió salir del programa")
                break

listas_numeros = ingresar_numeros()
menu_opciones(listas_numeros)