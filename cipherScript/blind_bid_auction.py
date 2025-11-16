# Compare bids in dictionary
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


auction_data = {}
should_continue = True
while should_continue:
    name = input(" Enter your Name: ")
    price = int(input("Enter Your price: "))
    auction_data[name] = price
    #print(auction_data)
    new_bidder = input(" Is there a new bidder? Type 'y' for yes 'n' for No: ")
    if new_bidder == 'n':
        should_continue = False
        find_highest_bidder(auction_data)
    else:
        should_continue = True
        print("\n" * 50)















