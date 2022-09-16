from objects import IBrewAll, IGrindAll, IServeCoffee, IBlackType, IEspressoType

class PMachine(IBrewAll, IGrindAll, IServeCoffee, IBlackType, IEspressoType):
    def __init__(self) -> None:
        super().__init__()
        print('*** Coffee Premium Machine ***')

    def grindingAll(self):
        print(" -> I'm grinding the coffee")
    def brewingAll(self):
        print(" -> I'm brewing the coffee")
    def servingAll(self):
        print(" -> I'm serving the coffee")
    def black(self):
        print(" -> I'm black coffee")
    def espresso(self):
        print(" -> I'm espresso coffee")
    def icecoldcoffee(self):
        print(" -> I'm ice cold coffee")