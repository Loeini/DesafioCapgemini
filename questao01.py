"""
Questão 01
Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços.
A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.
"""

tamanho = int(input('Insira um número inteiro:\n'))
quantidade = 1

while tamanho >= quantidade:
   print(f'{"*"*quantidade :>{tamanho}}')
   quantidade = quantidade +1