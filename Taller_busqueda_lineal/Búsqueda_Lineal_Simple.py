def busqueda_lineal_simple(lista, elemento):
    """
    Busca un elemento en una lista usando búsqueda lineal
    
    Args:
        lista: Lista de elementos
        elemento: Elemento a buscar
    
    Returns:
        int: Índice del elemento si se encuentra, -1 si no
    """
    # Recorremos cada elemento de la lista
    for i in range(len(lista)):
        # Comparamos el elemento actual con el que buscamos
        if lista[i] == elemento:
            # Si encontramos el elemento, retornamos su índice
            return i
    
    # Si llegamos aquí, el elemento no está en la lista
    return -1

# Pruebas
numeros = [64, 34, 25, 12, 22, 11, 90]
print(busqueda_lineal_simple(numeros, 25))  # Debe retornar 2
print(busqueda_lineal_simple(numeros, 99))  # Debe retornar -1

# Pruebas adicionales
print(busqueda_lineal_simple(numeros, 64))  # Debe retornar 0 (primer elemento)
print(busqueda_lineal_simple(numeros, 90))  # Debe retornar 6 (último elemento)
print(busqueda_lineal_simple(numeros, 12))  # Debe retornar 3 (elemento del medio)

# Prueba con lista vacía
print(busqueda_lineal_simple([], 5))       # Debe retornar -1

# Prueba con elementos repetidos
numeros_repetidos = [1, 2, 3, 2, 4]
print(busqueda_lineal_simple(numeros_repetidos, 2))  # Debe retornar 1 (primera ocurrencia)

#¿Cuál es la complejidad temporal ?
# La complejidad temporal de la búsqueda lineal es O(n), donde n es el número de elementos en la lista.
 
# ¿En qué casos la búsqueda lineal es eficiente?        
# La búsqueda lineal es eficiente para listas pequeñas o cuando los elementos están distribuidos de manera uniforme.
                         
#¿Cuándo sería mejor usar otro algoritmo de búsqueda?
# Sería mejor usar otro algoritmo de búsqueda, como la búsqueda binaria, cuando la lista está ordenada y es grande, ya que la búsqueda binaria tiene una complejidad temporal de O(log n).


