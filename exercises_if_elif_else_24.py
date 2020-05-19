"""
Leia  a distancia em km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:

CONSUMO     Km/l       Mensaggem
menor que     8        Venda o carro!
entre        8 e 12    Econômico!
maior que     12       Super econômico!

"""

distancia = float(input('Digite a distancia percorrida, em km: \n'))
litros = float(input('Digite quantos litros foram gastos: \n'))


media = distancia / litros

if media < 8:
    print(f'A média foi de {media: .2f}, venda o carro!')
elif 8 <= media <= 12:
    print(f'A méida foi de {media: .2f}, o carro é econômico!')
else:
    print(f'A média foi de {media: .2f}, o carro é super econômico!')
