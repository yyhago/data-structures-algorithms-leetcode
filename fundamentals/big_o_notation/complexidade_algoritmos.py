# Este arquivo .py é responsável apenas por chamar as funções das principais categorías de complexidade para visualização e estudo

from exemples.constante_o1 import *
from exemples.logaritmico_ologn import *



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