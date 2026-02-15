class Client:
    def __init__(self, name: str, cpf: str):
        self.accounts = []

        self.name = name
        self.cpf = cpf

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        return f"Cliente: {self.name} (CPF: {self.cpf})"
