from __future__ import annotations
from abc import ABC, abstractmethod

###############################################################################
# Observers
###############################################################################


class Observer(ABC):
    """..."""
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        pass


class DisplayElement(ABC):
    """..."""
    @abstractmethod
    def display(self):
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data_object: WeatherData):
        self.temperature = 0
        self.humidity = 0
        self.weather_data = weather_data_object
        self.weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}°C and {self.humidity} %humidity")


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self._max_temp = 0.0
        self._min_temp = 200
        self._temp_sum = 0.0
        self._num_readings = 0
        self._weather_data = weather_data

        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self._temp_sum += temp
        self._num_readings += 1

        if temp > self._max_temp:
            self._max_temp = temp

        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self):
        avg_temp = self._temp_sum / self._num_readings
        print("Statistics Avg/Max/Min temperature = {0}/{1}/{2}".format(
            avg_temp, self._max_temp, self._min_temp))


###############################################################################
# Subjects
###############################################################################


class Subject(ABC):
    """..."""
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
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


if __name__ == '__main__':
    my_weatherdata = WeatherData()
    first_display = CurrentConditionsDisplay(my_weatherdata)
    statistics_display = StatisticsDisplay(my_weatherdata)
    my_weatherdata.set_measurements(25, 80, 1008)
    my_weatherdata.set_measurements(26, 85, 1010)
    my_weatherdata.set_measurements(27, 87, 1020)


