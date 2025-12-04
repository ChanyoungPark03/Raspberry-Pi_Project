# modules/relay_control.py
import RPi.GPIO as GPIO
import time

# 라즈베리파이에서 릴레이 S(신호선)가 연결된 핀 번호 (BCM 기준)
RELAY_PIN = 17   # 너가 GPIO17에 꽂았으니까 그대로 사용

def init_relay():
    """릴레이 GPIO 초기 설정 (프로그램 시작할 때 한 번만 호출)"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT)

    # 기본은 꺼진 상태로
    GPIO.output(RELAY_PIN, GPIO.LOW)
    print("Relay initialized (OFF).")

def relay_on():
    """릴레이 ON (워터펌프 켜기)"""
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    print("Relay ON -> Pump ON")

def relay_off():
    """릴레이 OFF (워터펌프 끄기)"""
    GPIO.output(RELAY_PIN, GPIO.LOW)
    print("Relay OFF -> Pump OFF")

def cleanup_relay():
    """프로그램 끝날 때 GPIO 정리"""
    GPIO.output(RELAY_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("Relay GPIO cleanup done.")

