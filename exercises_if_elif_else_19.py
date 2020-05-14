"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção:
1 - Soma de números.
2 - Diferença entre dois números (mior pelo menos).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser zero).

Opção:

"""
print('Escolha a opção:')
print('1 - Soma de números.')
print('2 - Diferença entre dois números (maior pelo menor).')
print('3 - Produto entre 2 números.')
print('4 - Divisão entre 2 números (o denominador não pode ser zero).')
opcao = int(input('Opção: '))


if opcao == 1:
    print(f'Escolha dois números: ')
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    print(f'A soma de {num1} e {num2} é {num1 + num2}')
elif opcao == 2:
    print(f'Escolha doi números: ')
    num3 = int(input('Primeiro número: '))
    num4 = int(input('Segundo número: '))
    if num3 > num4:
        print(f'A diferença entre {num3} e {num4} é {num3 - num4}')
    else:
        print(f'A diferença entre {num4} e {num3} é {num4 - num3}')
elif opcao == 3:
    print(f'Escolha dois números: ')
    num5 = int(input('Primeiro número: '))
    num6 = int(input('Segundo número: '))
    print(f'O produto entre {num5} e {num6} é {num5 * num6}')
elif opcao == 4:
    print(f'Escolha dois números: ')
    num7 = int(input('Primeiro número: '))
    num8 = int(input('Segundo número: '))
    print(f'A divisão entre {num7} e {num8} é {num7 / num8}')
else:
    print('Opção inválida.')



