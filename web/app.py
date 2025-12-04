import os, sys, time, atexit
from flask import Flask, render_template, request, jsonify, redirect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from modules.temp_humidity import get_temp_humidity
from modules.soil_sensor import setup as soil_setup, is_dry, read_moisture_percent, cleanup
from modules.lcd_display import init_lcd, show_lcd_message

app = Flask(__name__)

logs = []
moisture_history = []

soil_setup()
init_lcd()

def add_log(message):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    logs.insert(0, f"[{ts}] {message}")
    logs[:] = logs[:50]

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/status")
def api_status():
    global moisture_history

    temp, hum = get_temp_humidity()
    moisture = read_moisture_percent()
    dry_flag = is_dry()

    moisture_state = "건조 🌵" if dry_flag else "촉촉 💧"

    line1 = f"T:{temp:.1f}C H:{hum:.1f}%"
    line2 = f"Moisture:{moisture}%"
    show_lcd_message(line1, line2)

    add_log(f"온도:{temp:.1f}°C / 습도:{hum:.1f}% / 수분:{moisture}% | {moisture_state}")

    moisture_history.append(moisture)
    moisture_history[:] = moisture_history[-30:]

    return jsonify({
        "temperature": round(temp, 1),
        "humidity": round(hum, 1),
        "moisture": moisture,
        "moisture_state": moisture_state,
        "logs": logs,
        "moisture_history": moisture_history
    })

atexit.register(cleanup)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

