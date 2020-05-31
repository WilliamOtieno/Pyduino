import pyfirmata
import time

board = pyfirmata.ArduinoMega('/dev/ttyACM0')

while True:
    board.digital[13].write(1)
    time.sleep(2)
    board.digital[13].write(0)
    time.sleep(1)