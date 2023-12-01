from hexagonal.app.core.domain.address import Address
from hexagonal.app.core.domain.customer import Customer


def test_customer_creation():
    address = Address("123 Main St", "Cityville", "CA")
    customer = Customer("1", "John Doe", address, "12345678901")

    assert customer.id == "1"
    assert customer.name == "John Doe"
    assert customer.address == address
    assert customer.cpf == "12345678901"
    assert not customer.is_valid_cpf


def test_customer_update():
    address = Address("123 Main St", "Cityville", "CA")
    customer = Customer("1", "John Doe", address, "12345678901")

    # Test updating id
    customer.id = "2"
    assert customer.id == "2"

    # Test updating name
    customer.name = "Jane Doe"
    assert customer.name == "Jane Doe"

    # Test updating address
    new_address = Address("456 Oak St", "Townsville", "NY")
    customer.address = new_address
    assert customer.address == new_address

    # Test updating cpf
    customer.cpf = "98765432109"
    assert customer.cpf == "98765432109"

    # Test updating is_valid_cpf
    customer.is_valid_cpf = True
    assert customer.is_valid_cpf
