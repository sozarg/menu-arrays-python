from package_input.Especificas import *

def ingresar_numeros():
    listas_numeros = [0] * 10
    for i in range(10):
        numero = get_int("Ingresa un número entre -1000 y 1000: ", "Número no válido. Intenta de nuevo.", -1000, 1000, 3)
        listas_numeros[i] = numero  
    return listas_numeros

def sumatoria_pares(listas_numeros:list) -> None:
    sumatoria = 0
    for numero in listas_numeros:
        if numero % 2 == 0:
            sumatoria += numero
    print(f"\nLa sumatoria de todos los pares da como resultado: {sumatoria}")

def listar_numeros(listas_numeros: list) -> None:
    print(f"\n Numeros listados: {listas_numeros}")

def listar_numeros_pares(listas_numeros: list) -> None:
    listas_numeros_pares = []
    for numero in listas_numeros:
        if numero % 2 == 0:
            listas_numeros_pares += [numero]
    print(f"Numeros pares listados: {listas_numeros_pares}")

def listar_numeros_posicion_impar(listas_numeros: list) -> None:
    lista_impar_posicion = []
    for i in range(len(listas_numeros)):
        if i % 2 != 0:
            lista_impar_posicion += [i]
    print(f"Numeros impares listados {lista_impar_posicion}")