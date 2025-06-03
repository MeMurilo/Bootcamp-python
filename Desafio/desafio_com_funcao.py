def menu():
    print("""
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
""")
    return input("=> ")

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido!")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        print("Valor inválido!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print("O valor do saque excede o limite!")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques excedido!")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n=========== EXTRATO ===========")
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("===============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe usuário com esse CPF!")
            return
    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")
    usuarios.append({"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")

def criar_conta(contas, usuarios, agencia):
    cpf = input("Informe o CPF do usuário: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            numero_conta = len(contas) + 1
            contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
            print("Conta criada com sucesso!")
            return
    print("Usuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        print("===============================")
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print("===============================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            criar_conta(contas, usuarios, AGENCIA)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Obrigado por acessar nosso banco!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
