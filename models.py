from enum import Enum, unique


@unique
class AccountType(Enum):
    CURRENT = 0
    DEPOSIT = 1


class Account:
    def __init__(self, account_type: AccountType):
        self.balance = 0
        self.account_type = account_type
        if account_type == AccountType.CURRENT:
            self.credit_allowed = True
        else:
            self.credit_allowed = False

    def withdraw_money(self, summa):
        if self.balance >= summa or self.credit_allowed:
            self.balance -= summa

    def change_credit_status(self, new_status: bool):
        self.credit_allowed = new_status

    def deposit_money(self, amount: int | float):
        self.balance += amount


class Client:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.accounts: list[Account] = []

    def open_new_account(self, account_type: AccountType):
        self.accounts.append(Account(account_type))


# new_client = Client('John', 'Kyiv')
# new_client.open_new_account(AccountType.CURRENT)
# new_client.open_new_account(AccountType.DEPOSIT)
# new_client.accounts[0].deposit_money(5000)
# new_client.accounts[0].withdraw_money(15000)
#
# pass