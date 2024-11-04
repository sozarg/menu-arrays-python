def validate_number(numero: int | float, minimo: int | float, maximo: int | float) -> bool:
    return numero >= minimo and numero <= maximo

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    for i in range(reintentos):
        numero = input(mensaje)
        numero = int(numero)
        if validate_number(numero, minimo, maximo):
            return numero
        else:
            print(mensaje_error)
    return None

def cantidad_positivos_y_negativos(listas_numeros:list) -> None:
    contador_positivos = 0
    contador_negativos = 0
    for numero in listas_numeros:
        if numero > 0:
            contador_positivos += 1
        elif numero < 0:
            contador_negativos += 1 
    print(f"\nCantidad de numeros positivos: {contador_positivos}\nCantidad de numeros negativos: {contador_negativos}")
    
def mayor_numeros_impares(listas_numeros:list) -> None:
    numero_mayor_impar = None
    for numero in listas_numeros:
        if numero % 2 != 0:
            if numero_mayor_impar == None or numero > numero_mayor_impar:
                numero_mayor_impar = numero
    if numero_mayor_impar == None:
        print("\n No se encontraron numeros impares")
    else:
        print(f"\nEl mayor numero impar es el: {numero_mayor_impar}")