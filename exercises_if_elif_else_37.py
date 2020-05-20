"""
Leia uma data de anscimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano. 
Teste a validade desta data para saber se esta data é uma data válida.
Teste de o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês de fevereio (29 se o ano for bissexto),
dia <= 30 em abril, junho, setembro e novembro, dia <= 31 nos outros meses.
Teste a validade do mês: mês > 0 e mês < 13. Teste a validade do ano: ano <= ano atual (use uma constante definida com
o valor igual a 2020). Imprimir: 'Data válida' ou 'Data inválida' no final da execução do programa.
"""

data_nasc = input('Qual a data do seu nascimento DD/MM/YYYY: ')

dia, mes, ano = (int(dado) for dado in data_nasc.split('/'))

if ano > 2020:
    print('Data não existe')
else:
    if 1 <= mes <= 12:
        if mes == 2:
            if ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0:
                if 0 <= dia <= 29:
                    print('Data existe')
                else:
                    print('Data não existe')
            elif 0 <= dia <= 28:
                print('Data existe')
            else:
                print('Data não existe')
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if 0 <= dia <= 30:
                print('Data existe')
            else:
                print('Data não existe')
        elif 0 <= dia <= 31:
            print('Data existe')
    else:
        print('Data não existe')


