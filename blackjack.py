import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):

        self.deck = []
        for suit in suits :
            for rank in ranks :

                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        deck_comp = ''
        for card in self.deck :
            deck_comp += '\n' + card.__str__()
        return deck_comp

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces :
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips) :

    while True:
        try:
            get_bet = int(input('Please, insert your bet'))
        except:
            print('Please, enter a valid integer')
            continue
        else:
            if get_bet > chips.total :
                print(f'Sorry, you don\'t have enought funds. You have {chips.total}')
                continue
            else :
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while playing:
        get_card = input('Do you want to hit or stand. Use h or s')
        if get_card[0].lower() == 'h':
            hand.add_card(deck.deal())
            hand.adjust_for_ace()
        elif get_card[0].lower() == 's' :
            print('Player stands, Dealers\' turn')
            playing = False
        else:
            print('Sorry, I didn\'t understand that')
            break;


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print('Player BUSTS')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player wins')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Dealer BUSTS')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer wins')
    chips.lose_bet()


def push(player, dealer, chips):
    print('Dealer and Player have the same number.')



while True:
    print('Welcome to blackjack!!')
    deck = Deck()
    deck.shuffle()

    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player, dealer)
    while playing:
        hit_or_stand(deck, player)
        show_some(player_hand, dealer_hand)

        if player.value > 21 :
            player_busts(player, dealer, chips)
            break

    if player.value <= 21:

        while dealer.value < 17 :
            hit(deck, dealer)

        show_all(player, dealer)

        if dealer.value > 21 :
            dealer_busts(player, dealer, chips)
        elif dealer.value > player.value :
            dealer_wins(player, dealer, chips)
        elif dealer.value < player.value :
            player_wins(player, dealer, chips)
        else :
            player_wins(player, dealer, chips)


    new_game = str(input('Would you like a new game? n or y?'))
    if new_game[0].lower() == 'y' :
        continue
    else :
        break