print('Estátistica de Acidente de Trabalho')
#LEGENDA: NA - Número de Acidentes:
#LEGENDA: HT - Horas Trabalhadas:
#LEGENDA: DP - Dias Perdidos:
#LEGENDA: TF - Taxa de Frequência (TF):
#LEGENDA: TG - Taxa de Gravidade (TG):   

mes=input('Digite os mês de  referência; ')
na=float(input('Digite a quantidade de acidentes:  '))
dp=float(input('Digite a quantidade de dias perdidos: '))
ht=float(input('Digite a quantidade de horas trabalhadas: '))
tf=(na*1.000000)/ht
tg=(dp*1.000000)/ht
print('A taxa de Gravidade de Acidente do més {} é {:.2f} '.format(mes, tg))
print('A taxa de Frequência de Acidentes de trabalho do mês é: {:.2f} '.format(tf,))