from random import shuffle
from itertools import product

class _Suit(object):
    def __init__(self, name):
        assert(name in ["Spades", "Hearts", "Clubs", "Diamonds"])
        self.__name = name

    @property
    def name(self):
        return self.__name

_spades = _Suit("Spades")
_hearts = _Suit("Hearts")
_clubs = _Suit("Clubs")
_diamonds = _Suit("Diamonds")

class _Rank(object):
    def __init__(self, name, values):
        self.__name = name
        self.__values = values

    @property
    def name(self):
        return self.__name

    @property
    def values(self):
        return self.__values

class _Ace(_Rank):
    def __init__(self):
        super(_Ace, self).__init__("Ace", [1,11])

class _NumberCard(_Rank):
    def __init__(self, value):
        assert(value >= 2 and value <= 10)
        super(_NumberCard, self).__init__(value, [value])

class _PictureCard(_Rank):
    def __init__(self, name):
        assert(name in ["Jack", "Queen", "King"])
        super(_PictureCard, self).__init__(name, [10])

_ace = _Ace()
_jack = _PictureCard("Jack")
_queen = _PictureCard("Queen")
_king = _PictureCard("King")

class _Card(object):
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit.name

    @property
    def rank(self):
        return self.__rank.name

    @property
    def values(self):
        return self.__rank.values

    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)

def standard_deck():
    return [ _Card(suit, rank) \
             for suit in [_spades, _hearts, _clubs, _diamonds] \
             for rank in [_ace] + \
                         [_NumberCard(x) for x in range(2, 11)] + \
                         [_jack, _queen, _king]]

def shuffle_deck(deck):
    shuffled_deck = deck[:]
    shuffle(shuffled_deck)
    return shuffled_deck

def deal(num_players, deck):
    num_hands = num_players + 1
    num_cards = num_hands * 2
    remaining_deck = deck[num_cards:]
    hands = zip(deck[:num_hands], deck[num_hands:num_cards])
    return (hands, remaining_deck)

def hand_value(hand):
    possible_values = [sum(x) for x in product(*[ card.values for card in hand ])]
    valid_values = [value for value in possible_values if value <= 21]
    bust_values = [value for value in possible_values if value > 21]
    if valid_values:
        return max(valid_values)
    else:
        return min(bust_values)

def is_blackjack(hand):
    return len(hand) == 2 and hand_value(hand) == 21

def is_bust(hand):
    return hand_value(hand) > 21

def parse_suit(s):
    if s == "S":
        return _spades
    elif s == "H":
        return _hearts
    elif s == "C":
        return _clubs
    elif s == "D":
        return _diamonds
    else:
        raise ValueError("Invalid suit '%s' requested - must be one of ['S', 'H', 'C', 'D']" % s)

def parse_rank(r):
    if r == "A":
        return _ace
    elif r == "J":
        return _jack
    elif r == "Q":
        return _queen
    elif r == "K":
        return _king
    else:
        try:
            return _NumberCard(int(r))
        except:
            raise ValueError("Invalid rank '%s' requested - must be one of " + \
                             "['A', 'J', 'Q', 'K'] or in range(2,11)" % r)

def parse_card(card):
    suit = parse_suit(card[-1:])
    rank = parse_rank(card[:-1])
    return _Card(suit, rank)

def parse_hand(hand):
    return [parse_card(card) for card in hand.split(" ")]

def main():
    hands, deck = deal(3, shuffle_deck(standard_deck()))

    for hand in hands:
        for card in hand:
            print card
        print "Hand value: %s" % ("Blackjack" if is_blackjack(hand) else hand_value(hand))
        print

    for card in deck:
        print card

if __name__ == "__main__":
    main()
