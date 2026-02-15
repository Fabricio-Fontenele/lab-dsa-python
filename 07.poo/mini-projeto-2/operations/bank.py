# Data Science Academy
# Mini-Projeto 2 - Aplicação Full-Stack de Sistema Bancário em Python com Programação Orientada a Objetos
# Módulo que define a classe principal do Banco, que gerencia clientes e contas.

# Importa a classe Cliente
from entities.cliente import Client

# Importa a classe base Conta e suas subclasses (Corrente e Poupança)
from entities.account import BankAccount, ContaCorrente, ContaPoupanca

# Importa exceção personalizada para conta inexistente
from utils.exceptions import AccountNotFoundError


# Define a classe Banco
class Bank:
    """
    Classe que gerencia as operações do banco.
    Demonstra Composição, pois "tem" clientes e contas.
    """

    # Construtor da classe Banco
    def __init__(self, name: str):

        # Nome do banco
        self.name = name

        # Dicionário de clientes (chave: CPF, valor: objeto Cliente)
        self._clients = {}

        # Dicionário de contas (chave: número da conta, valor: objeto Conta)
        self._accounts = {}

    # Método para adicionar um novo cliente ao banco
    def add_client(self, name: str, cpf: str) -> Client:
        """Cria e adiciona um novo cliente ao banco."""

        # Verifica se já existe cliente com o mesmo CPF
        if cpf in self._clients:
            print("Erro: Cliente com este CPF já cadastrado.")
            return self._clients[cpf]

        # Cria objeto Cliente e adiciona ao dicionário
        new_client = Client(name, cpf)
        self._clients[cpf] = new_client

        print(f"Cliente {name} adicionado com sucesso!")

        return new_client

    # Método para criar uma conta para um cliente
    def create_account(self, client: Client, account_type: str) -> BankAccount:
        """Cria uma nova conta para um cliente existente."""

        # Número da nova conta será baseado no total de contas + 1
        account_number = BankAccount.get_total_accounts() + 1

        # Cria conta corrente se o tipo informado for "corrente"
        if account_type.lower() == "corrente":
            new_account = ContaCorrente(account_number, client)

        # Cria conta poupança se o tipo informado for "poupanca"
        elif account_type.lower() == "poupanca":
            new_account = ContaPoupanca(account_number, client)

        # Caso o tipo não seja válido
        else:
            print("Tipo de conta inválido. Escolha 'corrente' ou 'poupanca'.")
            return None

        # Adiciona a conta ao dicionário de contas
        self._accounts[account_number] = new_account

        # Associa a conta ao cliente
        client.add_account(new_account)
        print(
            f"Conta {account_type} nº {account_number} criada para o cliente {client.name}."
        )

        return new_account

    # Método para buscar uma conta pelo número
    def find_account(self, account_number: int) -> BankAccount:
        """Busca uma conta pelo seu número."""

        # Tenta recuperar a conta do dicionário
        account = self._accounts.get(account_number)

        # Se não encontrar, lança exceção personalizada
        if not account:
            raise AccountNotFoundError(account_number)
        return account
