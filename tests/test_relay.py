# tests/test_relay.py
from modules.relay_control import init_relay, relay_on, relay_off, cleanup_relay
import time

if __name__ == "__main__":
    init_relay()

    try:
        while True:
            print("3초간 펌프 ON")
            relay_on()
            time.sleep(3)

            print("3초간 펌프 OFF")
            relay_off()
            time.sleep(3)

    except KeyboardInterrupt:
        print("사용자 종료(Ctrl+C)")
    finally:
        cleanup_relay()

