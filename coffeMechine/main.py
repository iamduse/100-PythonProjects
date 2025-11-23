from virtualenv.seed.wheels import pip_wheel_env_run

from menu import MENU, resources

# TODO 1: ask the use his order
# A: check the user order and process what to do next:
# B: show feedback to th user if his oder is completed
espresso =  MENU["espresso"]
latte = MENU["latte"]
cappuccino = MENU["cappuccino"]
all_ingredients = [data["ingredients"] for data in MENU.values()]
invest_coffee = resources["coffee"]
invest_water = resources["water"]
invest_milk = resources["milk"]

# report variables
profit =  0
def menu_function():
    print("*************")
    print("MENU ")
    print(f"1.Espresso: cost: ${espresso["cost"]} ")
    print(f"2.Latte: cost: ${latte["cost"]} ")
    print(f"3.Cappuccino: cost: ${cappuccino["cost"]} ")
    print("*************")
# convert coins to full dollar
def coin_to_dollar(pennies=0, nickels=0, dimes=0, quarters=0):
    return (
        pennies * 0.01 +
        nickels * 0.05 +
        dimes * 0.10 +
        quarters * 0.25
    )
def ask_for_coins():
    pennies = int(input("How many pennies: "))
    nickels = int(input("How many nickels: "))
    dimes = int(input("How many dimes: "))
    quarters = int(input("How many quarters: "))
    return coin_to_dollar(pennies, nickels, dimes, quarters)

def collect_payment():

    total_money = round(ask_for_coins(),2)
    print("****************")
    print(f"Total money: ${total_money}")
    profit = total_money

    # check if the total coins are less than the order price is so print not enough money
    # you are short that amount to process the order.
    if payment > total_money:
        print(f"Not enough Money!! You are short ${round(payment - total_money,2 )} ")
        shortage= input("ADD the remaining or cancel your order: 'A' for add 'C' for cancel ")
        if shortage == "a".lower():
            new_total_money = round(ask_for_coins(),2)
            new_total_money += total_money
            print(new_total_money)

            # Still not enough after adding? second attempt
            if payment > new_total_money:
                shortage = round(payment- new_total_money,2)
                print(f"You are short ${shortage}, Order Cancelled and Your money is refunded. ")


        else:
            print("Order Cancelled")
    else:
        #Print the payment - the total as change
        print(f"Here is your change: ${round(total_money - payment,2)}")
        # print(f"Enjoy Your Coffee")
        #Print here is your order.  Enjoy.
        # in here calculate the resource of the coffee and minus this order

# TODO 2: make coffee
def make_coffee():


    print(f"Enjoy Your espresso")

print("Welcome to Magol Coffee: ")
menu_function()
order =input("Press 1,2 or 3 to choose the menu: ")
if order == "espresso":
    print("Please Insert Coins")
    payment = espresso["cost"]
    collect_payment()
    make_coffee()
elif order == "latte":
    print("Please Insert Coins")
    payment = latte["cost"]
    collect_payment()
    print(f"Enjoy Your Latte")
elif order == "cappuccino":
    print("Please Insert Coins")
    payment = cappuccino["cost"]
    collect_payment()
    print(f"Enjoy Your Cappuccino")
elif order == "report":
    print("****************")
    make_coffee()
else:
    print("You choose wrong order")






# TODO: once u got the order and the money execute the making function

