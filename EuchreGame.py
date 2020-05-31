import random

SPADE = 'spades'
CLUB = 'clubs'
HEART = 'hearts'
DIAMOND = 'diamonds'
ACE = 'Ace'
KING = 'king'
QUEEN = 'queen'
JACK = 'jack'
RANKS = ['9', '10', JACK, QUEEN, KING, ACE]
SUITS = [SPADE, CLUB, HEART, DIAMOND]
FREE_PLAY = 'free_play'

class Player:
  def __init__(self, id):
    self.hand = []
    self.id = id

  def add_cards(self, cards):
    self.hand.append(cards)
  
  def play_card(self):
    card = self.hand.pop()

    return card


class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank


class Euchre:
  def __init__(self, number_of_rounds, mode):
    self.number_of_rounds = number_of_rounds
    self.players = [Player(1), Player(2), Player(3), Player(4)]
    self.undealt_cards = []
    self.mode = mode

  def create_deck(self):
    deck = []

    for rank in RANKS:
        for suit in SUITS:
            card = Card(suit, rank)
            deck.append(card)
    
    return deck

  def deal_round(self, deck):
    count = 0
    for i in deck:
      if 0 <= count < 2 or 10 <= count < 13:
        self.players[0].add_cards(i)
      elif 2 <= count < 5 or 13 <= count < 15:
        self.players[1].add_cards(i)
      elif 5 <= count < 7 or 15 <= count < 18:
        self.players[2].add_cards(i)
      elif 7 <= count < 10 or 18 <= count < 20:
        self.players[3].add_cards(i)
      else:
        self.undealt_cards.append(i)

      count+=1


  def play(self):
    game = 0

    while game < self.number_of_rounds:
      deck = self.create_deck()
      random.shuffle(deck)
      self.deal_round(deck)
      trump = self.undealt_cards[0]
      print('Hand dealt with trump: ' + trump.suit)

      hand = 0
      while hand < 5:
        plays = []
        for i in self.players:
          card = i.play_card()
          plays.append(card)

          print('Player ' + str(i.id) + ' played ' + card.rank + ' of ' + card.suit)
        hand+=1

      print('Round ' + str(game) + ' complete')
      print('')
      print('')
      game+=1



simulation = Euchre(10, FREE_PLAY)
simulation.play()



