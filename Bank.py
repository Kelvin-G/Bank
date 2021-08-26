saldo = 3159.10

saque = float(input('Quanto deseja sacar? R$'))

if saque <= saldo:
    print(f'saque efetuado com sucesso! seu saldo atual é de R${saldo - saque :.2f}')
    saldo = saldo - saque
else:
    print(f'Ops! parece que seu saldo é isuficiente. Você tem disponivel na conta R${saldo :.2f} tente novamente.')
