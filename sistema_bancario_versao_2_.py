
def menu():
    menu = """\n
    ========== Menu ==========
    [ 1 ] Depositar
    [ 2 ] Sacar
    [ 3 ] Extrato
    [ 4 ] Nova Conta
    [ 5 ] Novo usuario
    [ 6 ] Listar Contas
    [ 0 ] Sair
    ==> """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n *** Deposito realizado com sucesso! ***")
    else:
        print("\n *** Operacao falhou. O valor informado é invalido. Tente novamente. ***")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, Limite_Saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = valor >= Limite_Saques

    if excedeu_saldo:
        print("\n *** Operacao falhou por saldo insuficiente. ***")

    elif excedeu_limite:
        print("\n *** Operaçao falhou, O valor do saque excedeu o limite. ***")

    elif excedeu_saques:
        print("\n *** Operaçao falhou. Atingiu o numero de saques diarios. ***")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n *** Saque realizado com sucesso! ***")

    else:
        print("\n *** Operaçao falhou. O valor informado é invalido. Por favor tente mais tarde. ***")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("n ========== Extrato ========== ")
    print("Nao foram realizadas movimentaçoes." if not extrato else extrato)
    print(f"\n Saldo: \t\t R$ {saldo:.2f}")
    print("====================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n *** Ja existe usuario com esse CPF! ***")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereço = input("Informe o seu endereço (rua, numero, cidade, estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("*** Usuario criado com sucesso! ***")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n *** Conta criada com sucesso! ***")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n *** Usuario nao encontrado, fluxo de criaçao de conta ecerrado! ***")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agencia:\t{conta['agencia']}
        C\C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """

        print("=" * 100)
        print(linha)

def main():
    Limite_Saques = 3
    Agencia = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe a quantia que deseja sacar: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                Limite_Saques = Limite_Saques,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(Agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break
    else:
        print("*** Operçao invalida, por favor selecione novamente a operçao desejada. ***")

main ()