import time
import board

from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
from connected_variables import ConnectedVariables

cv = ConnectedVariables()
cv.define('voltage', 0.0)
cv.define('threshold', 3.0)

analog_in = AnalogIn(board.IO1)

led = DigitalInOut(board.IO44)
led.direction = Direction.OUTPUT

def get_voltage(pin):
    return (pin.value * 3.3) / 65536


print('startplot:', 'voltage', 'threshold')
while True:
    voltage = get_voltage(analog_in)
    cv.write('voltage', voltage)
    threshold = cv.read('threshold')
    print(voltage, threshold)
    if voltage < threshold:
        led.value = False
    else:
        led.value = True
    time.sleep(0.1)