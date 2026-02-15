# Data Science Academy
# Mini-Projeto 2 - Aplicação Full-Stack de Sistema Bancário em Python com Programação Orientada a Objetos
# Módulo Principal da Aplicação

# Importa a classe Banco responsável por gerenciar clientes e contas
from operations.bank import Bank

# Importa exceções personalizadas usadas no fluxo de operações
from utils.exceptions import InsufficientBalanceError, AccountNotFoundError


# Função que exibe o menu principal da aplicação
def main_menu():

    print("\n--- DSA Mini-Projeto 2 - Sistema Bancário Digital ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")

    # Retorna a opção digitada pelo usuário
    return input("Escolha uma opção: ")


# Função que exibe o menu de operações de uma conta específica
def account_menu(bank):

    try:

        # Solicita ao usuário o número da conta
        account_number = int(input("Digite o número da conta: "))

        # Busca a conta no banco; pode gerar exceção se não existir
        account = bank.find_account(account_number)

        # Loop de operações dentro da conta
        while True:

            print(f"\n--- Operações para Conta Nº {account._account_number} ---")
            print(f"Cliente: {account._client.name} | Saldo: R${account.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")

            # Lê a opção do usuário
            option = input("Escolha uma opção: ")

            if option == "1":

                # Deposita valor na conta
                amount = float(input("Digite o valor para depósito: "))
                account.add_funds(amount)

            elif option == "2":

                # Tenta realizar um saque
                try:

                    amount = float(input("Digite o valor para saque: "))
                    account.withdraw(amount)  # Polimorfismo: depende do tipo de conta

                except InsufficientBalanceError as e:
                    print(f"Erro na operação: {e}")

            elif option == "3":

                # Exibe o extrato da conta
                account.display_account_summary()

            elif option == "4":

                # Sai do menu da conta e retorna ao menu principal
                break

            else:
                print("Opção inválida. Tente novamente.")

    # Exceção caso a conta não exista
    except AccountNotFoundError as e:
        print(f"Erro: {e}")

    # Exceção para entradas inválidas (não numéricas)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")


# Função principal que controla o fluxo do sistema
def main():

    # Cria o objeto Banco
    bank = Bank("Banco Digital DSA")

    # Loop principal do sistema
    while True:

        option = main_menu()

        if option == "1":

            # Adiciona um novo cliente
            name = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            bank.add_client(name, cpf)

        elif option == "2":

            # Cria uma nova conta vinculada a um cliente existente
            cpf = input("Digite o CPF do cliente para vincular a conta: ")
            client = bank._clients.get(cpf)

            if client:

                account_type = input("Digite o tipo da conta (corrente/poupanca): ")
                bank.create_account(client, account_type)

            else:
                print("Cliente não encontrado. Cadastre o cliente primeiro.")

        elif option == "3":

            # Abre o menu de operações de uma conta
            account_menu(bank)

        elif option == "4":

            # Encerra o programa
            print("\nObrigado por usar o nosso sistema. Até logo!\n")
            break

        else:

            print("\nOpção inválida. Por favor, tente novamente.\n")


# Ponto de entrada da aplicação
if __name__ == "__main__":
    main()
