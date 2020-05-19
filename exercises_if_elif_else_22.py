"""
Uma empresa vende o mesmo produto para 4 diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o
produto (MG 7%; SP 12%; RJ 15% e MS 8%).
Faça um programa em que o usuário entre com o valor do produto e o estado destino do produto e o programa retorne
o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado não for válido, mostrar uma
mensagem de erro.
"""

valor_produto = float(input('Digite o valor do produto: '))
print('Escolha o estado de destino:')
print('1 - MG')
print('2 - SP')
print('3 - RJ')
print('3 - MS')
estado = int(input("Digite o número do estado: "))

if estado == 1:
    print(f'Para o estado de MG o valor do produto fica {(valor_produto + (valor_produto * (7/100))): .2f}')
elif estado == 2:
    print(f'Para o estado de SP o valor do produto fica {(valor_produto + (valor_produto * (12/100))): .2f}')
elif estado == 3:
    print(f'Para o estado de RJ o valor do produto fica {(valor_produto + (valor_produto * (15/100))): .2f}')
elif estado == 4:
    print(f'Para o estado de MS o valor do produto fica {(valor_produto + (valor_produto * (8/100))): .2f}')
else:
    print('Opção inválida.')

