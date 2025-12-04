from modules.temp_humidity import get_temp_humidity
from modules.soil_sensor import is_dry          # ⬅ 함수 이름 정확히 수정!
from modules.relay_control import relay_on, relay_off
from modules.lcd_display import lcd_init, lcd_print
import time

lcd_init()

while True:
    # 센서값 읽기
    temp, hum = get_temp_humidity()
    dry = is_dry()          # ⬅ 함수 사용도 수정

    # LCD 표시
    lcd_print(f"T:{temp:.1f}C H:{hum:.1f}%")
    time.sleep(1)
    lcd_print(f"Soil Dry: {dry}")
    time.sleep(1)

    # 릴레이 제어
    if dry:
        relay_on()     # 토양 건조 → 물 펌프 켜기
        lcd_print("Pump ON")
    else:
        relay_off()    # 토양 촉촉 → 물 펌프 끄기
        lcd_print("Pump OFF")
    
    time.sleep(2)

