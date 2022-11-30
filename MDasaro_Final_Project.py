from Deck import *
import time

def Delay(t=0.5):
    time.sleep(t)

#name = input("Welcome to BlackJack, you start with $100 of chips, please enter your name: ")
#print("Hello "+name+", let's begin!")

print("Welcome to BlackJack, you start with $100, betting starts at $10")
Delay()

class BlackJack():
    def __init__(self):
        self.money = 100
        #Create a Deck and shuffle it
        self.GameDeck = Deck()
        self.GameDeck.shuffle()
        self.play_game()

    def print_info(self, dealer, player, bet):
        dealer_value, player_value = self.update_hands(dealer, player)
        Delay()
        print()
        print('─' * 100)
        print("Dealer: ", end="")
        for card in dealer:
            print(card, "  ", end="")
            Delay()
        print("\nPlayer: ", end="")
        for card in player:
            print(card,"  ", end="")
            Delay()

        print()
        Delay()
        print("     Dealer Value: "+str(dealer_value), format("Player Value: "+str(player_value), "^30"),format("Current Bet: $"+str(bet)+"        Money: "+str(self.money), ">30"))
        print('─' * 100)
        print()
        Delay()
        #Include # of cards left in deck
        #Player value, dealer value, money, bet, # of games won? with good justifications

    def update_hands(self, dealer, player):
        dealer_value = 0
        player_value = 0
        for card in dealer:
            dealer_value += card.get_value()
        for card in player:
            player_value += card.get_value()
        return dealer_value, player_value


    def play_game(self):
        if self.money < 10:
            print("Sorry, you have less than $10, the required amount to bet. Please come again. ")
            exit()

        #Initialize first card draws
        dealer = []
        dealer.append(self.GameDeck.pop_card())
        player = [] 
        player.append(self.GameDeck.pop_card())

        dealer_value = dealer[0].get_value()
        player_value = player[0].get_value()

        bet = 10
        self.print_info(dealer, player, bet)

        #Display current information (dealer cards and total, player cards and total, total money, total bet)
        #Make that a function ^
        self.betting(dealer, player, bet)

    def play_again(self):
        Delay()
        print("\nYou currently have $"+str(self.money))
        Delay()
        again = input("Press 'return' to play again, or 'q' to quit. ")
        if len(again) == 0:
            self.play_game()
        else:
            exit()

    def betting(self, dealer, player, bet):
        Delay()
        dealer_value, player_value = self.update_hands(dealer, player)
        bet_increase = input("Enter amount to increase bet or press 'return' to pass. ")
        
        if len(bet_increase) !=0:
            try:
                bet_increase_int = int(bet_increase)
            except:
                print("Error, bet amount was not a number. \n")
                Delay()
                self.betting(dealer, player, bet)

            if bet_increase_int <= (self.money-bet):
                bet+=bet_increase_int
                print("Bet successfully updated to $"+str(bet))
            else:
                Delay()
                print("You can't increase your bet that much, you only have $"+str(self.money)+"\n")
                self.betting(dealer, player, bet)
        #self.print_info(dealer, player, bet)

        while True: 
            decision = input("Press 'h' to hit or 'p' to pass. ")
            if decision == 'h':
                hit = self.GameDeck.pop_card()
                player.append(hit)
                    
                player_value += hit.get_value() #Should equal play[-1].get_value()

                print("You received a ",end="")
                print(hit) #get random new card
                print()
                Delay()
                
                self.print_info(dealer, player, bet)
                
                
                #show updated information

                if player_value > 21:
                    Delay()
                    print("BUST")
                    print("You lost your bet of $"+str(bet))
                    self.money -= bet

                    self.play_again()
                else:
                    continue
            elif decision == 'p':
                Delay()
                print("Passing, your total is "+ str(player_value)+". Let's see if you beat the dealer. ")
                print()
                while dealer_value < 17:
                    Delay()
                    dealer_hit = self.GameDeck.pop_card()
                    dealer.append(dealer_hit)
                    dealer_value += dealer_hit.get_value()

                    print("The dealer received a ", end="")
                    print(dealer_hit)
                    
                    #Remove this later
                    #print("Dealer is at "+ str(dealer_value))
                    if dealer_value > 21:
                        self.print_info(dealer, player, bet)

                        print("Dealer busted, you win by default! Your money has been increased. "+"\n")
                        self.money += bet
                        Delay()
                        self.play_again()
                #print("Dealer value must be between 17 and 21 I hope, it's: " + str(dealer_value))
                #Display all information
                self.print_info(dealer, player, bet)

                if player_value > dealer_value:
                    Delay()
                    print("Your value is higher than the dealer, you win! You money has been updated. ")
                    self.money += bet
                    self.play_again()
                elif player_value == dealer_value:
                    Delay()
                    print("You've tied in value with the dealer, your bet has been return to you. ")
                    self.play_again()
                else:
                    Delay()
                    print("The dealer has won, you've lost your bet. ")
                    self.money -= bet
                    self.play_again()


Game = BlackJack()