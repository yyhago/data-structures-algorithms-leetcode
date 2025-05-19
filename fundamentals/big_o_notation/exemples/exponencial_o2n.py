# O(2^n) - Complexidade Exponencial
# Implementação recursiva ingênua da sequência de Fibonacci.
# Cada chamada resulta em duas chamadas adicionais, criando uma árvore binária,
# resultando em complexidade 2^n.

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ========================================
# Solução para o problema da Torre de Hanói.
# Para mover n discos, precisamos fazer 2^n - 1 movimentos.
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        # Movimento básico: mover um disco da origem para o destino
        return [(source, target)]

    # Movimentos recursivos
    moves = []
    # 1. Mover n-1 discos da origem para auxiliar, usando o destino como auxiliar
    moves.extend(tower_of_hanoi(n - 1, source, target, auxiliary))
    # 2. Mover o disco restante da origem para o destino
    moves.append((source, target))
    # 3. Mover n-1 discos do auxiliar para o destino, usando a origem como auxiliar
    moves.extend(tower_of_hanoi(n - 1, auxiliary, source, target))

    return moves


# ========================================
# Gera todos os subconjuntos de um conjunto.
# Para n elementos, existem 2^n subconjuntos possíveis.
def generate_subsets(elements):
    if not elements:
        return [[]]

    # Pega o primeiro elemento
    first = elements[0]
    # Gera subconjuntos sem o primeiro elemento
    subsets_without_first = generate_subsets(elements[1:])
    # Gera subconjuntos com o primeiro elemento
    subsets_with_first = []
    for subset in subsets_without_first:
        subsets_with_first.append([first] + subset)

    # Combina todos os subconjuntos
    return subsets_without_first + subsets_with_first