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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#insertin of money
def coin_processing():
    input("Insert coins:")
    quaters = (int(input("No. of quaters:")) * 0.25)
    dimes = (int(input("No. of dimes:")) * 0.1)
    nickles = (int(input("No. of nickles:")) * 0.05)
    pennies = (int(input("No. of pennies:")) * 0.01)

    sum = quaters + dimes + nickles + pennies
    return sum

#checking if money is enough.

def money_check(given_money , drink_cost):

    if given_money >= drink_cost:
        change = round(given_money - drink_cost , 2 )
        print(f"your change is :{change}")
        global profit
        profit += drink_cost
        return True

    
    else:
        print("Sorry that's not enough money.Money refunded")
        return False
    


#resources checking

def check_resources(order_ingredients):
    for item in order_ingredients:
        resources[item] < order_ingredients[item]
        return "sorry not enough items"
    
def make_coffee(order_ingredients , drink) :
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your drink. Enjoy your {drink}.")       





is_on = True
while is_on:
    ask = input("What would you like (cappuccino , espresso , latte : ")
    if ask == 'report':
        print(f"Water = {resources['water']}ml")
        print(f"Water = {resources['water']}ml")
        print(f"Water = {resources['water']}ml")
        print(f"money = ${profit}ml")

    elif ask == 'off':
        is_on = False

    else:
        drink = MENU[ask]

        if check_resources(drink['ingredients']):
            problem = coin_processing()
            if money_check(problem, drink['cost']):
                    make_coffee(drink['ingredients'] ,ask)
                    
