#total = 0
#x = int(input("please enter a number : "))
#for i in range(x):
#    if i % 3 == 0:
#        total += i
#for j in range(x):
#    if j % 5 == 0:
#        total += j
#print(total)
#

#prime_list = list()
#
#prime_list.append(2)
#
#sayi = 3
#
#while True:
#    prime = True
#    for i in range(2, int(sayi** 0.5)+1):
#        if sayi %i == 0:
#            prime = False
#            break
#    if prime:
#        prime_list.append(sayi)
#        if len(prime_list) == 10000:
#            break
#    sayi += 1
#liste2 = []
#for prime in prime_list:
#    strprime = str(prime)
#    if strprime.startswith("3") and strprime.endswith("7"):
#        liste2.append(prime)

#print(liste2)
#print(len(liste2))

#import random
#
#class Card:
#    def __init__(self, suit, rank):
#        self.suit = suit
#        self.rank = rank
#
#    def __str__(self):
#        return f"{self.rank} of {self.suit}"
#
#class Deck:
#    def __init__(self):
#        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
#        random.shuffle(self.cards)
#
#    def deal(self, num_cards):
#        dealt_cards = self.cards[:num_cards]
#        self.cards = self.cards[num_cards:]
#        return dealt_cards
#
#class PokerHand:
#    def __init__(self, cards):
#        self.cards = cards
#
#    def __str__(self):
#        return ', '.join(map(str, self.cards))
#
#def main():
#    deck = Deck()
#    num_players = 2
#    hands = [PokerHand(deck.deal(5)) for _ in range(num_players)]
#
#    for i, hand in enumerate(hands):
#        print(f"Player {i + 1}'s Hand: {hand}")
#
#    winner_index = evaluate_winner(hands)
#    print(f"\nPlayer {winner_index + 1} wins!")
#
#def evaluate_winner(hands):
#    # For simplicity, this example considers the highest card as the winner
#    def get_hand_value(hand):
#        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
#        sorted_cards = sorted(hand.cards, key=lambda card: values[card.rank], reverse=True)
#        return values[sorted_cards[0].rank]
#
#    winner_index = max(range(len(hands)), key=lambda i: get_hand_value(hands[i]))
#    return winner_index
#
#if __name__ == "__main__":
#    main()
