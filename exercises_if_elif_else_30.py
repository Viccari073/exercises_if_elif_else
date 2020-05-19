"""
Um produto vai sofrer aumento de acordo com a tabela abaixo.
Leia o preço antigo e escreva o preço novo e escreva uma mensagem em função do preço novo,
de acordo com a tabela abaixo:

Preço antido             Percentual de aumento                Preço Novo                             Mensagem
até R$ 50,00                       5%                         até R$ 80,00                            Barato
entre R$ 50,00 e R$ 100,00        10%                         entre R$ 80,00 e R$120,00 (inclusive)   Normal
acima de R$ 100,00                15%                         entre R$ 120,00 e R$ 200,00 (inclusive) Caro
                                                              acima de R$ 200,00                      Muito caro
"""
print('Escreva o valor do produto: ')
preco_antigo = float(input('R$ '))

preco_novo = 0

if preco_antigo < 50.00:
    preco_novo = preco_antigo + preco_antigo * (5/100)
    print(f'Esse produto sofreu alteração de 5% e agora custa R$ {preco_novo}')
    print('Barato')

elif 50.00 <= preco_antigo <= 100.00:
    preco_novo = preco_antigo + preco_antigo * (10/100)
    if preco_novo < 80.00:
        print(f'Esse produto sofreu alteração de 10% e agora custa R$ {preco_novo}')
        print('Barato')
    elif 80.00 <= preco_novo <= 120.00:
        print(f'Esse produto sofreu alteração de 10% e agora custa R$ {preco_novo}')
        print('Normal')
elif preco_antigo > 100.00:
    preco_novo = preco_antigo + preco_antigo * (15 / 100)
    if 80.00 <= preco_novo <= 120.00:
        print(f'Esse produto sofreu alteração de 15% e agora custa R$ {preco_novo}')
        print('Normal')
    elif 120.00 <= preco_novo <= 200.00:
        print(f'Esse produto sofreu alteração de 15% e agora custa R$ {preco_novo}')
        print('Caro')
    elif preco_novo > 200.00:
        print(f'Esse produto sofreu alteração de 15% e agora custa R$ {preco_novo}')
        print('Muito caro')






