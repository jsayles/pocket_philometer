# SPDX-FileCopyrightText: 2020 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# CircuitPython Bluefruit LE Connect Plotter Example

import time
import board
import analogio
import adafruit_thermistor
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)
light = analogio.AnalogIn(board.LIGHT)
gsr = analogio.AnalogIn(board.A1)


def scale(value, scale=50):
    """Scale the light sensor values from 0-65535 (AnalogIn range)
    to 0-50 (arbitrarily chosen to plot well with temperature)"""
    return value / 65535 * scale


while True:
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        # Print statement for the mu_editor plotter
        print(f"({gsr.value},{light.value})")

        # Uart write for the Bluefruit app plotter
        uart_server.write(f"{gsr.value},{light.value}\n")

        time.sleep(0.1)
