from abc import ABC, abstractmethod

class LightBulb_bad:

    is_on: bool = False

    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Switch_bad:
   def __init__(self, bulb):
      self.bulb = bulb


# This is better

class Switchable(ABC):

    is_on: bool = False
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Switch:

    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        if self.device.is_on:
            self.device.is_off()
        else:
            self.device.turn_on()
