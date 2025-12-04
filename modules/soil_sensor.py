import RPi.GPIO as GPIO

SOIL_PIN = 17  # 토양 수분센서 DO핀

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOIL_PIN, GPIO.IN)

def is_dry():
    return GPIO.input(SOIL_PIN) == GPIO.HIGH  # 건조=True

def read_moisture_percent():
    """
    테스트 코드처럼 실제 센서 반응 기반으로 수분량 계산
    물에 닿으면 LOW → 젖음 → 높은 수분값
    흙/공기 중이면 HIGH → 건조 → 낮은 수분값
    """
    raw = GPIO.input(SOIL_PIN)
    
    if raw == GPIO.LOW:   # 물에 젖음
        return 75         # (70~90 범위에서 자유 조절 가능)
    else:                # 건조 상태
        return 28         # (25~35 범위 자유 조절 가능)

def cleanup():
    GPIO.cleanup()

