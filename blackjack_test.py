import blackjack

def test_deck_has_52_cards():
    assert len(blackjack.standard_deck()) == 52

def test_deck_has_13_of_each_suit():
    for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
        yield (has_13_in_suit, suit)

def has_13_in_suit(suit):
    cards = [card for card in blackjack.standard_deck() if card.suit == suit]
    assert len(cards) == 13

def test_deck_has_4_aces():
    has_4_of_rank("Ace")

def test_deck_has_4_of_each_number():
    for rank in range(2, 11):
        yield(has_4_of_rank, rank)

def test_deck_has_4_of_each_picture_card():
    for rank in ["Jack", "Queen", "King"]:
        yield(has_4_of_rank, rank)

def has_4_of_rank(rank):
    cards = [card for card in blackjack.standard_deck() if card.rank == rank]
    assert len(cards) == 4

def test_deck_has_no_duplicates():
    card_names = [str(card) for card in blackjack.standard_deck()]
    assert len(set(card_names)) == 52

def test_hand_value():
    for hand in [("2H 2C", 4),
                 ("2H 2C 2D 2S", 8),
                 ("2H 2C 7S 8D", 19),
                 ("KH 5C 6S", 21),
                 ("KH QC 3S", 23),
                 ("9H AC 3S KS", 23),
                 ("JH 8C 9S", 27),
                 ("AS KS", 21),
                 ("AS 5H", 16),
                 ("AS 5H 7C", 13),
                 ("AS AC", 12),
                 ("AS AC AD AH", 14),
                 ("AS AC KC", 12),
                 ("AS AC AH AD KC", 14),
                 ("AS AC AH AD KC JH", 24),
                 ("10H QC AS", 21)]:
        yield(hand_has_value, hand[0], hand[1])

def hand_has_value(hand_code, value):
    hand = blackjack.parse_hand(hand_code)
    assert blackjack.hand_value(hand) == value
