# Complexidade de Algoritmos e Big O Notation

## O que é Big O Notation?

A notação Big O é uma ferramenta matemática usada para descrever o comportamento limitante de uma função quando o argumento tende a um valor específico ou infinito. No contexto de algoritmos, é utilizada para classificar algoritmos de acordo com como seu tempo de execução ou requisitos de espaço crescem conforme o tamanho da entrada aumenta.

A notação Big O nos ajuda a responder perguntas como:
- Quão bem o algoritmo se escalará?
- O algoritmo é eficiente para entradas grandes?
- Qual algoritmo é mais eficiente para resolver um problema específico?

## Principais Categorias de Complexidade

### 1. O(1) - Complexidade Constante

**Definição**: O tempo de execução permanece o mesmo, independentemente do tamanho da entrada.

**Características**:
- O algoritmo executa em tempo constante
- O número de operações não aumenta com o tamanho da entrada
- É a complexidade mais eficiente possível

**Exemplos comuns**:
- Acesso a um elemento em um array por índice
- Inserção/remoção no início ou fim de uma lista ligada
- Operações push/pop em uma pilha
- Verificar se um número é par ou ímpar

### 2. O(log n) - Complexidade Logarítmica

**Definição**: O tempo de execução cresce de forma logarítmica em relação ao tamanho da entrada.

**Características**:
- Muito eficiente mesmo para entradas grandes
- Geralmente envolve algoritmos que dividem o problema pela metade a cada etapa
- A base do logaritmo normalmente é 2 (divisão pela metade)

**Exemplos comuns**:
- Busca binária
- Operações em árvores binárias balanceadas
- Alguns algoritmos de divisão e conquista
- Algoritmos que reduzem o problema pela metade a cada passo

### 3. O(n) - Complexidade Linear

**Definição**: O tempo de execução cresce linearmente com o tamanho da entrada.

**Características**:
- O número de operações é diretamente proporcional ao tamanho da entrada
- Cada elemento da entrada precisa ser processado pelo menos uma vez

**Exemplos comuns**:
- Percorrer um array
- Busca linear em uma lista
- Encontrar o valor máximo/mínimo em um array não ordenado
- Operações sobre cada elemento de uma coleção

### 4. O(n log n) - Complexidade Linearítmica

**Definição**: O tempo de execução é proporcional a n multiplicado pelo logaritmo de n.

**Características**:
- Mais lento que O(n), mas muito mais rápido que O(n²)
- Comum em algoritmos eficientes de ordenação
- Frequentemente resultado de algoritmos que combinam uma etapa linear com uma etapa logarítmica

**Exemplos comuns**:
- Merge Sort
- Heap Sort
- Quick Sort (caso médio)
- Algoritmos eficientes de ordenação

### 5. O(n²) - Complexidade Quadrática

**Definição**: O tempo de execução é proporcional ao quadrado do tamanho da entrada.

**Características**:
- Para cada elemento na entrada, o algoritmo executa operações proporcionais a n
- Geralmente envolve loops aninhados
- Se torna ineficiente rapidamente à medida que n cresce

**Exemplos comuns**:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Comparar cada elemento com todos os outros elementos

### 6. O(2^n) - Complexidade Exponencial

**Definição**: O tempo de execução dobra com cada adição à entrada.

**Características**:
- Cresce muito rapidamente
- Geralmente resulta de algoritmos que geram todas as combinações/subconjuntos
- Praticamente inviável para entradas maiores que 20-30

**Exemplos comuns**:
- Algoritmos que soluciona o problema da torre de Hanói
- Fibonacci recursivo ingênuo
- Algoritmos que enumeram todos os subconjuntos
- Solução por força bruta de problemas NP-completos

### 7. O(n!) - Complexidade Fatorial

**Definição**: O tempo de execução cresce de acordo com o fatorial do tamanho da entrada.

**Características**:
- Cresce extremamente rápido
- Geralmente resulta de algoritmos que geram todas as permutações
- Praticamente inviável para entradas maiores que 10-12

**Exemplos comuns**:
- Problema do caixeiro viajante por força bruta
- Algoritmos que geram todas as permutações
- Solução por força bruta de alguns problemas de otimização combinatória

## Como Identificar a Complexidade de um Algoritmo

1. **Análise de loops**:
   - Um único loop que percorre a entrada: geralmente O(n)
   - Loops aninhados: multiplicar as complexidades (ex: dois loops = O(n²))
   - Loop que divide o problema pela metade: geralmente O(log n)

2. **Análise de recursão**:
   - Identifique o número de chamadas recursivas
   - Determine o trabalho feito em cada chamada
   - Combine essas informações usando a relação de recorrência

3. **Regras práticas**:
   - Ignore constantes: O(2n) é simplificado para O(n)
   - Mantenha apenas o termo de maior crescimento: O(n² + n) é simplificado para O(n²)
   - Verifique o "pior caso" para análise conservadora

4. **Observe padrões comuns**:
   - Divisão do problema pela metade: provavelmente O(log n)
   - Percorrer todos os elementos: provavelmente O(n)
   - Comparar cada elemento com cada outro: provavelmente O(n²)
   - Algoritmos de ordenação eficientes: provavelmente O(n log n)

## Dicas para Otimização

1. **Conheça as estruturas de dados**:
   - Diferentes estruturas têm diferentes complexidades para operações comuns
   - Escolha a estrutura adequada ao problema

2. **Simplificação do problema**:
   - Às vezes um algoritmo mais simples com complexidade maior é preferível para entradas pequenas

3. **Compromisso espaço-tempo**:
   - Algumas otimizações de tempo requerem mais espaço
   - Considere as restrições de memória

4. **Identifique operações redundantes**:
   - Uso de memorização e programação dinâmica
   - Estruturas de dados indexadas para operações frequentes

5. **Análise amortizada**:
   - Algumas operações podem ser caras ocasionalmente, mas baratas na média
   - Exemplo: redimensionamento de arrays dinâmicos