"""
Determine se um documento ano lido é bissexto. Sendo que um ano é bissexto quando se for divisível por 400 ou se for
divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992 e 1996
"""

ano = int(input('Digite o ano: '))

ano1 = ano % 400
ano2 = ano % 4
ano3 = ano % 100

if ano1 == 0:
    print('Esse ano é bissexto.')
elif ano1 == 0 or (ano2 == 0 and ano3 != 0):
    print('Esse ano é bissexto.')
elif ano1 != 0:
    print('Esse ano não é bissexto.')
