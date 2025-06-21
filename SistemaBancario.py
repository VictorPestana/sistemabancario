saldo = 0
movimentos = []
saques_do_dia = 0

def mostrar_menu():
    print("""
Escolha uma opção:

1 - Depósito
2 - Saque
3 - Transferência
4 - Extrato
0 - Sair
""")

while True:
    mostrar_menu()
    escolha = input("Opção: ")

    if escolha == "1":
        valor = float(input("Quanto deseja depositar? R$ "))
        if valor > 0:
            saldo += valor
            movimentos.append(f"Depósito de R$ {valor:.2f}")
        else:
            print("Valor inválido!")

    elif escolha == "2":
        if saques_do_dia >= 3:
            print("Limite de saques diários atingido.")
            continue

        valor = float(input("Quanto deseja sacar? R$ "))
        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > 500:
            print("Limite máximo por saque é R$ 500.")
        elif valor > 0:
            saldo -= valor
            movimentos.append(f"Saque de R$ {valor:.2f}")
            saques_do_dia += 1
        else:
            print("Valor inválido!")

    elif escolha == "3":
        valor = float(input("Valor da transferência: R$ "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            movimentos.append(f"Transferência de R$ {valor:.2f}")
        else:
            print("Transferência não realizada. Verifique o saldo e o valor.")

    elif escolha == "4":
        print("\n==== EXTRATO ====")
        if not movimentos:
            print("Nenhuma movimentação.")
        else:
            for m in movimentos:
                print(m)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=================\n")

    elif escolha == "0":
        print("Sessão encerrada. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
