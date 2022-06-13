from enum import Enum


class PizzaType(Enum):
    cheese = 1
    pepperoni = 2
    clam = 3
    veggie = 4


class Pizza:
    """
    The mother of pizzas
    """

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class CheesePizza(Pizza):
    """
    but with cheese
    """


class PepperoniPizza(Pizza):
    """
    and of course pepperoni
    """


class ClamPizza(Pizza):
    """
    whatever
    """


class VeggiePizza(Pizza):
    """
    trying to be healthy
    """


class SimplePizzaFactory:
    """
    This class has one job: it creates different pizzas
    """

    def __init__(self):
        self.pizza = None

    def create_pizza(self, _type: PizzaType) -> Pizza:
        if _type == PizzaType.cheese:
            self.pizza = CheesePizza()
        elif _type == PizzaType.pepperoni:
            self.pizza = PepperoniPizza()
        elif _type == PizzaType.clam:
            self.pizza = ClamPizza()
        elif _type == PizzaType.veggie:
            self.pizza = VeggiePizza()
        return self.pizza


class PizzaStore:
    """
    Client code for the pizza factory
    """

    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, _type):
        pizza = self.factory.create_pizza(_type)
        pizza.prepare()
        pizza.bake()
        pizza.box()
        pizza.cut()
