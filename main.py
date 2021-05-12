import time
import board
import busio
import adafruit_mpr121
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

key_mappings = {
    0: Keycode.Q,
    1: Keycode.W,
    2: Keycode.E,
    3: Keycode.R,
    4: Keycode.T,
    5: Keycode.Y,
    6: Keycode.U,
    7: Keycode.I,
    8: Keycode.O,
    9: Keycode.P,
    10: Keycode.LEFT_BRACKET,
    11: Keycode.RIGHT_BRACKET,
}

i2c = busio.I2C(board.GP1, board.GP0)
mpr121 = adafruit_mpr121.MPR121(i2c)

kbd = Keyboard(usb_hid.devices)


while True:
    touched = mpr121.touched_pins
    
    for key, val in key_mappings.items():
        if touched[key]:
            kbd.press(val)
        else:
            kbd.release(val)
            
    
    
