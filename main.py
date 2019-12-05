class Beverage:
    _description = 'Unknown'

    def get_description(self) -> str:
        return self._description

    def cost(self) -> float:
        pass


class Decorator(Beverage):
    _component: Beverage = None

    def __init__(self, component: Beverage) -> None:
        self._component = component

    @property
    def component(self):
        """ Декоратор делегирует всю работу обёрнутому компоненту. """
        return self._component

    def get_description(self) -> str:
        return self._component.get_description()

    def cost(self) -> float:
        return self._component.cost()


class Espresso(Beverage):
    def get_description(self) -> str:
        return 'Espresso'

    def cost(self) -> float:
        return 1.89


class HouseBlend(Beverage):
    def get_description(self) -> str:
        return 'House Blend'

    def cost(self) -> float:
        return .89


class Mocha(Decorator):
    def __init__(self, component: Beverage) -> None:
        super().__init__(component)

    def get_description(self) -> str:
        return super().component.get_description() + ', Mocha'

    def cost(self) -> float:
        return .40 + super().component.cost()


class WhippedCream(Decorator):
    def __init__(self, component: Beverage) -> None:
        super().__init__(component)

    def get_description(self) -> str:
        return super().component.get_description() + ', Whipped Cream'

    def cost(self) -> float:
        return .20 + super().component.cost()


class Milk(Decorator):
    def __init__(self, component: Beverage) -> None:
        super().__init__(component)

    def get_description(self) -> str:
        return super().component.get_description() + ', Milk'

    def cost(self) -> float:
        return .25 + super().component.cost()


class Sugar(Decorator):
    def __init__(self, component: Beverage) -> None:
        super().__init__(component)

    def get_description(self) -> str:
        return super().component.get_description() + ', Sugar'

    def cost(self) -> float:
        return 0 + super().component.cost()


if __name__ == "__main__":
    stop_coffee = False
    print('Welcome to our cozy cafe Decoracofe!')
    print('Your hosts are Ivana Begovic and Svetlana Ruchkina.')
    print('Please, chose your coffee.')
    bev_type = input('Espresso(1) or Home blend(2)?')
    beverage = Espresso()
    if bev_type == "1":
        beverage = Espresso()
    else:
        beverage = HouseBlend()
    while not stop_coffee:
        print('Please, chose additional components:')
        add = input('That`s it, thank you(0) '
                    '\n Sugar, please (1) '
                    '\n Whipped cream, please(2) '
                    '\n Milk, please(3) '
                    '\n Mocha, please(4)')
        if add == "0":
            stop_coffee = True
        elif add == "1":
            beverage = Sugar(beverage)
        elif add == "2":
            beverage = WhippedCream(beverage)
        elif add == "3":
            beverage = Milk(beverage)
        elif add == "4":
            beverage = Mocha(beverage)

    print('Thank you for choosing us! \n Your order is:', beverage.get_description(),
          '\n Your total is:', beverage.cost())
