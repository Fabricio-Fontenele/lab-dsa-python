# Data Science Academy
# Mini-Projeto 2 - Aplicação Full-Stack de Sistema Bancário em Python com Programação Orientada a Objetos
# Módulo que define as classes de Conta (Abstrata, Corrente e Poupança).

# Importa a classe base abstrata e o decorador para métodos abstratos
from abc import ABC, abstractmethod

# Importa a classe datetime para registrar data e hora das transações
from datetime import datetime

# Importa exceção personalizada para saldo insuficiente
from utils.exceptions import SaldoInsuficienteError


# Define a classe abstrata Conta, que serve como base para outros tipos de contas
class BankAccount(ABC):
    """
    Classe base abstrata para contas bancárias.
    Demonstra Herança e Encapsulamento.
    """

    # Atributo de classe que calcula quantas contas foram criadas
    _total_accounts_created = 0

    # Construtor da classe
    def __init__(self, account_number: int, client):

        # Número da conta (atributo protegido)
        self._account_number = account_number

        # Saldo da conta, inicializado em 0.0 (atributo protegido)
        self._balance = 0.0

        # Referência ao cliente dono da conta
        self._client = client

        # Lista para armazenar histórico de transações
        self._transaction_history = []

        # Incrementa o total de contas criadas
        BankAccount._total_accounts_created += 1

    # Propriedade para acessar o saldo de forma controlada
    @property
    def saldo(self):
        """Getter para o saldo, permitindo acesso controlado."""
        return self._balance

    # Método de classe para consultar o número total de contas
    @classmethod
    def get_total_accounts(cls):
        """Método de classe para obter o número total de contas criadas."""

        return cls._total_accounts_created

    # Método para realizar depósitos
    def add_funds(self, amount: float):

        # Adiciona um valor ao saldo da conta.
        if amount > 0:

            # Incrementa o saldo
            self._balance += amount

            # Registra a transação no histórico com data e hora
            self._transaction_history.append(
                (datetime.now(), f"Depósito de R${amount:.2f}")
            )
            print(f"Depósito de R${amount:.2f} realizado com sucesso.")

        else:

            print("Valor de depósito inválido.")

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def withdraw(self, amount: float):
        """Método abstrato para sacar um valor. Deve ser implementado pelas subclasses."""

        pass

    # Método para exibir o extrato da conta
    def display_account_summary(self):
        """Exibe o extrato da conta."""
        print(f"\n--- Extrato da Conta Nº {self._account_number} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._balance:.2f}")
        print("Histórico de transações:")

        # Caso não haja transações registradas
        if not self._transaction_history:
            print("Nenhuma transação registrada.")

        # Percorre o histórico e exibe cada transação
        for transaction_date, transaction in self._transaction_history:
            print(f"- {transaction_date.strftime('%d/%m/%Y %H:%M:%S')}: {transaction}")
        print("--------------------------------------\n")


# Define a subclasse ContaCorrente
class ContaCorrente(BankAccount):
    """
    Subclasse que representa uma conta corrente.
    Demonstra Polimorfismo ao sobrescrever o método sacar.
    """

    # Construtor com limite padrão de cheque especial
    def __init__(self, account_number: int, client, credit_limit: float = 500.0):

        # Chama o construtor da classe base
        super().__init__(account_number, client)

        # Define o limite de cheque especial
        self.credit_limit = credit_limit

    # Implementação do método sacar com cheque especial
    def withdraw(self, amount: float):
        """Permite saque utilizando o saldo da conta mais o limite (cheque especial)."""

        if amount <= 0:
            print("Valor de saque inválido.")
            return

        # Calcula o saldo disponível (saldo + limite)
        available_balance = self._account_balance + self.credit_limit

        # Caso o valor do saque ultrapasse o saldo disponível
        if amount > available_balance:
            raise SaldoInsuficienteError(
                available_balance, amount, "Saldo e limite insuficientes."
            )

        # Deduz o valor do saque do saldo
        self._account_balance -= amount

        # Registra a transação no histórico
        self._transaction_history.append((datetime.now(), f"Saque de R${amount:.2f}"))
        print(f"Saque de R${amount:.2f} realizado com sucesso.")


# Define a subclasse ContaPoupanca
class ContaPoupanca(BankAccount):
    """Subclasse que representa uma conta poupança."""

    # Construtor da poupança, herda do construtor base
    def __init__(self, account_number: int, client):
        super().__init__(account_number, client)

    # Implementação do método sacar apenas com saldo disponível
    def withdraw(self, amount: float):

        # Permite saque apenas se houver saldo suficiente na conta.
        if amount <= 0:
            print("Valor de saque inválido.")
            return

        # Verifica se há saldo suficiente
        if amount > self._account_balance:
            raise SaldoInsuficienteError(self._account_balance, amount)

        # Deduz o valor do saldo
        self._account_balance -= amount

        # Registra a transação no histórico
        self._transaction_history.append((datetime.now(), f"Saque de R${amount:.2f}"))
        print(f"Saque de R${amount:.2f} realizado com sucesso.")
