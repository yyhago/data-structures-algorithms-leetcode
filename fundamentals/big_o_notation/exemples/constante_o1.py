# O(1) - Complexidade Constante
# Acesso a um elemento específico de um array.
# Não importa o tamanho do array, acessar um elemento por índice sempre leva o mesmo tempo.

def constant_time(array, index):

    if 0 <= index < len(array):
        return array[index]

    return None

# ========================================
# Verifica se um número é par ou ímpar.
# Esta operação executa em tempo constante porque o número de operações não depende do tamanho da entrada.

def verify_number(number):

    return number % 2 == 0

print(verify_number(5))