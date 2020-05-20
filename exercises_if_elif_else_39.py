"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor e dos impostos.
A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo.
Leia o custo de fábrica e escreva o custo ao consumidor.

Custo de fábrica                   % do distribuidor                  % dos impostos
até R$ 12000,00                            5                               isento
entre R$ 12000,00 e R$ 25000,00            10                                 15
acima de R$25000,00                        15                                 20
"""

custo_fabrica = float(input('Digite o valor do custo de fábrica: R$'))

distribuidor = 0
impostos = 0
valor_final = 0

while not custo_fabrica > 0:
    print('Custo inválido! Digite um valor válido.')
    custo_fabrica = float(input('Digite o valor do custo de fábrica: R$'))

if custo_fabrica <= 12_000:
    distribuidor = custo_fabrica * (5/100)
    valor_final = custo_fabrica + distribuidor
    print(f'O valor do carro novo é R${valor_final: .2f}')
elif 12_000 < custo_fabrica <= 25_000:
    distribuidor = custo_fabrica * (10/100)
    impostos = custo_fabrica * (15/100)
    valor_final = custo_fabrica + distribuidor + impostos
    print(f'O valor do carro novo é R${valor_final: .2f}')
else:
    distribuidor = custo_fabrica * (15/100)
    impostos = custo_fabrica * (20/100)
    valor_final = custo_fabrica + distribuidor + impostos
    print(f'O valor do carro novo é R${valor_final: .2f}')





