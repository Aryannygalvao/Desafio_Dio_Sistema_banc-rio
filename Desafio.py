menu = """
[d] depositar 
[s] sacar
[e] extrato
[q] sair
=> """

numero_saque= 0
limite_saque = 3
saldo = 0
limite = 500
extrato = ""

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Informe o valor do saque:"))
        saldo += deposito
        extrato += f"Depósito de R${deposito:.2f}\n"
        print(f"Saldo atual: R${saldo:.2f}")
    elif opcao == "s":
        print("Saque")
        saque = float(input("Informe o valor do saque:"))
        if saldo >= saque and numero_saque < limite_saque: 
           saldo -= saque 
           extrato += f"Saque de R${saque:.2f}\n"
           numero_saque += 1
           print(f"Saque de R${saque:.2f} realizado. Saldo atual: R${saldo:.2f}")
        elif numero_saque >= limite_saque: 
            print(f"O limite de saques ({limite_saque}) foi atingido hoje.")
        else: 
            print("Saldo insuficiente.")
    elif opcao =="e":
        print("Extrato")
        extrato += f"Saldo atual:R${saldo:.2f}"
        print(extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
