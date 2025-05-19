# O(n log n) - Complexidade Linearítmica
# Implementação do algoritmo Merge Sort.
# Divide o array pela metade repetidamente (log n) e depois combina (n),
# resultando em complexidade n log n.
def merge_sort(array):
    if len(array) <= 1:
        return array

    # Divide o array ao meio
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # Combina as duas metades ordenadas
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Combina os dois arrays ordenados
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Adiciona os elementos restantes
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ========================================
# Implementação simplificada do Heap Sort
# O Heap Sort tem complexidade O(n log n) tanto no melhor quanto no pior caso
def heap_sort(array):
    n = len(array)

    # Constrói um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extrai elementos um por um
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Troca
        heapify(array, i, 0)

    return array


def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Verifica se o filho esquerdo existe e é maior que a raiz
    if left < n and array[left] > array[largest]:
        largest = left

    # Verifica se o filho direito existe e é maior que a raiz
    if right < n and array[right] > array[largest]:
        largest = right

    # Troca e continua heapificando se necessário
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)