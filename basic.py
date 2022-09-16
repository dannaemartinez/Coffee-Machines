from objects import IBrewAll, IServeCoffee, IBlackType

class CBMachine(IBrewAll, IServeCoffee, IBlackType):
    def __init__(self) -> None:
        super().__init__()
        print('*** Coffee Basic Machine ***') 

    def brewingAll(self):
        print(" -> I'm brewing the coffee")
    def servingAll(self):
        print(" -> I'm serving the coffee")
    def black(self):
        print(" -> I'm black coffee")