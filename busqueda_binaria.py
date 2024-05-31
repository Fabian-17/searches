import time
import psutil

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
    
def analizar_recursos():
    proceso = psutil.Process()
    uso_cpu = proceso.cpu_percent(interval=None)
    uso_memoria = proceso.memory_info().rss / (1024 * 1024)  # Convierte a MB
    return uso_cpu, uso_memoria

def test_search_binary():
    # datasets contiene listas de enteros y un entero x a buscar en la lista
    datasets = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        ([10, 20, 30, 40, 50], 30),
        ([1, 2, 3, 4, 5], 10),
        (list(range(1000)), 999),
        (list(range(10000000)), 41241)
    ]

    for lista, x in datasets: # itera sobre los elementos de datasets
        uso_cpu_inicio, uso_memoria_inicio = analizar_recursos() # recursos al inicio
        inicio = time.time()
        resultado = search_binary(lista, 0, len(lista) - 1, x)
        fin = time.time()
        uso_cpu_fin, uso_memoria_fin = analizar_recursos() # recursos al fin
        tiempo_ejecucion = fin - inicio # tiempo de ejecución
        uso_cpu = uso_cpu_fin - uso_cpu_inicio
        uso_memoria = uso_memoria_fin - uso_memoria_inicio

        print(f"search_binary({x}) en lista de tamaño {len(lista)}: {resultado}, Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")
        print(f"Uso de CPU: {uso_cpu:.2f}%, Uso de memoria: {uso_memoria:.2f} MB\n")

# Repite el experimento para obtener mediciones más estables
def repetir_test():
    for _ in range(10):
        test_search_binary()

repetir_test() # ejecuta la función repetir_test