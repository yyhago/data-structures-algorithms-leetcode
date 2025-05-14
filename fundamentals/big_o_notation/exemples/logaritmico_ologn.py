# O(log n) - Complexidade Logarítmica
# Implementação de busca binária em um array ordenado.
# A cada iteração, dividimos o tamanho do problema pela metade, resultando em complexidade logarítmica.

def binary_search(array, target):

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

# ========================================
# Conta o número de dígitos em um número.
# A cada divisão por 10, estamos efetivamente dividindo o problema por um fator constante.

def number_count(number):

    if number == 0:
        return 1

    count = 0
    num_abs = abs(number)

    while num_abs > 0:
        count += 1
        num_abs //= 10

    return count