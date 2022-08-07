from bill_of_materials import drinks, coins
from art import text2art

logo = text2art('Coffee\nMachine', font='random')

machine_resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}


def sufficient_resources(drink):
    """checks if the coffee machine has sufficient resources to make
    the requested drink.

    Args:
        drink (string): drink specified by the user

    Returns:
        bool: whether of not the machine can make the drink
    """
    bom = drinks[drink]

    for resource in machine_resources:
        if resource != 'money':
            if bom[resource] > machine_resources[resource]:
                print(f'Sorry there isn\'t enough {resource}')
                return False
    return True


def sum_coins():
    """Asks the user the amount of each coin he wants to add to the machine
    and then sums the values of those coins.

    Returns:
        float: _description_
    """
    total = 0
    for coin in coins:
        total = int(input(f'How many {coin}s? ')) * coins[coin]
    return total


def paid_enough(money, drink):
    """Has the user paid enough to buy the requested drink

    Args:
        money (float): amount of coins deposited
        drink (string): drink specified by user

    Returns:
        bool: whether the user provided enough money
    """
    return money >= drinks[drink]['price']


def refund(money, drink):
    if paid_enough(money, drink):
        cost = drinks[drink]['price']
        refund = money - cost
        machine_resources['money'] += cost
        update_resources(drink)
        if refund:
            print(f'Here is your ${refund} in change.')
        print(f' is your {drink}, enjoy!')
    else:
        print("Sorry that's not enough money. Money refunded")


def update_resources(drink):
    """updates the machine's resources

    Args:
        drink (string): drink choice from user
    """
    bom = drinks[drink]

    for resource in machine_resources:
        if resource != 'money':
            machine_resources[resource] -= bom[resource]


def main():
    print(logo)
    choice = input(f'What would you like? {list(drinks.keys())}: ').lower()

    if choice == 'report':
        print(machine_resources)
    else:
        if sufficient_resources(choice):
            money = sum_coins()
            refund(money, choice)

    main()


if __name__ == '__main__':
    main()
