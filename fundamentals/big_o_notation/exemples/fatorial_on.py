# O(n!) - Complexidade Fatorial
# Gera todas as permutações possíveis de um array.
# Para n elementos, existem n! permutações possíveis.
def generate_permutations(elements):
    if len(elements) <= 1:
        return [elements]

    result = []
    for i, current in enumerate(elements):
        # Remove o elemento atual e gera permutações para os elementos restantes
        remaining_elements = elements[:i] + elements[i + 1:]
        for perm in generate_permutations(remaining_elements):
            # Adiciona o elemento atual no início de cada permutação
            result.append([current] + perm)

    return result


# ========================================
# Solução por força bruta para o problema do caixeiro viajante.
# Verifica todas as permutações possíveis para encontrar o caminho mais curto.
def traveling_salesman_brute_force(graph):
    # graph é uma matriz de adjacência onde graph[i][j] é a distância da cidade i para j
    n = len(graph)
    # Cidades de 1 a n-1 (excluindo a cidade 0 que é o ponto de partida)
    cities = list(range(1, n))

    min_path = None
    min_distance = float('inf')

    # Gera todas as permutações possíveis das cidades
    for perm in generate_permutations(cities):
        # Adiciona a cidade de origem no início e no fim
        path = [0] + perm + [0]

        # Calcula a distância total
        distance = 0
        for i in range(len(path) - 1):
            distance += graph[path[i]][path[i + 1]]

        # Atualiza se encontrou um caminho mais curto
        if distance < min_distance:
            min_distance = distance
            min_path = path

    return min_path, min_distance


# ========================================
# Resolução do problema de alocação de tarefas.
# Atribui n tarefas a n trabalhadores de forma a minimizar o custo total.
def assignment_problem(cost_matrix):
    n = len(cost_matrix)
    # Lista de índices de trabalhadores
    workers = list(range(n))

    min_cost = float('inf')
    min_assignment = None

    # Gera todas as permutações possíveis de atribuições
    for perm in generate_permutations(workers):
        # Calcula o custo total para esta atribuição
        total_cost = 0
        for i in range(n):
            total_cost += cost_matrix[i][perm[i]]

        # Atualiza se encontrou uma atribuição de menor custo
        if total_cost < min_cost:
            min_cost = total_cost
            min_assignment = perm

    return min_assignment, min_cost