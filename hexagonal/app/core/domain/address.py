class Address:
    def __init__(self, street: str, city: str, state: str):
        self.__street = street
        self.__city = city
        self.__state = state

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        self.__street = street

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
