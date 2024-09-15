import time
import board
import analogio

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_circuitplayground import cp


LED_BRIGHTNESS = 0.15
RANGE_THRESHOLD = 1000
DELAY = 0.1


class GSRSensor:
    def __init__(self, pin):
        self.pin = pin
        self.sensor = analogio.AnalogIn(pin)
        self.value = None
        self.min_value = None
        self.max_value = None

    @property
    def range(self):
        if self.min_value and self.max_value:
            return self.max_value - self.min_value
        return 0

    def read(self):
        self.value = self.sensor.value
        if self.min_value is None or self.value < self.min_value:
            self.min_value = self.value
        if self.max_value is None or self.value > self.max_value:
            self.max_value =self. value
        return self.value
    
    def has_data(self):
        if self.range > RANGE_THRESHOLD:
            return True
        return False


gsr = GSRSensor(board.A1)

ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

cp.pixels.brightness = LED_BRIGHTNESS


def calculate_color(gsr_sensor):
    if not gsr_sensor.has_data():
        # No data yet, return blue
        return (0, 0, 255)

    scaled_value = gsr_sensor.value - gsr_sensor.min_value
    red = int(scaled_value / gsr_sensor.range * 255)
    green = int((gsr_sensor.range - scaled_value)/gsr_sensor.range * 255)

    return (red, green, 0)


while True:
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        # Read the sensor values
        gsr_value = gsr.read()
        gsr_min = gsr.min_value
        gsr_max = gsr.max_value

        # Calculate the color based on the sensor values
        color = calculate_color(gsr)
        cp.pixels.fill(color)

        # Print statement for the mu_editor plotter
        print(f"({gsr_value},{gsr_min},{gsr_max})")

        # Uart write for the Bluefruit app plotter
        uart_server.write(f"{gsr_value},{gsr_min},{gsr_max}\n")

        time.sleep(DELAY)
