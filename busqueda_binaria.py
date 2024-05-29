import time

def search_binary(lista, low, high, x):
    if high >= low: # si el índice del último elemento es mayor o igual al índice del primer elemento
        mid = (high + low) // 2 # obtiene el índice del elemento del medio
        if lista[mid] == x: # si el elemento del medio es igual a x entonces devuelve el índice del elemento
            return mid 
        elif lista[mid] > x: # si el elemento del medio es mayor a x entonces busca en la mitad izquierda
            return search_binary(lista, low, mid - 1, x)
        else: # si el elemento del medio es menor a x entonces busca en la mitad derecha
            return search_binary(lista, mid + 1, high, x)
    else:
        return 'No encontrado'

def test_search_binary():
    # datasets contiene listas de enteros y un entero x a buscar en la lista
    datasets = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        ([10, 20, 30, 40, 50], 30),
        ([1, 2, 3, 4, 5], 10),
        (list(range(1000)), 999),
        (list(range(10000)), -1)
    ]

    for lista, x in datasets: # itera sobre los elementos de datasets
        inicio = time.time()
        resultado = search_binary(lista, 0, len(lista) - 1, x)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"search_binary({x}) en lista de tamaño {len(lista)}: {resultado}, Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")

test_search_binary()