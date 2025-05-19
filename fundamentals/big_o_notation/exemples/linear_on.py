# O(n) - Complexidade Linear
# Percorre todos os elementos de um array para encontrar o valor máximo.
# O tempo de execução cresce linearmente com o tamanho da entrada.
def find_max(array):
    if not array:
        return None
    max_value = array[0]
    for element in array:
        if element > max_value:
            max_value = element
    return max_value

# ========================================
# Busca linear em um array para encontrar um elemento específico.
# Precisa verificar cada elemento até encontrar o alvo.
def linear_search(array, target):
    for i, element in enumerate(array):
        if element == target:
            return i  # Retorna o índice do elemento encontrado
    return -1  # Retorna -1 se o elemento não for encontrado
# ========================================
# Calcula a soma de todos os elementos em um array.
# Precisa processar cada elemento exatamente uma vez.
def sum_array(array):
    total = 0
    for element in array:
        total += element
    return total