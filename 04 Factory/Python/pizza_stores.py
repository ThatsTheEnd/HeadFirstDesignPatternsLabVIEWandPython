from pizzas import *  # I know consered bad design, but don't have the time to rework it here


class PizzaStore(ABC):
    """
    Client code for the pizza factory
    """

    def __init__(self, ):
        self.pizza: Pizza

    @abstractmethod
    def create_pizza(self, _type: PizzaType) -> Pizza:
        pass

    def order_pizza(self, _type) -> Pizza:
        pizza = self.create_pizza(_type)
        print(f'--- Making a {pizza.get_name()} ---"')
        pizza.prepare()
        pizza.bake()
        pizza.box()
        pizza.cut()
        return pizza


class NYPizzaStore(PizzaStore):
    """
    implements the abstract methods of the pizza store
    """
    def create_pizza(self, _type: PizzaType) -> Pizza:
        if _type == PizzaType.cheese:
            return NYStyleCheesePizza()

        elif _type == PizzaType.pepperoni:
            return NYStylePepperoniPizza()

        else:
            raise Exception('The Pizzatype has not been implemented yet due to laziness of the programmer')
