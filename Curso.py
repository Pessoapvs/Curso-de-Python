print('Desafio - 01')
nome=input('Qual é o seu nome? ')
print(nome,',Bem vindo! ao curso de python')

print('Desafio - 02')
dia=input('Qual é o dia do seu nascimento?: ')
mes=input('Qual é o més do seu nascimento?: ')
ano=input('Qual é o ano do seu nascimento?: ')
print('Vocẽ nasceu no dia',dia,'de',mes,'do ano de',ano,'correto?')

print('Desafio - 03')
numero1=int(input('Primeiro numero; '))
numero2=int(input('Segundo numero: '))
Soma=numero1+numero2
#print('A soma é',Soma)
print('A soma entre {} e {} e igual a {}'.format(numero1, numero2, Soma))

print('Desafio - 04')
a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')

print('Desafio - 05')
n1=int(input('Um Valor; '))
n2=int(input('Outro Valor; '))
s=n1+n2
m=n1*n2
d=n1/n2
d1=n1//n2
e=n1**n2
print ('A soma é {} o produto é {} a divisãao é {}' .format (s, m, d,))
print ('A divisão inteira é {} a potẽncia é {}'.format(d1, e))

print ('Desafio - 06')
n1=int(input('Digite um numero: '))
d=n1*2
t=n1*3
rz2=n1*n1
print ('O Dobro é {} o triplo é {} e a raiz quadrada é {}'.format(d, t, rz2))

print ('Desafio - 07')
nt1=int(input('Digite a nota 01: '))
nt2=int(input('Digite a nota 02: '))
m=(nt1+nt2)//2
print ('A media do aluno é {}'.format(m,))

print ('Desafio - 08')
n1=float(input('Digite um numero para convertemos: '))
cm = n1 * 100
mm = n1 * 1000
print ('conversão em centimetros é {} e conversão para milimetos e {}'.format(cm, mm))

print('Desafio - 09')

n = int(input('Digite um número inteiro: '))

print(f'Tabuada do {n}:')
print('-' * 20)

for i in range(1, 11):
    resultado = n * i
    print(f'{n} x {i} = {resultado}')

print('-' * 20)

print ('Desafio - 10')
n1=int(input('Digite um numero: '))
at=n1-1
ss=n1+1
print('O numero antercessor ao digitado é {} e o sucessor e {}.' .format(at, ss))

print ('Desafio - 11')
ct=int(input('Quanto de dinheito tem na carteira: '))
Dolar=ct*5,30
print ('Com o saldo da carteria vc consegue comprar {} dolar.'.format(Dolar,))

