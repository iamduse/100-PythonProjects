#THIS IS THE FOREX PIP VALUE MEASUREMENT
pip_value = 10

def find_perfect_lot_size():
    """This function calculates the perfect lot size to your position according to your risk amount """
    row_lot_size = risk_money / (stop_loss *pip_value)
    lot_size = round(row_lot_size,2)
    TP = take_profit * row_lot_size * pip_value


   #totalrisk = lot_size * stop_loss * pip_value
    print("**********************")
    print(f"Your lot size is:  ${lot_size}")
    print(f"Your Total risk of this trade is: ${risk_money}")
    print(f"Your expected TP is ${TP}\nGood luck")
    print("**********************")


restart = True
while restart:
    print("LOT SIZE CALCULATOR FOR CFD MARKETS: ")
    stop_loss = float(input("ENTER YOUR STOP LOSS PIPS: "))
    risk_money = float(input("ENTER YOUR RISK DOLLAR AMOUNT:$"))
    take_profit = float(input("ENTER YOUR TARGET PIPS: "))
    find_perfect_lot_size()

    should_restart = input("Do you want to calculate another pair, type 'Y' for yes 'N' for No; ").lower()
    if should_restart == "n":
        print("GOOD LUCK, YOU GOT THIS!")
        restart = False







