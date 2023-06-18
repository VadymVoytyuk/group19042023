from models import AccountType

from models import AccountType


def test_current_account(new_current_account):
    print(new_current_account.__dict__)
    assert new_current_account.account_type == AccountType.CURRENT


def test_current_account_withdraw(new_current_account):
    print(new_current_account.__dict__)
    new_current_account.deposit_money(4500.0)
    new_current_account.withdraw_money(summa=100)
    assert new_current_account.balance == 4400


def test_current_account_change_credit_status(new_current_account):
    print(new_current_account.__dict__)
    new_current_account.change_credit_status(True)
    assert new_current_account.credit_allowed is True


def test_current_account_deposit_money(new_current_account):
    print(new_current_account.__dict__)
    new_current_account.deposit_money(100.0)
    assert new_current_account.balance == 100.0
