menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Insira um valor válido > 0")

def sacar():
    global saldo, extrato, numero_saques
    valor = float(input("Informe o valor do saque: "))
    if valor > 0:
        if saldo >= valor:
            if valor <= limite:
                if numero_saques < LIMITE_SAQUES:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
                else:
                    print("Número máximo de saques atingido.")
            else:
                print("Limite excedente.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Valor informado inválido")

def exibir_extrato():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)
    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        exibir_extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
