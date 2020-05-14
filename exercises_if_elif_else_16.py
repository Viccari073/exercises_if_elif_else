"""
Faça um programa que mostre ao usuário um menu com 4 opções e opreações matemáticas (as básicas).
O usuário escolhe uma das opções e o seu programa então pede  dois valores numéricos e realiza a operação,
mostrando o resultado e saindo.
"""

print('Escolha uma opção:\n')
print('1 = Soma de dois números.\n')
print('2 = Diferença entre dois números.\n')
print('3 = Produto entre dois números.\n')
print('4 = Divisão entre dois número.\n')

opcao = int(input('Opção: '))

if opcao < 1 or opcao > 4:
    print('Opção iválida.')
else:
    print('Escolha dois números:')
    num1 = int(input('Digite o primerio número: \n'))
    num2 = int(input('Digite o segundo número: \n'))
    if opcao == 1:
        print(f'A soma de {num1} e {num2} é {num1 + num2}')
    elif opcao == 2:
        print(f'A diferença entre {num1} e {num2} é {num1 - num2}')
    elif opcao == 3:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}')
    else:
        opcao == 4
        print(f'A divisão entre {num1} e {num2} é {num1 / num2}')




