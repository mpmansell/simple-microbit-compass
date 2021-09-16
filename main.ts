let bearing = 0
basic.forever(function () {
    bearing = input.compassHeading()
    if (bearing > 365 || bearing < 15) {
        basic.showString("N")
    } else if (bearing < 195 && bearing > 165) {
        basic.showString("S")
    } else if (bearing < 105 && bearing > 65) {
        basic.showString("E")
    } else if (bearing < 285 && bearing > 255) {
        basic.showString("W")
    } else {
        basic.showString(" ")
    }
})
