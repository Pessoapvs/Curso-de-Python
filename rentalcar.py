km=float(input('Digite o km: '))
diaria=int(input('Digite quantos dias de locação: '))
valor=(km*0.15)+(diaria*60)
print('De acordo com a km rodada de {} durante {} dias o valor tottal da fatura é R$ {:.2f}'. format(km, diaria, valor))