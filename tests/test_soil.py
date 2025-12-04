import os
import sys
import time

# 📌 modules 경로 추가
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from modules.soil_sensor import setup, is_dry, get_moisture_percent

# 센서 초기화
setup()
print("\n🌱 토양 수분 센서 상세 상태 테스트 시작 (Ctrl + C 종료)\n")

try:
    while True:
        moisture = get_moisture_percent()  # 수분 퍼센트
        dry = is_dry()                     # 건조하면 True (1), 아니면 False (0)

        # 🌾 토양 상태 판별
        if moisture < 30:
            status = "🌵 건조함 (물 필요!)"
        elif 30 <= moisture < 70:
            status = "🙂 적당한 흙 상태"
        elif 70 <= moisture < 90:
            status = "💧 촉촉한 상태 (좋음)"
        else:  # 물에 센서를 넣었거나 완전히 젖은 상태
            status = "🌊 물에 잠긴 상태 (센서 과습)"

        print(f"🧪 수분: {moisture}%  | 상태: {status} | dry_flag={dry}")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 사용자에 의해 종료됨")

