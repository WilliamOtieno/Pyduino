import pyfirmata
from pyfirmata.util import Iterator
import time

board = pyfirmata.ArduinoMega('/dev/ttyACM2')

it = Iterator(board)
it.start()

board.digital[10].mode = pyfirmata.INPUT

while True:
    switch = board.digital[10].read()
    if switch is True:
        board.digital[13].write(1)
        print("On")
    else:
        board.digital[13].write(0)
        print("Off")
    time.sleep(0.1)
