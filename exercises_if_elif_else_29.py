"""
Escrever um porgrama que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido.
O cardápio da lanchonete segue o padrão abaixo:

Especificação            Código      Preço

Cachorro quente           100         1.20
Bauru simples             101         1.30
Bauru com Ovo             102         1.50
Hambuguer                 103         1.20
Cheeseburguer             104         1.70
Suco                      105         2.20
Refrigerante              106         1.00

"""

print('Cardápio: \n')
print('100 - Cachorro quente')
print('101 - Bauru simples')
print('102 - Bauru com Ovo')
print('103 - Hambuguer')
print('104 - Cheeseburguer')
print('105 - Suco')
print('106 - Refrigerante\n')

escolha = int(input('Digite o código da sua escolha: '))

if escolha == 100:
    print('Você escolheu o cachorro-quente!')
    print('Qual a quantidade que você deseja? ')
    qtd = int(input())
    total = float(qtd * 1.20)
    print(f'O valor a pagar é de R${total: .2f}')
elif escolha == 101:
    print('Você escolheu o bauru simples!')
    print('Qual a quantidade que você deseja? ')
    qtd = int(input())
    total = float(qtd * 1.30)
    print(f'O valor a pagar é de R${total: .2f}')
elif escolha == 102:
    print('Você escolheu o Bauru com Ovo!')
    print('Qual a quantidade que você deseja? ')
    qtd = int(input())
    total = float(qtd * 1.30)
    print(f'O valor a pagar é de R${total: .2f}')
elif escolha == 103:
    print('Você escolheu o Hambuguer!')
    print('Qual a quantidade que você deseja? ')
    qtd = int(input())
    total = float(qtd * 1.20)
    print(f'O valor a pagar é de R${total: .2f}')
elif escolha == 104:
    print('Você escolheu o Cheeseburguerr!')
    print('Qual a quantidade que você deseja? ')
    qtd = int(input())
    total = float(qtd * 1.70)
    print(f'O valor a pagar é de R${total: .2f}')
elif escolha == 105:
    print('Você escolheu o Suco!')
    print('Qual a quantidade que você deseja? ')
    qtd = int(input())
    total = float(qtd * 2.20)
    print(f'O valor a pagar é de R${total: .2f}')
elif escolha == 106:
    print('Você escolheu o Refrigerante!')
    print('Qual a quantidade que você deseja? ')
    qtd = int(input())
    total = float(qtd * 1.00)
    print(f'O valor a pagar é de R${total: .2f}')
else:
    print('Escolheu o código errado!')



