# i2c_lcd_driver.py

# smbus 불러오기 (smbus 없으면 smbus2 사용하기)
try:
    import smbus
except ImportError:
    import smbus2 as smbus

from time import sleep

# LCD 기본 설정
LCD_ADDR = 0x27      # sudo i2cdetect -y 1 결과에서 확인된 주소
LCD_WIDTH = 16       # 한 줄에 표시할 수 있는 문자 수

LCD_CHR = 1          # 문자 모드
LCD_CMD = 0          # 명령 모드

LCD_LINE_1 = 0x80    # LCD 첫 번째 줄 주소
LCD_LINE_2 = 0xC0    # LCD 두 번째 줄 주소

LCD_BACKLIGHT = 0x08  # LCD 백라이트 ON
ENABLE = 0b00000100   # Enable 비트

# I2C 버스 열기 (채널 1 사용)
bus = smbus.SMBus(1)


# LCD 초기화 함수
def lcd_init():
    lcd_write(0x33, LCD_CMD)
    lcd_write(0x32, LCD_CMD)
    lcd_write(0x06, LCD_CMD)
    lcd_write(0x0C, LCD_CMD)
    lcd_write(0x28, LCD_CMD)
    lcd_write(0x01, LCD_CMD)
    sleep(0.005)


# LCD에 데이터 쓰기
def lcd_write(bits, mode):
    upper_bits = mode | (bits & 0xF0) | LCD_BACKLIGHT
    lower_bits = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    bus.write_byte(LCD_ADDR, upper_bits)
    lcd_toggle_enable(upper_bits)

    bus.write_byte(LCD_ADDR, lower_bits)
    lcd_toggle_enable(lower_bits)


# Enable 핀 토글
def lcd_toggle_enable(bits):
    sleep(0.0005)
    bus.write_byte(LCD_ADDR, (bits | ENABLE))
    sleep(0.0005)
    bus.write_byte(LCD_ADDR, (bits & ~ENABLE))
    sleep(0.0005)


# 한 줄에 문자열 출력하는 함수
def lcd_display_string(message, line):
    lcd_write(line, LCD_CMD)
    message = message.ljust(LCD_WIDTH, " ")
    for char in message:
        lcd_write(ord(char), LCD_CHR)


# LCD 초기화 후 2줄 출력하는 함수
def lcd_display_message(line1, line2=""):
    lcd_init()
    lcd_display_string(line1, LCD_LINE_1)
    if line2:
        lcd_display_string(line2, LCD_LINE_2)


# LCD 화면 지우기 함수
def lcd_clear():
    lcd_write(0x01, LCD_CMD)
    sleep(0.005)


# 디버깅용 실행 테스트
if __name__ == "__main__":
    lcd_display_message("Smart Farm", "LCD Test OK!")
    sleep(5)
    lcd_clear()

