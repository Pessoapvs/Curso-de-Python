print('Salario')
sl=float(input('Qual é o salario do funcionario?:R$ '))
novo=sl+(sl*15/100)

print('Um funcionario que ganhava R$ {:.2f} com 15% de aumento passa a ganhar R$ {:.2f}'.format(sl, novo))