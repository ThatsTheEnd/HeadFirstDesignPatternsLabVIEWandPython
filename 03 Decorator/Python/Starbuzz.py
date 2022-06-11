from abc import ABC, abstractmethod


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
    def __init__(self, my_beverage: Beverage):
        super().__init__()
        self.beverage_that_condiment_wraps = my_beverage

    def get_description(self) -> str:
        return self.beverage_that_condiment_wraps.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage_that_condiment_wraps.cost() + 0.20


  class SteamedMilk(CondimentDecorator):
    """
    SteamedMilk is a decorator, so it is a subclass of CondimentDecorator, but CondimentDecorator is a subclass of Beverage
    """
    def __init__(self, my_beverage: Beverage):
        super().__init__()
        self.beverage_that_condiment_wraps = my_beverage

    def get_description(self) -> str:
        return self.beverage_that_condiment_wraps.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage_that_condiment_wraps.cost() + 0.20
