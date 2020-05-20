"""
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12 e se o dia existe naquele mês.
Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
"""

data = input('Informe uma data dd/mm/aaaa: ')
data = data.split('/')

for i in range(3):
    data[i] = int(data[i])
#  data[0] = dia, data[1] = mês, data[2] = ano
if 1 <= data[1] <= 12:
    if data[1] == 2:
        if data[2] % 400 == 0 or data[2] % 4 == 0 and data[2] % 100 != 0:
            if 0 <= data[0] <= 29:
                print('Data existente.')
            else:
                print('Data não existe.')
        elif 0 <= data[0] <= 28:
            print('Data existente.')
        else:
            print('Data não existe.')
    elif data[1] == 4 or data[1] == 6 or data[1] == 9 or data[1] == 11:
        if 0 <= data[0] <= 30:
            print('Data existente.')
        else:
            print('Data não existe')
    else:
        if 0 <= data[0] <= 31:
            print('Data existente.')
        else:
            print('Data não existe.')
else:
    print('Data não existe')



