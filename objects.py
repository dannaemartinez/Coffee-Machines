from abc import abstractmethod

class IBrewAll():
    @abstractmethod
    def brewingAll(self):
        pass

class IGrindAll():
    @abstractmethod
    def grindingAll(self):
        pass

class IServeCoffee():
    @abstractmethod
    def servingAll(self):
        pass

class IBlackType():
    @abstractmethod
    def black(self):
        pass

class IEspressoType():
    @abstractmethod
    def espresso(self):
        pass

class IIcedColdCoffee():
    @abstractmethod
    def icecoldcoffee(self):
        pass