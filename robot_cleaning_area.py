from karel.stanfordkarel import *

def main():
    pick_obj()
    new_line()
    pick_obj()
    turn_right()
    move()
    while beepers_present():
        pick_beeper()
    turn_right()
    pick_obj()
    new_line()
    pick_obj()
    turn_right()
    move()
    while beepers_present():
        pick_beeper()
    turn_right()
    pick_obj()
    new_line()
    pick_obj()
def pick_obj():
    while front_is_clear():
        while beepers_present():
            pick_beeper()
        move()
def new_line():
    turn_left()
    while beepers_present():
        pick_beeper()
    move()
    turn_left()
def turn_right():
    for i in range(3):
        turn_left()
    
# don't change this code
if __name__ == '__main__':
    main()