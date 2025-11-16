#THIS IS THE FOREX PIP VALUE MEASUREMENT
pip_value = 10

stop_loss = float(input("QOR STOP LOSS LEVEL KAAGA: "))
take_profit = float(input("QOR TAKE PROFIT LEVEL KAAGA: "))
risk_money = float(input("GELI LACAGTA AAD RISK GARAYNAY: $"))

def find_perfect_lot_size():
    """This function calculates the perfect lot size to your position according to your risk amount """
    lot_size = round(risk_money / (stop_loss * pip_value),2)
    TP = take_profit * lot_size * pip_value



   #totalrisk = lot_size * stop_loss * pip_value
    print("**********************")
    print(f"Your lot size is:  ${lot_size}")
    print(f"Your Total risk of this trade is: ${risk_money}")
    print(f"Your expected TP is ${TP}\nGood luck")
    print("**********************")

find_perfect_lot_size()