bearing = 0

def on_forever():
    global bearing
    bearing = input.compass_heading()
    if bearing > 365 or bearing < 15:
        basic.show_string("N")
    elif bearing < 195 and bearing > 165:
        basic.show_string("S")
    elif bearing < 105 and bearing > 65:
        basic.show_string("E")
    elif bearing < 285 and bearing > 255:
        basic.show_string("W")
    else:
        basic.show_string(" ")
basic.forever(on_forever)
