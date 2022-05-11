class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def make_coffee(self, water, milk, coffee_beans, money):
        self.water -= water
        self.milk -= milk
        self.coffee_beans -= coffee_beans
        self.disposable_cups -= 1
        self.money += money

    def check_ingredients(self, water, milk, coffee_beans):
        if self.water < water:
            print('Sorry, not enough water!')
            if self.milk < milk:
                print('Sorry, not enough milk!')
            if self.coffee_beans < coffee_beans:
                print('Sorry, not enough coffee beans!')
            if self.disposable_cups < 1:
                print('Sorry, not enough disposable cups!')
            return False
        elif self.milk < milk:
            print('Sorry, not enough milk!')
            if self.coffee_beans < coffee_beans:
                print('Sorry, not enough coffee_beans!')
            if self.disposable_cups < 1:
                print('Sorry, not enough disposable cups!')
            return False
        elif self.coffee_beans < coffee_beans:
            print('Sorry, not enough coffee_beans!')
            if self.disposable_cups < 1:
                print('Sorry, not enough disposable cups!')
            return False
        elif self.disposable_cups < 1:
            print('Sorry, not enough disposable cups!')
            return False
        else:
            print('I have enough resources, making you a coffee!')
            return True

    def fill_coffee_machine(self):
        water = int(input('Write how many ml of water you want to add: \n'))
        self.water += water
        milk = int(input('Write how many ml of milk you want to add: \n'))
        self.milk += milk
        coffee_beans = int(input('Write how many grams of coffee beans you want to add: \n'))
        self.coffee_beans += coffee_beans
        disposable_cups = int(input('Write how many disposable cups of coffee you want to add: \n'))
        self.disposable_cups += disposable_cups

    def take_money(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def current_ingredients(self):
        print('\nThe coffee machine has:')
        print(f'{self.water} ml of water\n{self.milk} ml of milk\n{self.coffee_beans} g of coffee beans\n'
              f'{self.disposable_cups} disposable cups\n${self.money} of money')

    def make_espresso(self):
        water = 250
        milk = 0
        coffee_beans = 16
        money = 4
        if self.check_ingredients(water=water, milk=milk, coffee_beans=coffee_beans):
            self.make_coffee(water=water, milk=milk, coffee_beans=coffee_beans, money=money)

    def make_latte(self):
        water = 350
        milk = 75
        coffee_beans = 20
        money = 7
        if self.check_ingredients(water=water, milk=milk, coffee_beans=coffee_beans):
            self.make_coffee(water=water, milk=milk, coffee_beans=coffee_beans, money=money)

    def make_cappuccino(self):
        water = 200
        milk = 100
        coffee_beans = 12
        money = 6
        if self.check_ingredients(water=water, milk=milk, coffee_beans=coffee_beans):
            self.make_coffee(water=water, milk=milk, coffee_beans=coffee_beans, money=money)


my_coffee_machine = CoffeeMachine()

while True:
    action = input('\nWrite action (buy, fill, take, remaining, exit): \n')

    if action == 'exit':
        break

    elif action == 'buy':

        buy_coffee = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, '
                           'back - to main menu: \n')
        if buy_coffee == '1':
            my_coffee_machine.make_espresso()

        elif buy_coffee == '2':
            my_coffee_machine.make_latte()

        elif buy_coffee == '3':
            my_coffee_machine.make_cappuccino()

        elif buy_coffee == 'back':
            continue
        else:
            print('Incorrect input!')

    elif action == 'fill':
        my_coffee_machine.fill_coffee_machine()

    elif action == 'take':
        my_coffee_machine.take_money()

    elif action == 'remaining':
        my_coffee_machine.current_ingredients()

    else:
        print('Incorrect input!')
