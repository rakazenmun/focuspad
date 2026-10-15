"""Focuspad KMK firmware for the Seeed Studio XIAO RP2040."""

import board

from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation


keyboard = KMKKeyboard()

# PCB net mapping: three columns by two rows, with COL2ROW diodes.
keyboard.col_pins = (board.D0, board.D1, board.D6)
keyboard.row_pins = (board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# The 0.91-inch SSD1306 display is wired SDA, SCL, 5V, GND on D4/D5.
display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[
        TextEntry(text="FOCUSPAD", x=64, y=2, x_anchor="M"),
        TextEntry(text="COPY  PASTE  UNDO", x=64, y=15, x_anchor="M"),
        TextEntry(text="TAB+  FIND  ENTER", x=64, y=27, x_anchor="M"),
    ],
    width=128,
    height=32,
    dim_time=30,
    off_time=120,
)
keyboard.extensions.append(display)
keyboard.extensions.append(MediaKeys())

# Productivity layout. These are ordinary HID shortcuts and can be changed.
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
UNDO = KC.LCTL(KC.Z)
REOPEN_TAB = KC.LCTL(KC.LSFT(KC.T))
FIND = KC.LCTL(KC.F)

keyboard.keymap = [[COPY, PASTE, UNDO, REOPEN_TAB, FIND, KC.ENTER]]

# Clockwise/counter-clockwise control system volume; pressing the knob mutes.
encoder = EncoderHandler()
encoder.pins = ((board.D8, board.D7, board.D9, False),)
encoder.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)
keyboard.modules.append(encoder)


if __name__ == "__main__":
    keyboard.go()
