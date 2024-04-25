menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuario
[c] Criar conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios =[]
contas = []
seq_contas = 1

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Insira um valor válido > 0")
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
        
    if valor > 0:
        if saldo >= valor:
            if valor <= limite:
                if numero_saques < limite_saques:
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
    
    return saldo, extrato

def criar_usuarios(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Já existe usupario com o CPF informado")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaa): ")
    endereco = input("Informe o endereço no formato (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário inserido com sucesso.")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso.")
        return({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    
    print("Usuario não encontrado.")
    
      
def exibir_extrato(saldo, /, *, extrato=extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    

while True:
    opcao = input(menu)
    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "s":
        sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == "u":
        criar_usuarios(usuarios)
    elif opcao == "c":
        conta = criar_conta(AGENCIA, seq_contas, usuarios)
        
        if conta:
            contas.append(conta)
            seq_contas += 1
            
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
