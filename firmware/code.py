import board
import digitalio
import analogio
import usb_hid
from hid_gamepad import Gamepad

import time

gp = Gamepad(usb_hid.devices)


# Create some buttons. The physical buttons are connected
# to ground on one side and these and these pins on the other.
button_pins = (board.GP2, board.GP3, board.GP4, board.GP5)

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.

gamepad_buttons = (1, 2, 8, 15)
buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]

for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Connect an analog two-axis joystick to A4 and A5.
a0 = analogio.AnalogIn(board.A0)
a1 = analogio.AnalogIn(board.A1)
a2 = analogio.AnalogIn(board.A2)
a3 = analogio.AnalogIn(board.A3)

# Equivalent of Arduino's map() function.

def range_map(x, in_min, in_max, out_min, out_max):

    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min



while True:

    # Buttons are grounded when pressed (.value = False).

#    for i, button in enumerate(buttons):
#        gamepad_button_num = gamepad_buttons[i]
#        if button.value:
#            gp.release_buttons(gamepad_button_num)
#            print(" release", gamepad_button_num, end="")
#        else:
#            gp.press_buttons(gamepad_button_num)
#            print(" press", gamepad_button_num, end="")


    # Convert range[0, 65535] to -127 to 127

    gp.move_joysticks(
        x=range_map(a0.value, -65535, 65535, -127, 127),
    )

    # print(" x", ax.value, "y", ay.value)


    # print( a0.value, ";", a1.value, ";", a2.value, ";", a3.value)
    # print( a0.value)
    # print("analog 0", a0.value)
    # print("analog 1", a1.value)
    # print("analog 2", a2.value)
    # print("analog 3", a3.value)
    # print("------------------")

    voltage = a0.value * 3.3 / 65536
    print("VALUE", voltage)

    # time.sleep(0.3) # TODO remove this later
