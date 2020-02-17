class CoffeeMachine:
    def __init__(self):
        self.water_available = 400
        self.milk_available = 540
        self.beans_available = 120
        self.cups_available = 9
        self.money_available = 550
        self.active_state = True
        self.current_action = ""
        self.coffee_type = ""

    # class getters

    def get_water(self):
        return self.water_available

    def get_milk(self):
        return self.milk_available

    def get_beans(self):
        return self.beans_available

    def get_cups(self):
        return self.cups_available

    def get_money(self):
        return self.money_available

    def get_state(self):
        return self.active_state

    def get_action(self):
        return self.current_action

    def get_type(self):
        return self.coffee_type

    # class setters

    def set_water(self, update_value):
        self.water_available += update_value

    def set_milk(self, update_value):
        self.milk_available += update_value

    def set_beans(self, update_value):
        self.beans_available += update_value

    def set_cups(self, update_value):
        self.cups_available += update_value

    def set_money(self, update_value):
        self.money_available += update_value

    def set_state(self, new_state):
        self.active_state = new_state

    def set_action(self, new_action):
        self.current_action = new_action

    def set_type(self, new_type):
        self.coffee_type = new_type

    # available operations

    def exit(self):
        self.set_state(False)

    def print_resources(self):
        print(f"The coffee machine has:")
        print(f"{self.get_water()} of water")
        print(f"{self.get_milk()} of milk")
        print(f"{self.get_beans()} of coffee beans")
        print(f"{self.get_cups()} of disposable cups")
        print(f"{self.get_money()} of money")
        print("")

    def take_money(self):
        print(f"I gave you ${self.get_money()}")
        self.set_money(- self.get_money())

    def fill(self):
        self.set_water(int(input("Write how many ml of water do you want to add: ")))
        self.set_milk(int(input("Write how many ml of milk do you want to add: ")))
        self.set_beans(int(input("Write how many grams of coffee beans do you want to add: ")))
        self.set_cups(int(input("Write how many disposable cups of coffee do you want to add: ")))

    def choose_coffee(self):
        self.set_type(input("What do you want to buy? 1 - espresso, 2 - latte, "
                            "3 - cappuccino, back - to main "))
        return self.get_type()

    def update_resources(self, water, milk, beans, money):
        self.set_water(- water)
        self.set_milk(- milk)
        self.set_beans(- beans)
        self.set_cups(- 1)
        self.set_money(money)

    def check_resources(self, water, milk, beans):
        if self.get_water() - water < 0:
            print("Sorry, not enough water!")
            return False
        elif self.get_milk() - milk < 0:
            print("Sorry, not enough milk!")
            return False
        elif self.get_beans() - beans < 0:
            print("Sorry, not enough coffee beans!")
            return False
        elif self.get_cups() <= 0:
            print("Sorry, not enough cups!")
            return False

    def buy_coffee(self, coffee_type):
        if coffee_type == "1":
            if self.check_resources(250, 0, 16) is not False:
                self.update_resources(250, 0, 16, 4)
                print("I have enough resources, making you a coffee!")
        elif coffee_type == "2":
            if self.check_resources(350, 75, 20) is not False:
                self.update_resources(350, 75, 20, 7)
                print("I have enough resources, making you a coffee!")
        elif coffee_type == "3":
            if self.check_resources(200, 100, 12) is not False:
                self.update_resources(200, 100, 12, 6)
                print("I have enough resources, making you a coffee!")


coffee_machine = CoffeeMachine()

# main loop
while coffee_machine.get_state() is True:
    coffee_machine.set_action(input("Write action (buy, fill, take, remaining, exit): "))
    print("")
    if coffee_machine.get_action() == "exit":
        coffee_machine.set_state(False)
    elif coffee_machine.get_action() == "remaining":
        coffee_machine.print_resources()
    elif coffee_machine.get_action() == "take":
        coffee_machine.take_money()
    elif coffee_machine.get_action() == "fill":
        coffee_machine.fill()
    elif coffee_machine.get_action() == "buy":
        chosen_type = coffee_machine.choose_coffee()
        coffee_machine.buy_coffee(chosen_type)
        print("")
    else:
        print("Only the following actions are available: buy, fill, take, remaining, exit.")
        print("Please type carefully and enter an appropriate action.")
