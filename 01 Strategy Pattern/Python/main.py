class FlyBehavior:
    """
    Where all the flying is done
    """
    def __init__(self):
        print('An object for the FlyBehavior class is created ...')

    def flying_with_wings(self):
        print("flap flap with wings")

    def no_way_i_am_flying(self):
        print("I can't fly")

    def fly_rocket_powered(self):
        print("I'm flying with a rocket!")


class QuackBehavior:
    """
    where all the quacking is done
    """
    def __init__(self):
        print('An object for the QuackBehavior class is created ...')

    def quack(self):
        print("quack quack")

    def no_sound(self):
        print("*awkward silence*")


class Duck:
    """
    This is my main Duck class
    """
    def __init__(self):
        self.make_sound = QuackBehavior()
        self.do_fly = FlyBehavior()

    def swim(self):
        print("swimming is done here, even by plastic ducks...")

    def display(self):
        print("look at how pretty I am")

    def fly(self):
        print("This is not implemented here")

    # @property
    # def fly_behavior(self):
    #     return self.fly_behavior
    #



class MallardDuck(Duck):
    """
    This is my bla
    """
    def __init__(self):
        super(MallardDuck, self).__init__()
        self.my_behavior = self.do_fly.flying_with_wings

    def fly(self):
        self.my_behavior()

    def new_fly_behavior(self, new_fly_behavior):
        self.my_behavior = new_fly_behavior


class PlasticDuck(Duck):
    """
    This is my bla
    """
    def __init__(self):
        super(PlasticDuck, self).__init__()

    def fly(self):
        self.do_fly.no_way_i_am_flying()


if __name__ == '__main__':
    print("here we go:")
    # Testcode for Mallard duck
    real_duck = MallardDuck()
    real_duck.swim()
    real_duck.display()
    real_duck.fly()
    real_duck.new_fly_behavior(real_duck.do_fly.fly_rocket_powered)
    real_duck.fly()
    # Testcode for Plastic Duck
    plastic_duck = PlasticDuck()
    plastic_duck.swim()
    plastic_duck.display()
    plastic_duck.fly()
    pass
