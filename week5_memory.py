# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, state, exposed_cards, turns
    cards = [*range(0, 8)] + [*range(0, 8)]
    random.shuffle(cards)
    exposed = [False] * 16
    state = 0
    turns = 0
    exposed_cards = []
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed_cards, turns
    i = pos[0] // 50
    if not exposed[i] and state < 2:
        exposed[i] = True
        state += 1
        exposed_cards.append(i)
        if state == 2:
            turns += 1
            label.set_text("Turns = " + str(turns))
    elif not exposed[i] and state == 2:
        exposed[i] = True
        state = 1
        label.set_text("Turns = " + str(turns))
        if cards[exposed_cards[0]] != cards[exposed_cards[1]]:
            exposed[exposed_cards[0]] = False
            exposed[exposed_cards[1]] = False
        exposed_cards = [i]
            
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i, card in enumerate(cards):
        if exposed[i]:
            if i in exposed_cards:
                color = "#fff"
            else:
                color = "#49cee4"
            canvas.draw_text(str(card), [10 + i*50, 70], 50, color)
            canvas.draw_polygon([[0 + i*50, 0], [49 + i*50, 0], [49 + i*50, 100], [0 + i*50, 100]],
                                2, color)
        else:
            points = [[0 + i*50, 0], [49 + i*50, 0], [49 + i*50, 100], [0 + i*50, 100]]
            canvas.draw_polygon(points, 1, "#25be9e", "#1a7761")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background("#123450")
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric