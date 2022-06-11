from abc import ABC


class Beverage(ABC):
    """
    Original Starbuzz Class
    """

    def __init__(self):
        self.description = "unknown beverage"

    def get_description(self) -> str:
        return self.description

    def cost(self) -> float:
        pass


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

    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    """
    Extends also beverage class
    """

    def __init__(self):
        super().__init__()
        self.description = "House blend coffee"

    def cost(self) -> float:
        return 0.89


class Decaf(Beverage):
    """
    Extends also beverage class
    """

    def __init__(self):
        super().__init__()
        self.description = "Decaffinated Coffee"

    def cost(self) -> float:
        return 1.09


class DarkRoast(Beverage):
    """
    Extends also beverage class
    """

    def __init__(self):
        super().__init__()
        self.description = "Dark Roast Coffee"

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
        return self.beverage_that_condiment_wraps.cost() + 0.20


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
    my_beverage = Espresso()
    print("Beverage 1:" + my_beverage.get_description() + " €" + str(my_beverage.cost()))

    my_beverage2 = DarkRoast()
    my_beverage2 = Mocha(my_beverage2)
    my_beverage2 = Mocha(my_beverage2)
    my_beverage2 = Whip(my_beverage2)
    print("Beverage 2:" + my_beverage2.get_description() + " €" + str(my_beverage2.cost()))

    my_beverage3 = HouseBlend()
    my_beverage3 = Soy(my_beverage3)
    my_beverage3 = Mocha(my_beverage3)
    my_beverage3 = Whip(my_beverage3)
    print("Beverage 3:" + my_beverage3.get_description() + " €" + str(my_beverage3.cost()))
