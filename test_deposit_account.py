from models import AccountType


def test_deposit_account(new_deposit_account):
    print(new_deposit_account.__dict__)
    assert new_deposit_account.account_type == AccountType.DEPOSIT


def test_deposit_account_withdraw(new_deposit_account):
    print(new_deposit_account.__dict__)
    new_deposit_account.deposit_money(5000.0)
    new_deposit_account.withdraw_money(summa=100)
    assert new_deposit_account.balance == 4900


def test_deposit_account_change_credit_status(new_deposit_account):
    print(new_deposit_account.__dict__)
    new_deposit_account.change_credit_status(True)
    assert new_deposit_account.credit_allowed is True


def test_deposit_account_deposit_money(new_deposit_account):
    print(new_deposit_account.__dict__)
    new_deposit_account.deposit_money(100.0)
    assert new_deposit_account.balance == 100.0
