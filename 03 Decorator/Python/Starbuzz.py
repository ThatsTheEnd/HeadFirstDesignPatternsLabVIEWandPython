from abc import ABC
from enum import Enum


class Size(Enum):
    Tall = 1
    Grande = 2
    Venti = 3


class Beverage(ABC):
    """
    Original Starbuzz Class
    """

    def __init__(self):
        self.description = "unknown beverage"
        self.size = Size.Tall

    def get_description(self) -> str:
        return self.description

    def cost(self) -> float:
        pass

    def set_size(self, beverage_size: Size) -> None:
        self.size = beverage_size

    def get_size(self) -> Size:
        return self.size


class CondimentDecorator(Beverage):
    """
    Abstract class for the condiments
    """

    def __init__(self):
        super().__init__()
        self.beverage_that_condiment_wraps = Beverage

    def get_description(self) -> str:
        pass


###############################################################################
# Impleneting all different coffee sorts:
###############################################################################
class Espresso(Beverage):
    """
    Extends also beverage class
    """

    def __init__(self, _size):
        super().__init__()
        self.description = "Espresso"
        self.size = _size

    def cost(self) -> float:
        cost: float
        if self.size == Size.Tall:
            cost = 0.99
        elif self.size == Size.Grande:
            cost = 1.09
        elif self.size == Size.Venti:
            cost = 1.19
        return cost


class HouseBlend(Beverage):
    """
    Extends also beverage class
    """

    def __init__(self, _size):
        super().__init__()
        self.description = "House blend coffee"
        self.size = _size

    def cost(self) -> float:
        return 0.89


class Decaf(Beverage):
    """
    Extends also beverage class
    """

    def __init__(self, _size):
        super().__init__()
        self.description = "Decaffinated Coffee"
        self.size = _size

    def cost(self) -> float:
        return 1.09


class DarkRoast(Beverage):
    """
    Extends also beverage class
    """

    def __init__(self, _size):
        super().__init__()
        self.description = "Dark Roast Coffee"
        self.size = _size

    def cost(self) -> float:
        return 0.99


###############################################################################
# Impleneting concrete Condiments
###############################################################################
class Mocha(CondimentDecorator):
    """
    Mocha is a decorator, so it is a subclass of CondimentDecorator, but CondimentDecorator is a subclass of Beverage
    """

    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage_that_condiment_wraps = beverage

    def get_description(self) -> str:
        return self.beverage_that_condiment_wraps.get_description() + ", Mocha"

    def cost(self) -> float:
        """This has to be repeated for all other drink classes"""
        cost = self.beverage_that_condiment_wraps.cost()
        drink_size = self.beverage_that_condiment_wraps.get_size()
        if drink_size == Size.Tall:
            cost += 0.20
        elif drink_size == Size.Grande:
            cost += 0.25
        elif drink_size == Size.Venti:
            cost += 0.30
        return cost


class SteamedMilk(CondimentDecorator):
    """
    SteamedMilk is a decorator, so it is a subclass of CondimentDecorator,
    but CondimentDecorator is a subclass of Beverage
    """

    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage_that_condiment_wraps = beverage

    def get_description(self) -> str:
        return self.beverage_that_condiment_wraps.get_description() + ", Steamed Milk"

    def cost(self) -> float:
        return self.beverage_that_condiment_wraps.cost() + 0.10


class Soy(CondimentDecorator):
    """
    SteamedMilk is a decorator, so it is a subclass of CondimentDecorator,
    but CondimentDecorator is a subclass of Beverage
    """

    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage_that_condiment_wraps = beverage

    def get_description(self) -> str:
        return self.beverage_that_condiment_wraps.get_description() + ", Soy Milk"

    def cost(self) -> float:
        return self.beverage_that_condiment_wraps.cost() + 0.15


class Whip(CondimentDecorator):
    """
    SteamedMilk is a decorator, so it is a subclass of CondimentDecorator,
    but CondimentDecorator is a subclass of Beverage
    """

    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage_that_condiment_wraps = beverage

    def get_description(self) -> str:
        return self.beverage_that_condiment_wraps.get_description() + ", Whip"

    def cost(self) -> float:
        return self.beverage_that_condiment_wraps.cost() + 0.10


if __name__ == '__main__':
    my_beverage = Espresso(Size.Tall)
    my_beverage = Mocha(my_beverage)
    print("Beverage 1 Tall:" + my_beverage.get_description() + " €" + str(my_beverage.cost()))
    my_beverage = Espresso(Size.Venti)
    my_beverage = Mocha(my_beverage)
    print("Beverage 1 Venti:" + my_beverage.get_description() + " €" + str(my_beverage.cost()))

    my_beverage2 = DarkRoast(Size.Venti)
    my_beverage2 = Mocha(my_beverage2)
    my_beverage2 = Mocha(my_beverage2)
    my_beverage2 = Whip(my_beverage2)
    print("Beverage 2:" + my_beverage2.get_description() + " €" + str(my_beverage2.cost()))

    my_beverage3 = HouseBlend(Size.Venti)
    my_beverage3 = Soy(my_beverage3)
    my_beverage3 = Mocha(my_beverage3)
    my_beverage3 = Whip(my_beverage3)
    print("Beverage 3:" + my_beverage3.get_description() + " €" + str(my_beverage3.cost()))
