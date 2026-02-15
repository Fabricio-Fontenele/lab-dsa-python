# Data Science Academy
# Mini-Projeto 2 - Aplicação Full-Stack de Sistema Bancário em Python com Programação Orientada a Objetos
# Módulo para exceções customizadas da aplicação.


# Define a exceção para saldo insuficiente em operações de saque
class InsufficientBalanceError(Exception):
    """Exceção levantada quando uma operação de saque excede o saldo disponível."""

    # Construtor da exceção
    def __init__(
        self,
        current_balance,
        withdrawal_amount,
        message="Saldo insuficiente para realizar o saque.",
    ):

        # Saldo atual da conta no momento do erro
        self.current_balance = current_balance

        # Valor solicitado para saque
        self.withdrawal_amount = withdrawal_amount

        # Mensagem detalhada de erro com saldo atual e valor do saque
        self.message = f"{message} Saldo atual: R${current_balance:.2f}, Tentativa de saque: R${withdrawal_amount:.2f}"

        # Chama o construtor da classe Exception com a mensagem
        super().__init__(self.message)


# Define a exceção para operações em contas inexistentes
class AccountNotFoundError(Exception):
    """Exceção levantada ao tentar operar em uma conta que não existe."""

    # Construtor da exceção
    def __init__(
        self, account_number, message="A conta especificada não foi encontrada."
    ):

        # Número da conta que não foi encontrada
        self.account_number = account_number

        # Mensagem detalhada de erro com o número da conta
        self.message = f"{message} Número da conta: {account_number}"

        # Chama o construtor da classe Exception com a mensagem
        super().__init__(self.message)
