from abc import ABC


class Subject(ABC):
    """..."""
    def register_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self):
        pass


class Observer(ABC):
    """..."""

    def update(self, temp: float, humidity: float, pressure: float):
        pass


class DisplayElement(ABC):
    """..."""

    def display(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self.observers: list = []
        self.temperature: float = 0
        self.humidity: float = 0
        self.presssure: float = 0

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for single_observer in self.observers:
            single_observer.update(self.temperature, self.humidity, self.presssure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp: float, humid: float, press: float):
        self.temperature = temp
        self.humidity = humid
        self.presssure = press
        self.measurements_changed()
