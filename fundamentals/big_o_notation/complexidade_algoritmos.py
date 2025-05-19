# Este arquivo .py é responsável apenas por chamar as funções das principais categorías de complexidade para visualização e estudo
from exemples.constante_o1 import *
from exemples.logaritmico_ologn import *
from exemples.linear_on import *
from exemples.linearitmico_onlogn import *
from exemples.quadratico_on2 import *
from exemples.exponencial_o2n import *
from exemples.fatorial_on import *

print("======= Algoritmo: O(1) =======")
print("constant_time: ")
print(constant_time([4, 5, 3, 8], 2))
print()
print("verify_number: ")
print(verify_number(4))
print("True: Positivo | False: Negativo")
# ====================================================================

print("======= Algoritmo: O(LOG N) =======")
print("binary_search: ")
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print()
print("number_count: ")
print(number_count(400))

# ====================================================================

print("======= Algoritmo: O(N) =======")
print("find_max: ")
print(find_max([4, 2, 9, 7, 5, 1]))
print()
print("linear_search: ")
print(linear_search([4, 2, 9, 7, 5, 1], 7))
print()
print("sum_array: ")
print(sum_array([4, 2, 9, 7, 5, 1]))
# ====================================================================

print("======= Algoritmo: O(N LOG N) =======")
print("merge_sort: ")
print(merge_sort([4, 2, 9, 7, 5, 1]))
print()
print("heap_sort: ")
print(heap_sort([4, 2, 9, 7, 5, 1]))
# ====================================================================

print("======= Algoritmo: O(N²) =======")
print("bubble_sort: ")
print(bubble_sort([4, 2, 9, 7, 5, 1]))
print()
print("selection_sort: ")
print(selection_sort([4, 2, 9, 7, 5, 1]))
print()
print("has_duplicates: ")
print(has_duplicates([4, 2, 9, 7, 5, 1]))
print(has_duplicates([4, 2, 9, 7, 5, 4]))
# ====================================================================

print("======= Algoritmo: O(2^N) =======")
print("fibonacci_recursive: ")
print(fibonacci_recursive(10))
print()
print("tower_of_hanoi: ")
print(tower_of_hanoi(3, 'A', 'B', 'C'))
print()
print("generate_subsets: ")
print(generate_subsets([1, 2, 3]))
# ====================================================================

print("======= Algoritmo: O(N!) =======")
print("generate_permutations: ")
print(generate_permutations([1, 2, 3]))
print()
print("traveling_salesman_brute_force (amostra): ")
# Exemplo simplificado com 4 cidades
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
path, distance = traveling_salesman_brute_force(graph)
print(f"Caminho: {path}, Distância: {distance}")
# ===================================================================="