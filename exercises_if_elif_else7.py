"""
Faça um programa que receba dois números e mostre o maior. Se por acaso os dois números forem iguais,
imprima a mensagem: Números Iguais
"""

num1 = int(input('Escreva um número: \n'))
num2 = int(input('Escreva outro número: \n'))

if num1 == num2:
    print('Números iguais.')
elif num1 > num2:
    print(f'O número {num1} é o maior.')
else:
    print(f'O número {num2} é o maior.')





