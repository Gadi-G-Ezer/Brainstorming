ENGINE_VALID_VALUES = {'electric', 'diesel', 'gas', 'hybrid'}


class Vehicle:

    def __init__(self, *, color: str, price: float or int, engine: str, number_of_wheels=4):
        if type(color) != str or (type(price) != float and type(price) != int) or type(engine) != str or type(number_of_wheels) != int:
            raise TypeError(f'Error: expecting color: str, price: int or float, engine: str, number_of_wheels: int, '
                            f'but received color: {type(color)}, price: {type(price)}, engine: {type(engine)}, '
                            f'number_of_wheels: {type(number_of_wheels)}')
        if engine not in ENGINE_VALID_VALUES:
            raise ValueError(f'Error: engine parameter expecting values: {ENGINE_VALID_VALUES}, but received {engine}!')
        self._color = color
        self._price = price
        self._engine = engine
        self._number_of_wheels = number_of_wheels

    def get_color(self):
        return self._color

    def get_price(self):
        return self._price

    def update_price(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError(f'Error: expecting value: int or float, but received value: {type(value)}')
        else:
            self._price = value


class ElectricCar(Vehicle):
    """
    Inherits from Vehicle class
    • The engine attribute should be ‘electric’ without receiving this as a parameter in the constructor
    • The electric cars for now can also be assumed to have 4 wheels so no need to receive this in the constructor
    • Additional attributes:
    • _dist_range – range of distance (in kilometers) that the car can traveled on the current charge.
    """

    def __init__(self, *, color: str, price: float or int, dist_range: float or int):
        if type(dist_range) != int and type(dist_range) != float:
            raise TypeError(f'Error: expecting dist_range: int or float but received dist_range: {type(dist_range)}!')
        super().__init__(color=color, price=price, engine='electric', number_of_wheels=4)
        self._dist_range = dist_range

    def update_dist_range(self, new_dist_range):
        """
        update_dist_range(new_ dist_range)  will be called upon charging the car with new range in km that this car can travel
        :param new_dist_range:
        """
        if type(new_dist_range) != int and type(new_dist_range) != float:
            raise TypeError(f'Error: expecting new_dist_range: int or float but received new_dist_range: {type(new_dist_range)}!')
        self._dist_range = new_dist_range

    def is_journey_possible(self, journey_dist_range):
        """
        is_journey_possible(journey_ dist_range)  will return True/False whether the car can make the journey
        with the given range depending on the current charge/range.
        :param journey_dist_range:
        """
        if type(journey_dist_range) != int and type(journey_dist_range) != float:
            raise TypeError(f'Error: expecting journey_dist_range: int or float but received journey_dist_range: {type(journey_dist_range)}!')
        return journey_dist_range <= self._dist_range


class HybridCar(Vehicle):
    """
    HybridCar class definition:
    • Inherits from Vehicle class as well
    • The engine attribute should be ‘hybrid’ without receiving this as a parameter in the constructor
    • Hybrid cars for now can also be assumed to have 4 wheels so no need to receive this in the constructor
    • Addition attributes:
    o _fuel_level (in percentages of a full gas tank)
    """

    def __init__(self, *, color: str, price: float or int, fuel_level: float or int):
        if type(fuel_level) != float and type(fuel_level) != int:
            raise TypeError(f'Error: expecting fuel_level: float or int, but received fuel_level: {type(fuel_level)}!')
        elif fuel_level < 0 or fuel_level > 100:
            raise TypeError(f'Error: expecting 0 <= fuel_level <= 1, but received fuel_level={fuel_level}!')

        super().__init__(color=color, price=price, engine='hybrid', number_of_wheels=4)
        self._fuel_level = fuel_level

    def refuel(self):
        """
        refuel() – fills the gas tank to 100%
        """
        self._fuel_level = 100


def main():
    car = Vehicle(color='red', price=12000, engine='gas', number_of_wheels=6)
    electric = ElectricCar(color='green', price=13000, dist_range=0)
    hybrid = HybridCar(color='blue', price=14000, fuel_level=0)

    assert car.get_color() == 'red'
    assert electric.get_color() == 'green'

    assert hybrid.get_price() == 14000

    electric.update_price(10000)
    assert electric.get_price() == 10000

    electric.update_dist_range(250)
    assert electric.is_journey_possible(180)

    hybrid.refuel()
    assert hybrid._fuel_level == 100


if __name__ == '__main__':
    main()
