# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
stops = 0
wins = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(n):
    a = n // 600
    b = (n % 600) // 10
    c = n % 10
    return "{:d}:{:02d}.{:d}".format(a, b, c)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global stops, wins
    if (timer.is_running()):
        timer.stop()
        stops += 1
        if time % 10 == 0:
            wins += 1

def reset():
    global time, stops, wins
    timer.stop()
    time = 0
    stops = 0
    wins = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text("{}/{}".format(wins, stops), (300, 50), 20, "#fff")
    canvas.draw_text(format(time), (150, 150), 35, "#fff")

    
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 300)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
