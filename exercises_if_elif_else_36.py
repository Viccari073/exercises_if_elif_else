"""
Escreva um programa que, dado o valor da venda, imprima a comissão ue deverá ser paga ao vendedor.
Para calcular a comissão, considere a tabela abaixo:

Venda mensal                                                                Comissão
Maior ou igual a R$ 100.000,00                                              R$ 700,00 + 16% da vendas
Menor que R$ 100.000,00 e maior ou igual a R$ 80.000,00                     R$ 650,00 + 14% das vendas
Menor que R$ 80.000,00 e maior ou igual a R$ 60.000,00                      R$ 600,00 + 14% das vendas
Menor que R$ 60.000,00 e maior ou igual a R$ 40.000,00                      R$ 550,00 + 14% das vendas
Menor que R$ 40.000,00 e maior ou igual a R$ 20.000,00                      R$ 500,00 + 14% das vendas
Menor que R$ 20.000,00                                                      R$ 400,00 + 14% das vendas

"""

venda_mensal = float(input('Digite o valor da venda mensal: R$ '))

if venda_mensal >= 100_000.00:
    print(f'Sua comissão é de R${700.00 + (venda_mensal * (16 / 100)): .2f}')
elif 80_000.00 <= venda_mensal < 100_000.00:
    print(f'Sua comissão é de R${650.00 + (venda_mensal * (14 / 100)): .2f}')
elif 60_000.00 <= venda_mensal < 80_000.00:
    print(f'Sua comissão é de R${600.00 + (venda_mensal * (14 / 100)): .2f}')
elif 40_000.00 <= venda_mensal < 60_000.00:
    print(f'Sua comissão é de R${550.00 + (venda_mensal * (14 / 100)): .2f}')
elif 20_000.00 <= venda_mensal < 40_000.00:
    print(f'Sua comissão é de R${500.00 + (venda_mensal * (14 / 100)): .2f}')
else:
    print(f'Sua comissão é de R${400.00 + (venda_mensal * (14 / 100)): .2f}')
