from enum import Enum
from abc import ABC


class PizzaType(Enum):
    cheese = 1
    pepperoni = 2
    clam = 3
    veggie = 4


class Pizza(ABC):
    """
    The mother of pizzas
    """

    def __init__(self):
        self.name: str = ''
        self.dough: str = ''
        self.sauce: str = ''
        self.toppings: list = []

    def prepare(self):
        print("Prepare " + self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for item in self.toppings:
            print(item)

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cut the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self) -> str:
        return self.name


class NYStyleCheesePizza(Pizza):
    """
    but with cheese
    """

    def __init__(self):
        super(NYStyleCheesePizza, self).__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")


class NYStylePepperoniPizza(Pizza):
    """
    but with cheese
    """

    def __init__(self):
        super(NYStylePepperoniPizza, self).__init__()
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Sliced Pepperoni")
        self.toppings.append("Garlic")
        self.toppings.append("Onion")
