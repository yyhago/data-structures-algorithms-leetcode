# Binary Search (Pesquisa Binária)

Este diretório contém uma implementação em Python do algoritmo de **Pesquisa Binária**, também conhecido como **Binary Search**.

## 📌 Descrição

A pesquisa binária é um algoritmo eficiente para encontrar um elemento em uma **lista ordenada**. Ela funciona dividindo a lista repetidamente ao meio, eliminando metade dos elementos a cada passo.

- **Pré-requisito:** A lista deve estar **ordenada**.
- **Complexidade:** O(log n) no pior caso.
- **Paradigma:** Divisão e conquista.

## 🚀 Funcionamento

1. Define o intervalo de busca (início e fim da lista).
2. Calcula o ponto médio e compara com o valor buscado.
3. Se o valor for igual ao do meio, retorna o índice.
4. Caso contrário, repete o processo com a metade apropriada da lista.
5. Retorna `None` se o valor não for encontrado.

## 🧪 Exemplo de uso

```python
from binary_search import pesquisa_binaria

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))   # Saída: 1
print(pesquisa_binaria(minha_lista, -1))  # Saída: None
