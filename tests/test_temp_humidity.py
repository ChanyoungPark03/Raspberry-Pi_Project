import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.temp_humidity import get_temp_humidity

import time

try:
    while True:
        t, h = get_temp_humidity()
        print(f"온도: {t:.1f}C, 습도: {h:.1f}%")
        time.sleep(2)
except KeyboardInterrupt:
    print("종료")

