
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("A operação falhou! Valor informado é inválido.")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques  = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A operação falhou! Você não tem saldo sufuciente.")

        elif excedeu_limite:
            print("\nA operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("A operação falhou! Número Máximo de saques excedido.")  

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}s\n"
            numero_saques += 1
        
        else:
            print("A operação falhou! Valor informado é inválido.")

    elif opcao == "e":

        print("\n################### Extrato ###################")
        print("\nNão foi realizado movimentações." if not extrato else extrato)   
        print("###############################################")
        print(f"Saldo: R$ {saldo:.2f}")
        print("###############################################")

    elif opcao == "q":
        break

    else:
        print("Opção invalida! Por favor informe a opção desejada.")