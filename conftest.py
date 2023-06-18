import pytest
from faker import Faker

from models import Account, Client, AccountType

fake_gen = Faker(locale='uk_UA')


@pytest.fixture(scope='session')  # default = function, class, module, session
def new_client():
    client = Client(
        name=fake_gen.name(),
        address=fake_gen.address()
    )
    yield client
    del client


@pytest.fixture
def new_deposit_account():
    account = Account(AccountType.DEPOSIT)
    yield account
    del account


@pytest.fixture
def new_current_account():
    account = Account(AccountType.CURRENT)
    yield account
    del account
