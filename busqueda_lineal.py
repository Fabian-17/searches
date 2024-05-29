import time

def search_linear(lista, x):
    for ix, i in enumerate(lista): # itera sobre los elementos de la lista y devuelve el índice y el valor
        if i == x: # si el valor es igual a x entonces devuelve el índice
            return ix 
    return 'No encontrado' # si no se encuentra x en la lista devuelve 'No encontrado'

def test_search_linear():
    # datasets contiene listas de enteros y un entero x a buscar en la lista
    datasets = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        ([10, 20, 30, 40, 50], 30),
        ([1, 2, 3, 4, 5], 10),
        (list(range(1000)), 999),
        (list(range(10000)), -1)
    ]

    for lista, x in datasets: # itera sobre los elementos de datasets
        inicio = time.time() # tiempo de inicio
        resultado = search_linear(lista, x) # ejecuta la función search_linear
        fin = time.time() # tiempo de fin
        tiempo_ejecucion = fin - inicio # tiempo de ejecución
        print(f"search_linear({x}) en lista de tamaño {len(lista)}: {resultado}, Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")

test_search_linear() # ejecuta la función test_search_linear