MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "profit": 0.00,
}


def prompt():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        exit()
    elif choice == "report":
        choice_report()
    else:
        check_resources(choice)
        payment = collect_payment()
        check_money(choice, payment)
        deduct_resources(choice)
        print("Here is your " + choice + ", enjoy!")
        prompt()


# TODO CREATE CHOICE REPORT FUNCTION

def choice_report():
    print("Water: " + str(resources["water"]))
    print("Milk: " + str(resources["milk"]))
    print("Coffee: " + str(resources["coffee"]))
    print("Money: $" + str(money["profit"]))
    prompt()


# TODO CREATE CHECK RESOURCES FUNCTION

def check_resources(coffee_choice):
    if resources["water"] < MENU[coffee_choice]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        prompt()
    elif (coffee_choice != "espresso") and (resources["milk"] < MENU[coffee_choice]["ingredients"]["milk"]):
        print("Sorry there is not enough milk.")
        prompt()
    elif resources["coffee"] < MENU[coffee_choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        prompt()
    else:
        pass


def collect_payment():
    print("Please insert coins.")
    quarter_payment = float(input("how many quarters?: ")) * .25
    dime_payment = float(input("how many dimes?: ")) * .1
    nickel_payment = float(input("how many nickles?: ")) * .05
    penny_payment = float(input("how many pennies?: ")) * .01
    payment = quarter_payment + dime_payment + nickel_payment + penny_payment
    return payment


# TODO CREATE CHECK MONEY FUNCTION

def check_money(coffee_choice, payment):
    if payment < MENU[coffee_choice]["cost"]:
        print("Sorry that's not enough money.  Money refunded.")
        prompt()
    else:
        profit = money["profit"] + MENU[coffee_choice]["cost"]
        money["profit"] = profit
        change = payment - MENU[coffee_choice]["cost"]
        print("Here is $" + str(change) + " in change.")
        pass


def deduct_resources(coffee_choice):
    water_store = resources["water"] - MENU[coffee_choice]["ingredients"]["water"]
    if coffee_choice != "espresso":
        milk_store = resources["milk"] - MENU[coffee_choice]["ingredients"]["milk"]
    coffee_store = resources["coffee"] - MENU[coffee_choice]["ingredients"]["coffee"]
    resources["water"] = water_store
    if coffee_choice != "espresso":
        resources["milk"] = milk_store
    resources["coffee"] = coffee_store


prompt()
