menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

dinheiro = 0
limite = 1000
extrato = ""
numeroSaques = 0
limiteSaques = 5

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        print(f"Deposito de R${valor: .2f} realizado com sucesso!")

        if valor > 0:
            dinheiro += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        print(f"Saque de R${valor: .2f} realizado com sucesso!")

        excedeuSaldo = valor > dinheiro

        excedeuLimite = valor > limite

        excedeu_saques = numeroSaques >= limiteSaques

        if excedeuSaldo:
            print("Operação falhou! Você não tem saldo suficiente.\n")
            print(f"Saldo atual é de: R${dinheiro: .2f}")

        elif excedeuLimite:
            print(
                f"Operação falhou! O valor do saque excede o limite permitido R${limite}.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            dinheiro -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numeroSaques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n********** EXTRATO ************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {dinheiro: .2f}")
        print("*******************************")

    elif opcao == "0":
        print("Saindo do app...\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
