import random
from operator import index

# in this list the last 10, 10, 10 each represent Jack, King, Queen and the 11 is Ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game():
    input("Press any key to START THE GAME: ")

    def compare_hands(player, dealer):
        dealer_win = " Dealer Win"
        player_win = "Player Win"
        draw_hand = "Draw"
        if player > 21:
            return dealer_win
        if dealer > 21:
            return player_win
        if player > dealer:
            return player_win
        if dealer > player:
            return dealer_win
        return draw_hand

    # print 2 random cards as dealer hand and 2 as player hand also add the two numbers each and print
    dealer_hand1, dealer_hand2 = random.sample(cards, 2)
    player_card1, player_card2 = random.sample(cards, 2)
    print(f"Dealer Hand: {dealer_hand1}, {dealer_hand2}, Dealer Score: {dealer_hand1 + dealer_hand2}")
    print(f"Player Hand: {player_card1}, {player_card2}, Current Score: {player_card1 + player_card2}")
    dealer_hand = dealer_hand1 + dealer_hand2
    sum_of_player_hand = player_card1 + player_card2

    # first check if the firsthand player got 21. if he does he win and the game is over
    if sum_of_player_hand == 21:
        print("Jack Player Wins")
        return
    # first check if the firsthand dealer got 21. if he does he win and the game is over
    if dealer_hand == 21:
        print("Black Jack, Dealer Wins")
        return

    ask_second_hand = input("Do you want stand or hit. 'S' for stand 'H' for hit: ").lower()
    if ask_second_hand == 's':
        # compare the hands and print the winner using the compare function
        result = compare_hands(sum_of_player_hand, dealer_hand)
        print(result)

    elif ask_second_hand == "h":
        # the comma between dealer_second_hand and the = sign will unpact the cards list into integer
        dealer_second_hand, = random.sample(cards, 1)
        print(f"Dealer New Score: {dealer_hand}, {dealer_second_hand}, Total: {dealer_hand + dealer_second_hand}")
        player_second_hand, = random.sample(cards, 1)
        print(
            f"Player New Score: {player_second_hand}, {sum_of_player_hand}, {player_second_hand + sum_of_player_hand}")
        dealer_second_hand += dealer_hand
        player_second_hand += sum_of_player_hand
        result = compare_hands(player_second_hand, dealer_second_hand)
        print(result)


play_game()