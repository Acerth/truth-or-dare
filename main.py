def on_button_pressed_a():
    global Tr_or_Da
    Tr_or_Da = randint(0, 1)
    if Tr_or_Da == 1:
        basic.show_string("Truth")
    else:
        basic.show_string("Dare")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Direction2
    Direction2 = 0
    basic.clear_screen()
    Direction2 = randint(0, 7)
    if Direction2 == 0:
        basic.show_arrow(ArrowNames.NORTH)
    elif Direction2 == 1:
        basic.show_arrow(ArrowNames.EAST)
    elif Direction2 == 2:
        basic.show_arrow(ArrowNames.SOUTH)
    elif Direction2 == 3:
        basic.show_arrow(ArrowNames.WEST)
    elif Direction2 == 4:
        basic.show_arrow(ArrowNames.NORTH_EAST)
    elif Direction2 == 5:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif Direction2 == 6:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    else:
        basic.show_arrow(ArrowNames.NORTH_WEST)
input.on_button_pressed(Button.B, on_button_pressed_b)

Direction2 = 0
Tr_or_Da = 0
basic.show_string("Truth or Dare?")