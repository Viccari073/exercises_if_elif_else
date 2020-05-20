"""
Usando um switcher, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este numero.
Isto é, Janeiro se 1, Fevereiro se 2 e assim por diante.
"""

# Definir um valor que receba e cheque este valor em um dicionário:

def switcher(valor):
    switcher = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    return switcher.get(valor, 'Não encontrei o mês correspondente.')


mes = int(input('Informe um número referente ao mês do ano:'))

print(switcher(mes))
