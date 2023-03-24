from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


cf_maker = CoffeeMaker()
menu = Menu()
money_total = MoneyMachine()

end_game = False

#print(menu_item.name)
def additem(type):
    menu_item.name = type
    menu_item.ingredients = type
    menu_item.cost = type


while not end_game:
    type = input("what the fuck would you order: ").lower()
    if type == 'report':
        cf_maker.report()
        money_total.report()
    elif type == 'off':
        end_game = True
    else:
        menu_item = menu.find_drink(type)
        if cf_maker.is_resource_sufficient(menu_item):
            if money_total.make_payment(menu_item.cost):
                cf_maker.make_coffee(menu_item)

        


