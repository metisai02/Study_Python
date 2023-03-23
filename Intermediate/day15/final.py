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
    "coin": 0,
}


def report():
   # global resources
    print(resources['water'])
    print(resources['milk'])
    print(resources['coffee'])
    print(resources["coin"])


def calculate_drink(type):
    global resources
    resources["water"] = resources["water"] - MENU[type]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[type]["ingredients"]["water"]
    resources["coin"] = resources["coin"] + MENU[type]["cost"]


def calculate_money():
    print("pls insert ur coin:")
    q = float(input("how many quarters?: "))
    d = float(input("how many dimes?  : "))
    n = float(input("how many nickles?: "))
    p = float(input("how many pennies?: "))
    ketqua = 0.25*q + d*0.1 + n*0.05 + p*0.01
    return ketqua


def left_money(total, type):
    return total - MENU[type]["cost"]


def rezult(type, money):
    global resources
    if money - MENU[type]["cost"] > 0:
        print(resources["water"] - MENU[type]["ingredients"]["water"])
        if (resources["water"] - MENU[type]["ingredients"]["water"]) > 0 and (resources["milk"] - MENU[type]["ingredients"]["milk"]) > 0:
            calculate_drink(type)
            print(f"here is {left_money(money,type)} in change")
            print(f"here is ur {type}")
        else:
            print("does not enough")
    else:
        print("may khong du tien")


while True:
    type = input("what would you like? espreso,latte, cappuchino")
    if type == 'report':
        report()
    else:
        money = calculate_money()
        rezult(type, money)
