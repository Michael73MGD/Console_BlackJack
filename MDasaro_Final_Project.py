from Deck import *
import time

name = input("Welcome to BlackJack, you start with $100 of chips, please enter your name: ")
print("Hello "+name+", let's begin!")
time.sleep(0.5)

money = 100

def Delay(t=0.5):
    time.sleep(t)

def print_info(dealer, player, bet):
    dealer_value, player_value = update_hands(dealer, player)
    Delay()
    print("Dealer: ", end="")
    for card in dealer:
        print(card, "  ")
        Delay()
    print("Player: ", end="")
    for card in player:
        print(card,"  ")
        Delay()

    print()
    Delay()
    print("Dealer Value: "+str(dealer_value), format("Player Value: "+str(player_value), "^30"),format("Current Bet: $"+str(bet)+"        Money: "+str(money), ">30"))

    
    #Include # of cards left in deck
    #Player value, dealer value, money, bet, # of games won? with good justifications

def update_hands(dealer, player):
    dealer_value = 0
    player_value = 0
    for card in dealer:
        dealer_value += card.get_value()
    for card in player:
        player_value += card.get_value()
    return dealer_value, player_value


def play_game(money):
    if money < 10:
        print("Sorry, you have less than $10, the required amount to bet. Please come again. ")
        exit()

    #Create a Deck and shuffle it
    GameDeck = Deck()
    GameDeck.shuffle()

    #Initialize first card draws
    dealer = []
    dealer.append(GameDeck.pop_card())
    player = [] 
    player.append(GameDeck.pop_card())

    dealer_value = dealer[0].get_value()
    player_value = player[0].get_value()

    bet = 10
    print_info(dealer, player, bet)

    #Display current information (dealer cards and total, player cards and total, total money, total bet)
    #Make that a function ^
    betting(dealer, player, bet, money)

def play_again():
    again = input("Press 'return' to play again, or 'q' to quit. ")
    if len(again) == 0:
        play_game()
    else:
        exit()

def betting(dealer, player, bet, money):
    dealer_value, player_value = update_hands(dealer, player)
    bet_increase = input("Enter amount to increase bet or press 'return' to pass. ")
    
    if len(bet_increase) !=0:
        try:
            bet_increase_int = int(bet_increase)
        except:
            print("Error, bet amount was not a number. ")

        if bet_increase_int < money:
            bet+=bet_increase_int
            money-=bet_increase_int

    print_info(dealer, player, bet)

    while True: 
        decision = input("Press 'h' to hit or 'p' to pass. ")
        if decision == 'h':
            print("You received a ") #get random new card
            #show updated information
            if player_value > 21:
                print("BUST")
                print("You lost your bet of $"+str(bet))
                money -= bet

                play_again()
            else:
                continue
        elif decision == 'p':
            print("Passing, your total is "+ str(player_value)+". Let's see if you beat the dealer. ")
            while dealer_value < 17:
                d2 = 1 #get random card
                dealer_value += d2 #value of card
                print("The dealer received a " + str(d2))
                print("Dealer is at "+ str(dealer_value))
                if dealer_value > 21:
                    print("Dealer busted, you win by default! Your money has been increased. ")
                    money += bet
                    play_again()
            print("Dealer value must be between 17 and 21 I hope, it's: " + str(dealer_value))
            #Display all information
            if player_value > dealer_value:
                print("Your value is higher than the dealer, you win! You money has been updated. ")
                money += bet
                play_again()
            if player_value == dealer_value:
                print("You've tied in value with the dealer, your bet has been return to you. ")
                play_again()


play_game(money)