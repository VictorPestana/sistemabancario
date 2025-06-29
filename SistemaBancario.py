from POO_SistemaBancario import Cliente, ContaCorrente, Deposito, Saque

AGENCIA = "0001"
clientes = []
contas = []

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar cliente
[c] Criar conta
[l] Listar contas
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "u":
        cpf = input("CPF (somente números): ").strip()
        cliente_existente = next((c for c in clientes if c.cpf == cpf), None)

        if cliente_existente:
            print("Já existe um cliente com esse CPF!")
            continue

        nome = input("Nome completo: ").strip()
        nascimento = input("Data de nascimento (dd-mm-aaaa): ").strip()
        endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ").strip()

        # Corrigido: ordem correta dos parâmetros
        cliente = Cliente(nome, cpf, nascimento, endereco)
        clientes.append(cliente)
        print("Cliente criado com sucesso!")

    elif opcao == "c":
        cpf = input("Informe o CPF do cliente: ").strip()
        cliente = next((c for c in clientes if c.cpf == cpf), None)

        if cliente:
            numero_conta = len(contas) + 1
            # Corrigido: ordem correta dos parâmetros
            conta = ContaCorrente(numero_conta, cliente, AGENCIA)
            contas.append(conta)
            print("Conta criada com sucesso!")
        else:
            print("Cliente não encontrado. Por favor, crie o cliente primeiro.")

    elif opcao in ["d", "s", "e"]:
        cpf = input("Informe o CPF do titular da conta: ").strip()
        cliente = next((c for c in clientes if c.cpf == cpf), None)

        if not cliente or not cliente.contas:
            print("Cliente não encontrado ou sem contas cadastradas.")
            continue

        conta = cliente.contas[0]  # Assume a primeira conta do cliente

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            cliente.realizar_transacao(conta, Deposito(valor))

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            cliente.realizar_transacao(conta, Saque(valor))

        elif opcao == "e":
            conta.exibir_extrato()

    elif opcao == "l":
        for conta in contas:
            print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Titular: {conta.cliente.nome}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
