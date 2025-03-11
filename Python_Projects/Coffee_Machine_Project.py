# # #####################  A blueprint of the coffee machine project and its requirements ##########################

# 1. Ask from user for coffee type by prompting:
#     "what would you like to have?(latte/espresso/cappuccino)"   # it should be in loop as it will ask again and again
#     Once the drink is dispence this prompt should be show to serve the next customer.
# 2. When user enters "report"as an input then a report should be generated that shows
#    the current resource value:
#        exmaple: water = 200ml
#        milk = 50ml
#        coffee = 75g
#        money = Rs. 1500
# 3. If the user enter "off" as input then your program should end execution.
# 4. Check sufficient resource are available or not?
# 5. If sufficient resource are available then machine should ask to insert coins and calculate total money received
#    [Coffee Machine only accept 5rs. 10rs. and 20rs. coins]
# 6. Check payment is successful or not
#    if user has entered sufficient money, the cost of drink gets added to the machine as a profit.
#    if user has entered too much money, machine should offer change to the user.
#    and if the money is not sufficient to purchase the drink user has selected, it should print a message
#     "Sorry, that's not enough money. Money refunded"
# 7. Make coffee
#    if payment is successful, ingredient to make the selected drink should be deducted from the coffee machine resource.
#    and it will print the bill. and message "Here is your e.g. cappuccino"
#-----------------------------------------------------draft-------------------------------------------------------------
Menu = {
    "Espresso": {
        "ingredients": {
            "water": 210,
            "milk": 170,
            "coffee": 28
        },
        "cost": 180,
    },
    "Americano": {
        "ingredients": {
            "water": 150,
            "milk": 220,
            "coffee": 26
        },
        "cost": 180,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 25,
        },
        "cost": 200,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 26,
        },
        "cost": 150,
    },
    "Mocha": {
        "ingredients": {
            "water": 100,
            "milk": 250,
            "coffee": 30,
        },
        "cost": 282,
    }
}
profit = 0
resources = {
    "water": 1000,
    "milk": 800,
    "coffee": 100,
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry! There is not enough {item}")
            return False
def process_coins():
    print("Please insert coins.")
    total = 0
    coins_five = int(input("How many 5 Rs. coins do you have?: "))
    coins_tens = int(input("How many 10 Rs. coins do you have?: "))
    coins_twenty = int(input("How many 20 Rs. coins do you have?: "))
    total = coins_five * 5 + coins_tens * 10 + coins_twenty * 20
    return total
def is_payment_successful(money_received,coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"Here is your Rs.{change} in change.")
        return True
    else:
        print("Sorry!! that's not enough money. Money refunded.")
        return False
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
        print(f"Here is your {coffee_name} coffee ☕, Enjoy!!!")

is_on = True
while is_on:
    choice = input("What would you like to have? (Espresso/Americano/Cappuccino/Latte/Mocha): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}gram")
        print(f"Money={profit}Rs")
    else:
        coffee_type = Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredients'])
