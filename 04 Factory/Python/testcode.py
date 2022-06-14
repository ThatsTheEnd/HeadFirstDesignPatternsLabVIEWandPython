from pizzas import *
from pizza_stores import NYPizzaStore

if __name__ == '__main__':
    ethans_ny_pizza_store = NYPizzaStore()
    my_pizza_nr1 = ethans_ny_pizza_store.order_pizza(PizzaType.cheese)
    my_pizza_nr2 = ethans_ny_pizza_store.order_pizza(PizzaType.pepperoni)
    # my_pizza_nr3 = ethans_ny_pizza_store.order_pizza(PizzaType.veggie)  # This will throw an error
