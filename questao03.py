"""
Questão 03
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra.
Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.
"""

anagrama = input('Insira uma palavra:\n')

a = 0
list = []
for i in anagrama:
    for j in anagrama:
        if i == j:
            x = anagrama[anagrama.index(i)]
            y = anagrama[anagrama.index(j)]
            list = list + [x, y]
            print(list)
        else:
            pass
