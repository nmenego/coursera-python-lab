# "Stopwatch: The Game"
# by nmenego

import simplegui

# define global variables
interval = 100
time = 0
# score/tries
tries = 0
score = 0
# running flag
running = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = str(t//600)
    mod = str(t%600).rjust(3,'0')
    seconds = mod[:2]
    mseconds = mod[-1]
    fmt_time = minutes + ":" + seconds + "." + mseconds
    return fmt_time

def check_time_0():
    """ Checks if time is whole number """
    mod = time%600%10 
    if(mod == 0):
        return True;
    return False;
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_time():
    global running
    running = True
    timer.start()

def stop_time():
    global running, score, tries
    # only change score if currently running
    if(running):
        if(check_time_0()):
            score += 1
        tries += 1
    running = False
    timer.stop()

def reset_time():
    global time, running, score, tries
    if(running):
        timer.stop()
    running = False
    time = 0
    score = 0
    tries = 0

# define event handler for timer with 0.1 sec interval
def time_increment():
    global time
    time += 1
    print "time:", time

# define draw handler
def draw(canvas):
    global score, tries
    screen_text = format(time)
    score_text = str(score) + "/" + str(tries)
    canvas.draw_text(screen_text, [90,112], 48, "Red")
    canvas.draw_text(score_text, [210,40], 48, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)
frame.add_button("Start", start_time)
frame.add_button("Stop", stop_time)
frame.add_button("Reset", reset_time)
frame.set_draw_handler(draw)

# register event handlers
timer = simplegui.create_timer(interval, time_increment)

# start frame
frame.start()
