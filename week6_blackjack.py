# Mini-project #6 - Blackjack

import simplegui
import random
import time

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    
HOLE_POSITION = [75, 125]

# initialize some useful global variables
in_play = False
outcome = ""
score = [0, 0]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        c = [str(card) for card in self.cards]
        return "Hand contains: " + ", ".join(c)

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ranks = [card.get_rank() for card in self.cards]
        count = 0
        for rank in ranks:
            count += VALUES[rank]
        if "A" in ranks and count < 12:
            count += 10
        return count
   
    def draw(self, canvas, pos):
        for i, card in enumerate(self.cards):
            pos_card = [(pos[0] + (CARD_SIZE[0]+10) * i), pos[1]]
            card.draw(canvas, pos_card)
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)
    
    def __str__(self):
        c = [str(card) for card in self.cards]
        return "Deck contains: " + ", ".join(c)



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand

    if not timer.is_running():
        if in_play:
            outcome = "You lost the round!"
            score[1] += 1
            in_play = False
            timer.start()

        else:
            #Initialize deck
            deck = Deck()
            deck.shuffle()

            #Initialize player hand
            player_hand = Hand()
            player_hand.add_card(deck.deal_card())
            player_hand.add_card(deck.deal_card())

            #Initialize dealer hand
            dealer_hand = Hand()
            dealer_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card())

            in_play = True

            outcome = "Hit or stand?"

def hit():
    global in_play, deck, player_hand, dealer_hand, outcome
    # if the hand is in play, hit the player
    if not in_play:
        if not timer.is_running():
            outcome = "New deal?"
    else:
        player_hand.add_card(deck.deal_card())
    
    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You have busted! You lost!"
            score[1] += 1
            in_play = False
       
def stand():
    global in_play, deck, player_hand, dealer_hand, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if not in_play:
        if not timer.is_running():
            outcome = "New deal?"
        
    else:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
    
        if dealer_hand.get_value() > 21:
            outcome = "Dealer has busted! You won!"
            score[0] += 1
            
        elif player_hand.get_value() > dealer_hand.get_value():
            outcome = "The player has won!"
            score[0] += 1
            
        else:
            outcome = "The dealer has won!"
            score[1] += 1
            
        in_play = False

# draw handler    
def draw(canvas):
    global in_play
    canvas.draw_text("Blackjack", [215, 50], 35, "#fff")
    player_hand.draw(canvas, [75, 400]) #Player hand
    dealer_hand.draw(canvas, HOLE_POSITION) #Dealer hand
    canvas.draw_text(outcome, [75, 320], 30, "#fff")
    canvas.draw_text("Player: {}, Dealer: {}".format(score[0], score[1]), [380, 575], 20, "#fff")
    if in_play:
        if dealer_hand.cards[0].get_suit() in ["C", "H"]:
            card_loc = CARD_BACK_CENTER
        else:
            card_loc = [CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0], CARD_BACK_CENTER[1]]
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, 
                          [HOLE_POSITION[0] + CARD_BACK_CENTER[0], 
                           HOLE_POSITION[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

def timer_handler():
    timer.stop()
    deal()

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(2000, timer_handler)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric