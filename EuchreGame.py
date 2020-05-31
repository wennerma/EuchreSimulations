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
  
  def play_card(self, suit_set):
    if suit_set == False:
      return self.hand.pop()
    else:
      # TODO: find correct suit to play
      return self.hand.pop()


class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def value(self, trump):
    if self.suit != trump:
      return RANKS.index(self.rank)
    
    # else we need to determine the rank of trump cards


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
    round = 0
    deck = self.create_deck()
    while round < self.number_of_rounds:
      random.shuffle(deck)

      # Randomize who gets dealt first card, should we deal first black jack?
      random.shuffle(self.players)

      self.deal_round(deck)
      trump = self.undealt_cards[0]
      print('Hand dealt with trump: ' + trump.suit)

      hand = 0
      while hand < 5:
        plays = []
        suit_set = False
        best_hand = {'player_id': '', 'card': ''}
        for i in self.players:
          card = i.play_card(suit_set)
          # This is the first card played, set the suit and assign it as best card by default
          if suit_set == False:
            suit_set = card.suit
            best_hand['player_id'] = i.id
            best_hand['card'] = card
          # else:
            # we'll compare each card as it's dealt, and keep the best_card
            
              
          plays.append(card)

          print('Player ' + str(i.id) + ' played ' + card.rank + ' of ' + card.suit)
        hand+=1

      print('Round ' + str(round) + ' complete')
      print('')
      print('')
      round+=1


simulation = Euchre(10, FREE_PLAY)
simulation.play()




