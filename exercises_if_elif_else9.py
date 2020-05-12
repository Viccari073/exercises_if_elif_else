"""
Leia o salário de um tabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário, imprima: Empréstimo não concedido.
Caso contrário, imprima: Empréstimo concedido.
"""

salario = float(input('Qual seu salário:'))
prestacao = float(input('Qual o valor da prestação:'))

if prestacao < salario * 20/100:
    print('Empréstimo concedido.')
else:
    print('Empréstmo não concedido.')


