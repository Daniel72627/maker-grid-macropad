import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.encoder import RotaryEncoderHandler
from kmk.extensions.peg_oled import Oled, OledDisplayMode, OledReactionType

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D4, board.D5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I,
    ]
]

encoder_handler = RotaryEncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D6, board.D7, None, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU),),)

oled_ext = Oled(
    OledDisplayMode.TXT,
    OledReactionType.LAYER,
    i2c_device=None,
    channel=0,
    sda=board.D9,
    scl=board.D10,
)
keyboard.extensions.append(oled_ext)

if __name__ == '__main__':
    keyboard.go()