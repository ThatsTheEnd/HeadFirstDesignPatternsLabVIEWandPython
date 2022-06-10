from abc import ABC, abstractmethod


class Beverage(ABC):
    """
    Original Starbuzz Class
    """

    def __init__(self):
        self.description = "unknown beverage"

    def get_description(self) -> str:
        return self.description

    def cost(self):
        pass


class CondimentDecorator(Beverage):
    """
    Abstract class for the condiments
    """

    def __init__(self):
        super.__init__()
        self.beverage_that_condiment_wraps = Beverage

    def get_description(self) -> str:
        pass
