# Write your code here
water_per_cup = 200
milk_per_cup = 50
beans_per_cup = 15
water_available = 400
milk_available = 540
beans_available = 120
cups_available = 9
money_available = 550


def print_status():
    print(f"The coffee machine has:")
    print(f"{water_available} of water")
    print(f"{milk_available} of milk")
    print(f"{beans_available} of coffee beans")
    print(f"{cups_available} of disposable cups")
    print(f"{money_available} of money")


def resource_check(water, milk, beans):
    global water_available
    global milk_available
    global beans_available
    global money_available
    global cups_available
    if water_available - water < 0:
        print("Sorry, not enough water!")
    elif milk_available - milk < 0:
        print("Sorry, not enough milk!")
    elif beans_available - beans < 0:
        print("Sorry, not enough coffee beans!")
    elif cups_available <= 0:
        print("Sorry, not enough cups!")
    else:
        water_available -= water
        milk_available -= milk
        beans_available -= beans
        cups_available -= 1
        return True


def take_action():
    while True:
        action = input("Write action(buy, fill, take, remaining, exit): ")
        global water_available
        global milk_available
        global beans_available
        global money_available
        global cups_available
        if action == "buy":
            coffee_type = input("What do you want to buy? 1 - espresso, "
                                "2 - latte, 3 - cappuccino: 3, back -  to main menu: ")
            if coffee_type == "1":
                water_needed = 250
                milk_needed = 0
                beans_needed = 16
                if resource_check(water_needed, milk_needed, beans_needed):
                    money_available += 4
                    print("I have enough resources, making you a coffee!")
            elif coffee_type == "2":
                water_needed = 350
                milk_needed = 75
                beans_needed = 20
                if resource_check(water_needed, milk_needed, beans_needed):
                    money_available += 7
                    print("I have enough resources, making you a coffee!")
            elif coffee_type == "3":
                water_needed = 200
                milk_needed = 100
                beans_needed = 12
                if resource_check(water_needed, milk_needed, beans_needed):
                    money_available += 6
                    print("I have enough resources, making you a coffee!")
            elif coffee_type == "back":
                pass
        elif action == "fill":
            added_water = int(input("Write how many ml of water do you want to add: "))
            water_available += added_water
            added_milk = int(input("Write how many ml of milk do you want to add: "))
            milk_available += added_milk
            added_beans = int(input("Write how many grams of coffee beans do you want to add: "))
            beans_available += added_beans
            added_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
            cups_available += added_cups
        elif action == "take":
            print(f"I gave you ${money_available}")
            money_available = 0
        elif action == "remaining":
            print_status()
        elif action == "exit":
            return False


take_action()
