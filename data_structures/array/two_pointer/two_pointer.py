# Técnica usada para resolver algoritmos em cima de array de caracteres.
# two_pointer = Inicializar dois ponteiros (inicio e fim) para não alocar espaços adicionais na memória, assim apontando ao local precisamente

print("Exemplo:")


            #L                           #R
my_array = ["y", "m" , "" , "c" , "a" , "r"]
print(my_array)


# Para resolver este problema temos que inicializar nossos ponteiros juntos no começo.
# E assim andaremos apenas para a direira (R - Right), e quando achar o espaço em branco ele volta uma casa e troca os caracteres com o ponteiro inicial (L), até chegar no final.

           #L#R
my_array = ["y", "m" , "" , "c" , "a" , "r"]

           #L    #R
my_array = ["y", "m" , "" , "c" , "a" , "r"]

           #L          #R
my_array = ["y", "m" , "" , "c" , "a" , "r"]

           #L     #R
my_array = ["y", "m" , "" , "c" , "a" , "r"]

           #L     #R
my_array = ["m", "y" , "" , "c" , "a" , "r"]

# O algoritmo acaba quando L e R se encontram/cruzam, pois cumpriu seu propósito (inverter a parte necessária).



