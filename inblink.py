import pyfirmata
import time

board = pyfirmata.ArduinoMega('/dev/ttyACM1')

while True:
    board.digital[13].write(1)
    print("On")
    time.sleep(1)
    board.digital[13].write(0)
    print("Off")
    time.sleep(0.5)
