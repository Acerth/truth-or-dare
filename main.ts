input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Tr_or_Da = randint(0, 1)
    if (Tr_or_Da == 1) {
        basic.showString("Truth")
    } else {
        basic.showString("Dare")
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Direction2 = 0
    basic.clearScreen()
    Direction2 = randint(0, 7)
    if (Direction2 == 0) {
        basic.showArrow(ArrowNames.North)
    } else if (Direction2 == 1) {
        basic.showArrow(ArrowNames.East)
    } else if (Direction2 == 2) {
        basic.showArrow(ArrowNames.South)
    } else if (Direction2 == 3) {
        basic.showArrow(ArrowNames.West)
    } else if (Direction2 == 4) {
        basic.showArrow(ArrowNames.NorthEast)
    } else if (Direction2 == 5) {
        basic.showArrow(ArrowNames.SouthEast)
    } else if (Direction2 == 6) {
        basic.showArrow(ArrowNames.SouthWest)
    } else {
        basic.showArrow(ArrowNames.NorthWest)
    }
    
})
let Direction2 = 0
let Tr_or_Da = 0
basic.showString("Truth or Dare?")
