from . import i2c_lcd_driver
from time import sleep

def init_lcd():
    try:
        i2c_lcd_driver.lcd_display_message("Smart Farm", "LCD Ready")
        sleep(2)
        i2c_lcd_driver.lcd_clear()
    except Exception as e:
        print(f"LCD 초기화 실패: {e}")

def show_lcd_message(line1, line2=""):
    try:
        i2c_lcd_driver.lcd_display_message(line1, line2)
    except Exception as e:
        print(f"LCD 표시 실패: {e}")

