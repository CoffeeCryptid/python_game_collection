# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
right = True
paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT

paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == "RIGHT":
        ball_vel = [random.randrange(2, 4), -random.randrange(1, 3)]
    elif direction == "LEFT":
        ball_vel = [-random.randrange(2, 4), -random.randrange(1, 3)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    if right:
        spawn_ball("RIGHT")
    else:
        spawn_ball("LEFT")

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, right
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # bounce
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1

    # gutter, determine whether paddle and ball collide 
    if ball_pos[0]-BALL_RADIUS <= PAD_WIDTH:
        if paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            score2 += 1
            spawn_ball("RIGHT")
    if ball_pos[0]+BALL_RADIUS >= (WIDTH - PAD_WIDTH):
        if paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            score1 += 1
            spawn_ball("LEFT")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    #if paddle1_pos in range(0, HEIGHT-PAD_HEIGHT):
    paddle1_pos = min(max(paddle1_pos + paddle1_vel, 0), HEIGHT-PAD_HEIGHT)
    
    #if paddle2_pos in range(0, HEIGHT-PAD_HEIGHT):
    paddle2_pos = min(max(paddle2_pos + paddle2_vel, 0), HEIGHT-PAD_HEIGHT)
    
    # draw paddles
    # left paddle
    canvas.draw_polygon([(WIDTH, paddle1_pos), (WIDTH, paddle1_pos+PAD_HEIGHT), 
                         (WIDTH-PAD_WIDTH, paddle1_pos+PAD_HEIGHT), (WIDTH-PAD_WIDTH, paddle1_pos)], 
                        1, "#fff", "#fff")
    # right paddle
    canvas.draw_polygon([(0, paddle2_pos), (0, paddle2_pos+PAD_HEIGHT), 
                         (0+PAD_WIDTH, paddle2_pos+PAD_HEIGHT), (0+PAD_WIDTH, paddle2_pos)], 
                        1, "#fff", "#fff")
    
    # draw scores
    canvas.draw_text(str(score1), (250, 100), 32, "#0ff")
    canvas.draw_text(str(score2), (330, 100), 32, "#0ff")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 3
    if key == simplegui.KEY_MAP["down"]:
        paddle1_vel = vel
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel = -vel
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel = -vel
    if key == simplegui.KEY_MAP["s"]:
        paddle2_vel = vel
    
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key in [simplegui.KEY_MAP["up"], simplegui.KEY_MAP["down"]]:
        paddle1_vel = 0
    if key in [simplegui.KEY_MAP["s"], simplegui.KEY_MAP["w"]]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 150)


# start frame
new_game()
frame.start()
