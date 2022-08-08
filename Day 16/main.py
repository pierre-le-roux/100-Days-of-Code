from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
till = MoneyMachine()


def main():
    is_on = True

    while is_on:

        choice = input(f"What would you like? ({menu.get_items()}): ").lower()

        if choice == "report":
            machine.report()
            till.report()
        elif choice == "off":
            print("Coffee Machine Turning Off. Good Bye.")
            is_on = False
        elif menu.find_drink(choice):
            drink = menu.find_drink(choice)
            if machine.is_resource_sufficient(drink) and till.make_payment(drink.cost):
                machine.make_coffee(drink)


if __name__ == '__main__':
    main()
