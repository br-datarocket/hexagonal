from hexagonal.app.core.domain.address import Address


class Customer:
    def __init__(
        self,
        id: str,
        name: str,
        address: Address,
        cpf: str,
        is_valid_cpf: bool = False,
    ):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__cpf = cpf
        self.__is_valid_cpf = is_valid_cpf

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def is_valid_cpf(self):
        return self.__is_valid_cpf

    @is_valid_cpf.setter
    def is_valid_cpf(self, is_valid_cpf):
        self.__is_valid_cpf = is_valid_cpf
