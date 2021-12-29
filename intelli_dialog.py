from microbit import *

decision = 0
text = ['Has feathers?', 'Can fly?', 'Has finns?', 'Hawk', 'Penguin', 'Dolphin', 'Bear']

while True:
    if decision == 0:
        if button_a.was_pressed():
            # go to 1
            decision = 1
        elif button_b.was_pressed():
            # go to 2
            decision = 2

    if decision == 1:
        if button_a.was_pressed():
            # go to 3
            decision = 3
        elif button_b.was_pressed():
            # go to 4
            decision = 4

    if decision == 2:
        if button_a.was_pressed():
            # go to 5
            decision = 5
        elif button_b.was_pressed():
            # go to 6
            decision = 6

    display.scroll(text[decision])
