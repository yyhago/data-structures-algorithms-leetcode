# O(n²) - Complexidade Quadrática
# Implementação do algoritmo Bubble Sort.
# Para cada elemento, comparamos com todos os outros elementos,
# resultando em complexidade n².
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # Flag para otimização - se nenhuma troca ocorrer, o array já está ordenado
        swapped = False

        # Última iteração i já colocou os i maiores elementos nas posições corretas
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        # Se nenhuma troca ocorreu na passagem, o array está ordenado
        if not swapped:
            break

    return array


# ========================================
# Implementação do algoritmo Selection Sort.
# Para cada posição, encontramos o menor elemento no restante do array,
# resultando em complexidade n².
def selection_sort(array):
    n = len(array)
    for i in range(n):
        # Encontra o índice do menor elemento na parte não ordenada
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j

        # Troca o elemento encontrado com o primeiro elemento
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


# ========================================
# Função que verifica se existem elementos duplicados em um array.
# Compara cada elemento com todos os outros, resultando em complexidade n².
def has_duplicates(array):
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] == array[j]:
                return True
    return False