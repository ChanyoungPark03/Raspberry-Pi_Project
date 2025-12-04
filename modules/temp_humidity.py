import time
import board
import busio
import adafruit_htu21d

i2c = busio.I2C(board.SCL, board.SDA)
htu = adafruit_htu21d.HTU21D(i2c)

def get_temp_humidity():
    try:
        return round(htu.temperature, 1), round(htu.relative_humidity, 1)
    except:
        return 0.0, 0.0

