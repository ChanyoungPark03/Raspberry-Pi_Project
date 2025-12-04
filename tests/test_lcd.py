# tests/test_lcd.py

import os
import sys

# smart_pot 루트를 import 경로에 추가
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from modules.lcd_display import display_message, clear_lcd  # 래퍼 함수 불러오기
from time import sleep


def main():
    print("LCD 테스트: 파란 화면에 글자가 나오는지 확인하세요.")

    # 1줄만 출력
    display_message("Smart Pot", "LCD Test")

    # 5초 동안 보여주기
    sleep(5)

    # 화면 지우기
    clear_lcd()
    print("테스트 종료.")


if __name__ == "__main__":
    main()

