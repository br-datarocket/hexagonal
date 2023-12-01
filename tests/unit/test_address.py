from hexagonal.app.core.domain.address import Address


def test_address_creation():
    address = Address("123 Main St", "Cityville", "CA")
    assert address.street == "123 Main St"
    assert address.city == "Cityville"
    assert address.state == "CA"


def test_address_update():
    address = Address("123 Main St", "Cityville", "CA")

    # Test updating street
    address.street = "456 Oak St"
    assert address.street == "456 Oak St"

    # Test updating city
    address.city = "Townsville"
    assert address.city == "Townsville"

    # Test updating state
    address.state = "NY"
    assert address.state == "NY"
