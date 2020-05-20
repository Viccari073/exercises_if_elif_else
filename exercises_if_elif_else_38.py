"""
Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual
e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente
maior do que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário
irá receber um bônus adicional de salário. Faça um programa que leia:

- O valor do salário atual do funcionário;
- O tempo de serviço desse funcionário na empresa (número de anos de trabalho).

Use a tabela abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado,
ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

Salário Atual               Reajuste           Tempo de serviço            Bônus
Até 500,00                     25%              Abaixo de 1 ano              0
Até 1000,00                    20%              De 1 a 3 anos              100,00
Até 1500,00                    15%              De 4 a 6 anos              200,00
Até 2000,00                    10%              De 7 a 10 anos             300,00
Acima de 2000,00                0               Mais de 10 anos            500,00
"""

salario = float(input('Digite seu salário: R$ '))
temp_serv = int(input('Quantos anos de tempo de serviço: '))
bonus = float()

if temp_serv < 1:
    bonus = 0
    print(f'Com menos de 1 ano de serviço, você não tem direito a bônus.')
elif 1 <= temp_serv <= 3:
    bonus = 100.00
    print(f'Seu bônus será de {bonus}')
elif 4 <= temp_serv <= 6:
    bonus = 200.00
    print(f'Seu bônus será de {bonus}')
elif 7 <= temp_serv <= 10:
    bonus = 300.00
    print(f'Seu bônus será de {bonus}')
else:
    bonus = 500.00
    print(f'Seu bônus será de {bonus}')

if salario <= 500:
    salario = salario + (salario * (25/100))
    print(f'Seu salário com 25% de reajuste será de R${salario: .2f}')
elif 500 < salario <= 1000.00:
    salario = salario + (salario * (20/100))
    print(f'Seu salário com 20% de reajuste será de R${salario: .2f}')
elif 1000.00 < salario <= 1500.00:
    salario = salario + (salario * (15/100))
    print(f'Seu salário com 15% de reajuste será de R${salario: .2f}')
elif 1500.00 < salario <= 2000.00:
    salario = salario + (salario * (10/100))
    print(f'Seu salário com 10% de reajuste será de R${salario: .2f}')
else:
    print('Você não tem direito a reajuste.')

